import torch
import numpy as np
from torch.autograd import Variable
import net_sphere
import cv2
import mxnet as mx
from mtcnn_detector import MtcnnDetector
import matplotlib.pyplot as plt
import sys
from matlab_cp2tform import get_similarity_transform_for_cv2
from torch.autograd import Variable
import threading
import sys

class MyApi(threading.Thread):
	###Mtcnn人脸检测部分
	def __init__(self):
		threading.Thread.__init__(self)
		self.detector = MtcnnDetector(model_folder='mtcnnmodel', ctx=mx.gpu(0), num_worker=1, accurate_landmark=False)
		self.imgset=self.readFaceFeatureALL()
		self.threadhold = 0.45  # 设定阈值
		self.net = getattr(net_sphere,'sphere20a')()
		self.net.load_state_dict(torch.load('model/sphere20a_20171020.pth'))
		self.net.cuda()
		self.net.eval()
		self.net.feature = True
	##人脸关键点检测：输入一张原始图片，返回检测到所有人脸的五个关键点（face*10）10个float数值表示五个关键点的位置和检测到人脸的矩形框
	def faceDetect(self,img):
		results = self.detector.detect_face(img)
		if results is None:
			print("No face detected")
			return None,None
		all_box=results[0]
		img_points=results[1];
		for i in range(len(img_points)):
			this_point=[]
			for j in range(5):
				this_point.append(img_points[i][j])
				this_point.append(img_points[i][j+5])
			img_points[i]=this_point
		return img_points,all_box

	##人脸矫正：输入原始图像和五个关键点，返回矫正厚的人脸图像
	def alignment(self,src_img,src_pts):
		ref_pts = [ [30.2946, 51.6963],[65.5318, 51.5014],[48.0252, 71.7366],[33.5493, 92.3655],[62.7299, 92.2041]]
		crop_size = (96, 112)
		src_pts = np.array(src_pts).reshape(5,2)
		s = np.array(src_pts).astype(np.float32)
		r = np.array(ref_pts).astype(np.float32)
		tfm = get_similarity_transform_for_cv2(s, r)
		face_img = cv2.warpAffine(src_img, tfm, crop_size)
		return face_img


	###sphereface人脸识别部分

	##特征计算（sphereface卷积）：输入人脸图片列表，返回特征列表（face*512dim）
	def imageCNN(self,face_img_list):
		for i in range(len(face_img_list)):
			face_img_list[i] = face_img_list[i].transpose(2, 0, 1).reshape((1,3,112,96))
			face_img_list[i] = (face_img_list[i]-127.5)/128.0
		img = np.vstack(face_img_list)
		img = Variable(torch.from_numpy(img).float(),volatile=True).cuda()
		output = self.net(img)
		return output.data

	##余弦距离计算：输入两个特征向量，返回两者之间的余弦距离
	def computeDistance(self,a,b):
		return a.dot(b)/(a.norm()*b.norm()+1e-5)

	##人脸对比：输入两个人脸图片，返回两张人脸图片间的距离
	def faceCompare(self,face_img1,face_img2):##both are image(np.array)
		feature=self.imageCNN([face_img1,face_img2])
		return self.computeDistance(feature[0],feature[1])

	##人脸查找：输入一张人脸图片和一个含有多张人脸图片的列表，返回目标人脸和列表中所有人脸最相似的一张人脸的序号和相似度
	def faceFind(self,face_img1,face_imgs_list):##img1 is a image(np.array),imags is a lsit of images
		face_imgs_list.insert(0,face_img1)
		feature=self.imageCNN(face_imgs_list)
		distance_list=[]
		for i in feature[1:]:
			distance_list.append(self.computeDistance(feature[0],i))
		return np.argmax(distance_list),np.max(distance_list)

	##检测所有人脸：输入一张原始照片，返回检测到的所有人脸的图片列表
	def detectAllFaces(self,img):
		key_points,all_box=self.faceDetect(img)
		if key_points is None:
			return None
		face_img_list=[]
		for i in key_points:
			face_img_list.append(self.alignment(img,i))
		return face_img_list

	##增加人脸：输入人脸名称和原始图片（只可包含一张人脸）。将名称和图片中人脸的特征向量存到‘imageSet.txt’中
	def addImage(self,name,img_path):
		img=cv2.imread(img_path)
		face_list=self.detectAllFaces(img)
		if face_list is None:
			return
		else:
			feature=self.imageCNN(face_list).numpy()[0]
			with open('imageSet.txt','a+') as f:
				f.write(name+' ')
				for i in feature:
					f.write(str(i)+' ')
				f.write('\n')
				self.writeImage(name,img)
	##添加照片第二步:写照片
	def writeImage(self,name,img):
		results = self.detector.detect_face(img)
		if results is not None:
			total_boxes = results[0]
			points = results[1]
		# extract aligned face chips
		chips = self.detector.extract_image_chips(img, points, 144, 0.37)
		for i, chip in enumerate(chips):
			cv2.imwrite('./img/' + name + '.jpg', chip)
	##人脸查找(从imageSet.txt中查找)：输入人脸图片，计算其特征向量，并打开imageSet。找到相似的一张人脸，返回名称和相似度
	def faceFindFromSet(self,face_img):
		feature=self.imageCNN([face_img])
		imgset={}
		with open("imageSet.txt") as f:
			alllines=f.readlines()
		for line in alllines:
			line=line.replace('\n','').split(' ')
			imgset[line[0]]=torch.from_numpy(np.array([float(k) for k in line[1:-1]]).reshape(512)).float()
		distance={}
		for key in imgset:
			distance[key]=self.computeDistance(feature[0],imgset[key])
		max_item=max(distance.items(),key=lambda i:i[1])
		print(max_item[0],max_item[1])

	#根据需要查找的人名称查找对应的人脸特征向量：输入：人命列表["name"]，返回特征向量列表{"name":[featureVector]}
	def readFaceFeatureALL(self):
		imgset={}
		with open("imageSet.txt") as f:
			alllines=f.readlines()
		for line in alllines:
			line=line.replace('\n','').split(' ')
			imgset[line[0]]=torch.from_numpy(np.array([float(k) for k in line[1:-1]]).reshape(512)).float().cuda()
		return imgset
	def readFaceFeatureByname(self,names):
		imgset={}
		for name in names:
			if name in self.imgset:
				imgset[name]=self.imgset[name]
		return imgset
	#返回多个数据人脸检测：检测原始图像中所有的人脸，返回所有人脸的五个关键点，矩形框，特征向量。·[{"points":[point],"rect":[rect],"feature":[feature]},{}]
	def detailFaceDetect(self,img):
		key_points,all_box=self.faceDetect(img)
		if key_points is None:
			return None
		face_img_list=[]
		for i in key_points:
			face_img_list.append(self.alignment(img,i))
		features=self.imageCNN(face_img_list)
		detail_list=[]
		for i in range(len(key_points)):
			this_dict={}
			this_dict["points"]=key_points[i]
			this_dict["rect"]=all_box[i]
			this_dict["feature"]=features[i]
			detail_list.append(this_dict)
		return detail_list

	#将检测到的人脸同人脸库中的人脸进行对比：输入待检测图片，输出画完人脸的图片
	##人脸标记：输入原始图像并对比找到需求的人脸，找到所有人脸并绘制五个关键点位置和人脸矩形框。和detectAllFaces功能相似
	def markFace(self,img,names):
		if len(names)==0:
			return img
		detail_list=self.detailFaceDetect(img)
		if detail_list is None:
			return img
		face_set=self.readFaceFeatureByname(names)
		points_list=[]
		rect_list=[]
		for i in detail_list:
			for j in names:
				if self.computeDistance(i["feature"],face_set[j])>self.threadhold:
					points_list.append(i["points"])
					rect_list.append(i["rect"])
		for b in rect_list:
			cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255, 255, 255))
		for p in points_list:
			for i in range(0,10,2):
				cv2.circle(img, (p[i], p[i + 1]), 1, (0, 0, 255), 1)
		return img
