# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainJHMZfX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 562)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_show_frame = QFrame(self.centralwidget)
        self.drop_show_frame.setObjectName(u"drop_show_frame")
        self.drop_show_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 44, 111, 255), stop:0.5 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_show_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_show_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.drop_show_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_show_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Roboto Thin")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet(u"color: rgb(60,231, 195);")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.frame_title)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{	\n"
"	background-color: rgb(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout_2.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_show_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_bar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_infos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_circle_1 = QFrame(self.frame_infos)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(250, 250))
        self.frame_circle_1.setMaximumSize(QSize(250, 250))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 50, 10, 50)
        self.label_2 = QLabel(self.frame_circle_1)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame_circle_1)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(8)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: rgb(128, 102, 168);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_circle_1)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"Roboto Thin")
        font4.setPointSize(60)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: rgb(220, 220, 220);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_circle_1)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamily(u"Roboto")
        font5.setPointSize(10)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_4.addWidget(self.frame_circle_1)

        self.frame_circle_2 = QFrame(self.frame_infos)
        self.frame_circle_2.setObjectName(u"frame_circle_2")
        self.frame_circle_2.setMinimumSize(QSize(250, 250))
        self.frame_circle_2.setMaximumSize(QSize(250, 250))
        self.frame_circle_2.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"")
        self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 50, 10, 50)
        self.label_6 = QLabel(self.frame_circle_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_circle_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"border: none;\n"
"color: rgb(220, 220, 220);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_circle_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"border: none;\n"
"color: rgb(128, 102, 168);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_circle_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.frame_circle_2)

        self.frame_circle_3 = QFrame(self.frame_infos)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(250, 250))
        self.frame_circle_3.setMaximumSize(QSize(250, 250))
        self.frame_circle_3.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 50, 10, 50)
        self.label_10 = QLabel(self.frame_circle_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_circle_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"border: none;\n"
"color: rgb(220, 220, 220);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_circle_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"border: none;\n"
"color: rgb(128, 102, 168);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_circle_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_13)


        self.horizontalLayout_4.addWidget(self.frame_circle_3)


        self.verticalLayout_11.addWidget(self.frame_infos)

        self.frame = QFrame(self.frame_content_home)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(600, 0))
        self.label_14.setMaximumSize(QSize(600, 50))
        font6 = QFont()
        font6.setFamily(u"Roboto Light")
        font6.setPointSize(14)
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(33, 33, 75);\n"
"border-radius: 10px;\n"
"")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.verticalLayout_7 = QVBoxLayout(self.page_credits)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_content_credits)

        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_show_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 50))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setStyleSheet(u"padding: 8px;")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamily(u"Roboto Thin")
        self.label_credits.setFont(font7)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")
        self.label_credits.setFrameShape(QFrame.Panel)

        self.verticalLayout_4.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout_2.addWidget(self.credits_bar)


        self.verticalLayout.addWidget(self.drop_show_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This is My App - Title Bar", None))
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPU USAGE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Intel | i9 9900k | 8 Core", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temp: 45C\u00b0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"GPU USAGE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"40%", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RTX 3070 Ti", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Temp: 55C\u00b0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"RAM USAGE", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total 64gb", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Temp: 25C\u00b0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\"If you control the code, you control the world.\"", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By Mayaring", None))
    # retranslateUi

