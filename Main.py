#conding = utf-8
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import MainWindow
from MainWindow import Ui_MainWindow
import cv2
from PyQt5.QtGui import QPixmap
import myApi
import ctypes
import inspect
import os


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()
        '''palette1 = QtGui.QPalette(self)
        palette1.setColor(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("./img/backimg/background1.jpg")))
        self.setPalette(palette1)'''
        self.le = QLineEdit()
        self.le.setText("Empty")
        self.vedio1_Button.clicked.connect(self.vedio1)
        self.vedio2_Button_2.clicked.connect(self.vedio2)
        self.vedio3_Button_3.clicked.connect(self.vedio3)
        self.search_Button.clicked.connect(self.searchtest)
        self.intro_Button_4.clicked.connect(self.intro4)
        self.image = QImage()
        self.api=myApi.MyApi()
        self.api.start()
        self.closeimg=False
        self.names = []

    def initUI(self):       #导入显示人脸头像在右侧
        pixMap = QPixmap("./img/zhangwei.jpg").scaled(self.label_1.width(), self.label_1.height())
        self.label_1.setPixmap(pixMap)
        pixMap = QPixmap("./img/huyifei.jpg").scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(pixMap)
        pixMap = QPixmap("./img/guangu.jpg").scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(pixMap)
        pixMap = QPixmap("./img/baizhantang.jpg").scaled(self.label_4.width(), self.label_4.height())
        self.label_4.setPixmap(pixMap)
        pixMap = QPixmap("./img/tongxiangyu.jpg").scaled(self.label_5.width(), self.label_5.height())
        self.label_5.setPixmap(pixMap)
        pixMap = QPixmap("./img/lidazui.jpg").scaled(self.label_6.width(), self.label_6.height())
        self.label_6.setPixmap(pixMap)
        pixMap = QPixmap("./img/lvxiucai.jpg").scaled(self.label_7.width(), self.label_7.height())
        self.label_7.setPixmap(pixMap)
        pixMap = QPixmap("./img/luosi.jpg").scaled(self.label_8.width(), self.label_8.height())
        self.label_8.setPixmap(pixMap)
        pixMap = QPixmap("./img/qiaoyi.jpg").scaled(self.label_9.width(), self.label_9.height())
        self.label_9.setPixmap(pixMap)
        pixMap = QPixmap("./img/ruiqiu.jpg").scaled(self.label_10.width(), self.label_10.height())
        self.label_10.setPixmap(pixMap)
##重写关闭窗口函数
    def closeEvent(self,event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if self.api.is_alive():
                self.stop_thread(self.api)
            os.exit(0)
            #event.accept()
        else:
            event.ignore()
##关闭线程的部分
    def _async_raise(self,tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self,thread):
        """关闭线程,参数是线程的名字"""
        self._async_raise(thread.ident, SystemExit)

    def showimg(self,filname):
        self.textEdit.setHidden(True)   #隐藏开始的介绍文字
        self.label_vedio.setHidden(False)
        capture = cv2.VideoCapture(filname)
        self.closeimg=True
        # fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
        while capture.isOpened() and self.closeimg:
            ret, frame = capture.read()
            if frame is None:
                break
            if len(self.names) != 0:
                frame = cv2.resize(frame, (300, 204))
                frame = self.api.markFace(frame, self.names)
                frame = cv2.resize(frame, (960, 652))
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)  # 转换RGB
            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            self.image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)  # 生成图片
            pixmap = QPixmap.fromImage((self.image))  # 将图片加载到pixmap
            self.label_vedio.setPixmap(
                pixmap.scaled(self.label_vedio.width(), self.label_vedio.height()))  # 通过scaled函数把视频图片变换成label标签的大小
            QApplication.processEvents()  # 刷新窗口
            if len(self.names) == 0:
                time.sleep(0.06)
        if self.api.is_alive():
            self.stop_thread(self.api)

    def vedio1(self):
        filename = "./videos/aiqinggongyu480.mp4"
        self.showimg(filename)

    def vedio2(self):
        filename = "./videos/wulinwaizhuan480.mp4"
        self.showimg(filename)

    def vedio3(self):
        filename = "./videos/laoyouji720.mp4"
        self.showimg(filename)

    def intro4(self):
        self.closeimg=False
        QApplication.processEvents()
        self.label_vedio.setHidden(True)
        self.textEdit.setHidden(False)

    def searchtest(self):
        name = ['zhangwei','huyifei','guangu','baizhantang','tongxiangyu','lidazui','lvxiucai','luosi','qiaoyi','ruiqiu']
        names=[]
        for pipe in range(1,11):
            m = getattr(self, "checkBox_%d"%pipe)   #遍历每个checkBox
            if m.isChecked():                       #如果被选中则在新数组中添加
                names.append(name[pipe-1])
        self.names = names

def openfile(self):
        absolute_path = QFileDialog.getOpenFileName(self, '打开文件','.')
        if absolute_path:
            cur_path = QDir('.')
            relative_path = cur_path.relativeFilePath(absolute_path)
            self.le.setText(relative_path)
            print(relative_path)

        #if fname[0]:
            #with open(fname[0], 'r',encoding ='gb18030',errors = 'ignore') as f:
                #self.tx.setText(f.read())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