#if __name__=='__main__':
	#api=MyApi()
	#api.addImage(sys.argv[1],"D:/Program Files/git_repository/sphereface_pytorch/sphereface_pytorch/img/backimg/"+sys.argv[2])
	##初始化检测器
	#detector = MtcnnDetector(model_folder='mtcnnmodel', ctx=mx.gpu(0), num_worker = 1 , accurate_landmark = False)
	#img1=cv2.imread("/home/seven/下载/testimg/chip03.jpg")
	#img2=cv2.imread("./img/c.jpg")
	#addImage('gunagu',img2)
	#cv2.imshow("detection result", markFace(img2))
	#cv2.waitKey(0)
	#plt.imshow(markFace(img2))
	#plt.show()
	#face_list1=detectAllFaces(img1)
	#face_list2=detectAllFaces(img2)
	#addImage('chip3',img)
	#face_list=detectAllFaces(img)
	#dis=faceCompare(face_list1[0],face_list2[0])
	#print(dis)
	# cap=cv2.VideoCapture('./videos/videoHD.mp4')
	# while(cap.isOpened()):
	# 	ret,frame = cap.read()
	# 	if frame is None:
	# 		break
	# 	frame=cv2.resize(frame,(400,271))
	# 	key_points,allbox=api.faceDetect(frame)
	# 	if key_points is not None:
	# 		for b in allbox:
	# 			cv2.rectangle(frame, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255, 255, 255))
	# 		for p in key_points:
	# 			for i in range(0,10,2):
	# 				cv2.circle(frame, (p[i], p[i + 1]), 1, (0, 0, 255), 1)
	# 	frame=cv2.resize(frame,(960,652))
	# 	cv2.imshow('image', frame)
	# 	k = cv2.waitKey(20)
	# 	#q键退出
	# 	if (k & 0xff == ord('q')):
	# 		break
	# cap.release()
	# cv2.destroyAllWindows()
