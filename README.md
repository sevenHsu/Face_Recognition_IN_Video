# Face_Recognition_IN_Video

## About
This is a desktop programe for finding and marking the faces required in videos.
## Requirement
- python36

  I use python36 in this programe for using pytorch.
- Pytorch 

  Only Pytorch.02+ can work in this programe.If you want using GPU to make it run faster,please download and install Cuda.
- Mxnet
  
  I use Mtcnn for detecting face from videos which need Mxnet.
## Using

run:
  --python main.py-
  
## README_MTCNN_face_detection_and_alignment

# MTCNN_face_detection_and_alignment

## About

  This is a python/mxnet implementation of [Zhang](https://kpzhang93.github.io/)'s work **<Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Neural Networks>**. it's fast and accurate,  see [link](https://github.com/kpzhang93/MTCNN_face_detection_alignment). 

  It should have **almost** the same output with the original work,  for mxnet fans and those can't afford matlab :)

[中文blog](https://pangyupo.github.io/2016/10/22/mxnet-mtcnn/)

## Requirement	  

- opencv 

  ​	I use cv2 for image io and resize(much faster than skimage), the input image's channel is acutally BGR

- mxnet 

  ​	**please update to the newest version, we need 'full' mode in Pooling operation**

Only tested on Linux and Mac

## Test

run:

 ``python main.py`` 

you can change `ctx` to `mx.gpu(0)` for faster detection

--- update 20161028 ---

by setting ``num_worker=4``  ``accurate_landmark=False`` we can reduce the detection time by 1/4-1/3, the bboxes are still the same, but we skip the last landmark fine-tune stage( mtcnn_v1 ). 

--- update 20161207 ---

add function `extract_face_chips`, examples:

![1](http://7vikw0.com1.z0.glb.clouddn.com/chip_0.png)
![2](http://7vikw0.com1.z0.glb.clouddn.com/chip_3.png)
![3](http://7vikw0.com1.z0.glb.clouddn.com/chip_2.png)
![4](http://7vikw0.com1.z0.glb.clouddn.com/chip_1.png)

see `mtcnn_detector.py` for the details about the parameters. this function use [dlib](http://dlib.net/)'s align strategy, which works well on profile images :) 
## Results

![big4](http://7xsc78.com1.z0.glb.clouddn.com/face_mtcnn.png)



## License

MIT LICENSE



## Reference

K. Zhang and Z. Zhang and Z. Li and Y. Qiao Joint,  Face Detection and Alignment Using Multitask Cascaded Convolutional Networks, IEEE Signal Processing Letters

## README_SphereFace

# SphereFace
A PyTorch Implementation of SphereFace.
The code can be trained on CASIA-Webface and the best accuracy on LFW is **99.22%**.

[SphereFace: Deep Hypersphere Embedding for Face Recognition](https://arxiv.org/abs/1704.08063)

# Train
```
python train.py
```

# Test
```
# lfw.tgz to lfw.zip
tar zxf lfw.tgz; cd lfw; zip -r ../lfw.zip *; cd ..

# lfw evaluation
python lfw_eval.py --model model/sphere20a_20171020.pth
```

# Pre-trained models
| Model name      | LFW accuracy | Training dataset |
|-----------------|--------------|------------------|
| [20171020](model/sphere20a_20171020.7z) | 0.9922 | CASIA-WebFace |

# φ
![equation](https://latex.codecogs.com/gif.latex?phi%28x%29%3D%5Cleft%28-1%5Cright%29%5Ek%5Ccdot%20%5Ccos%20%5Cleft%28x%5Cright%29-2%5Ccdot%20k)

![equation](https://latex.codecogs.com/gif.latex?myphi(x)=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\frac{x^8}{8!}-\frac{x^9}{9!})

![phi](images/phi.png)

# References
[sphereface](https://github.com/wy1iu/sphereface)
## Reference

Mtcnn for face detection:https://github.com/pangyupo/mxnet_mtcnn_face_detection

Sphereface_pytorch for face recognition:https://github.com/clcarwin/sphereface_pytorch
