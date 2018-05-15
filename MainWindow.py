# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("视频人脸查找")
        MainWindow.resize(1171, 785)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        #MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.width(),MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0,0,1171,785))
        self.label_background.setStyleSheet("background-image:url(./img/backing/background11.jpg)")
        self.label_background.setText("")
        self.label_background.setObjectName("label_background")

        self.vedio1_Button = QtWidgets.QPushButton(self.centralwidget)
        self.vedio1_Button.setGeometry(QtCore.QRect(100, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vedio1_Button.setFont(font)
        self.vedio1_Button.setStyleSheet("QPushButton{background:rgba(0,0,0,30);}\n"
"QPushButton:pressed{background:rgba(0,255,0,30);}\n"
"QPushButton:hover{background:rgba(253, 217, 145,60);}")
        self.vedio1_Button.setObjectName("vedio1_Button")
        self.label_aera1 = QtWidgets.QLabel(self.centralwidget)
        self.label_aera1.setGeometry(QtCore.QRect(30, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_aera1.setFont(font)
        self.label_aera1.setObjectName("label_aera1")
        self.label_vedio = QtWidgets.QLabel(self.centralwidget)
        self.label_vedio.setGeometry(QtCore.QRect(30, 80, 831, 591))
        self.label_vedio.setFrameShape(QtWidgets.QFrame.Box)
        self.label_vedio.setLineWidth(2)
        self.label_vedio.setText("")
        self.label_vedio.setObjectName("label_vedio")
        self.label_area2 = QtWidgets.QLabel(self.centralwidget)
        self.label_area2.setGeometry(QtCore.QRect(910, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_area2.setFont(font)
        self.label_area2.setObjectName("label_area2")
        self.search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.search_Button.setGeometry(QtCore.QRect(970, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.search_Button.setFont(font)
        self.search_Button.setStyleSheet("QPushButton{background:rgba(0,0,0,30);}\n"
"QPushButton:pressed{background:rgba(0,255,0,30);}\n"
"QPushButton:hover{background:rgba(253, 217, 145,60);}")
        self.search_Button.setObjectName("search_Button")
        self.vedio2_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.vedio2_Button_2.setGeometry(QtCore.QRect(290,680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vedio2_Button_2.setFont(font)
        self.vedio2_Button_2.setStyleSheet("QPushButton{background:rgba(0,0,0,30);}\n"
"QPushButton:pressed{background:rgba(0,255,0,30);}\n"
"QPushButton:hover{background:rgba(253, 217, 145,60);}")
        self.vedio2_Button_2.setObjectName("vedio2_Button_2")
        self.vedio3_Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.vedio3_Button_3.setGeometry(QtCore.QRect(480, 680, 101, 41))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vedio3_Button_3.setFont(font)
        self.vedio3_Button_3.setStyleSheet("QPushButton{background:rgba(0,0,0,30);}\n"
"QPushButton:pressed{background:rgba(0,255,0,30);}\n"
"QPushButton:hover{background:rgba(253, 217, 145,60);}")
        self.vedio3_Button_3.setObjectName("vedio3_Button_3")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(960, 170, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(1090, 170, 71, 16))
        self.checkBox_2.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(960, 290, 71, 16))
        self.checkBox_3.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(1090, 290, 71, 16))
        self.checkBox_4.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(960, 410, 71, 16))
        self.checkBox_5.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(1090, 410, 71, 16))
        self.checkBox_6.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(960, 530, 71, 16))
        self.checkBox_7.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(1090, 530, 71, 20))
        self.checkBox_8.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_8.setObjectName("checkBox_8")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(913, 80, 101, 81))
        self.label_1.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 80, 101, 81))
        self.label_2.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(910, 200, 101, 81))
        self.label_3.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1040, 200, 101, 81))
        self.label_4.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 320, 101, 81))
        self.label_5.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1040, 320, 101, 81))
        self.label_6.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(910, 440, 101, 81))
        self.label_7.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1040, 440, 101, 81))
        self.label_8.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(910, 560, 101, 81))
        self.label_9.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1040, 560, 101, 81))
        self.label_10.setStyleSheet("\n"
"QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255,170,0);\n"
"    }\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(960, 650, 71, 20))
        self.checkBox_9.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(1090, 650, 71, 20))
        self.checkBox_10.setStyleSheet("color:rgb(255,255,255,0);")
        self.checkBox_10.setObjectName("checkBox_10")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(160, 200, 561, 361)
        self.textEdit.setStyleSheet("border:0xp;background:rgba(0,0,0,0)")
        self.textEdit.setObjectName("textEdit")
        self.intro_Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.intro_Button_4.setGeometry(QtCore.QRect(670, 680,101,41))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.intro_Button_4.setFont(font)
        self.intro_Button_4.setStyleSheet("QPushButton{background:rgba(0,0,0,30);}\n"
                                          "QPushButton:pressed{background:rgba(0,255,0,30);}\n"
                                          "QPushButton:hover{background:rgba(253,217,145,60);}")
        self.intro_Button_4.setObjectName("intro_Button_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "(@1104)视频人脸查找"))
        self.vedio1_Button.setText(_translate("MainWindow", "爱情公寓"))
        self.label_aera1.setText(_translate("MainWindow", "视频播放区域"))
        self.label_area2.setText(_translate("MainWindow", "选择查找的人脸"))
        self.search_Button.setText(_translate("MainWindow", "开始查找"))
        self.vedio2_Button_2.setText(_translate("MainWindow", "武林外传"))
        self.vedio3_Button_3.setText(_translate("MainWindow", "老友记"))
        self.checkBox_1.setText(_translate("MainWindow", "pipe1"))
        self.checkBox_2.setText(_translate("MainWindow", "pipe2"))
        self.checkBox_3.setText(_translate("MainWindow", "pipe3"))
        self.checkBox_4.setText(_translate("MainWindow", "pipe4"))
        self.checkBox_5.setText(_translate("MainWindow", "pipe5"))
        self.checkBox_6.setText(_translate("MainWindow", "pipe6"))
        self.checkBox_7.setText(_translate("MainWindow", "pipe7"))
        self.checkBox_8.setText(_translate("MainWindow", "pipe8"))
        self.checkBox_9.setText(_translate("MainWindow", "pipe9"))
        self.checkBox_10.setText(_translate("MainWindow", "pipe10"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; font-family:楷体; text-indent:0px;\"><span style=\" font-size:18pt;font-family:楷体; font-weight:600;\">操作说明：</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; font-family:楷体; text-indent:0px;\"><span style=\" font-family:楷体;font-size:18pt;\">在【视频播放区域】下方选择所要播放的视频，并在右侧【选择查找的人脸】中勾选所要检测的人脸，点击【开始查找】后会在视频中实时框选相匹配的人脸。</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; font-family:楷体; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">注意事项：</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; font-family:楷体; text-indent:0px;\"><span style=\"font-size:18pt;\">若点击【开始查找】出现卡顿为正常现象，此时系统正在进行初始化处理。</span></p></body></html>"))
        self.intro_Button_4.setText(_translate("MainWindow", "操作说明"))

