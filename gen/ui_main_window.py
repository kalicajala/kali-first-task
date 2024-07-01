# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 594)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 170, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_source_english_input = QTextEdit(self.centralwidget)
        self.textEdit_source_english_input.setObjectName(u"textEdit_source_english_input")
        self.textEdit_source_english_input.setGeometry(QRect(20, 110, 330, 350))
        self.textEdit_source_english_input.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.textEdit_output = QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setGeometry(QRect(450, 110, 330, 350))
        self.textEdit_output.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.textEdit_output.setReadOnly(True)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(280, 40, 240, 30))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)
        self.pushButton_translate = QPushButton(self.centralwidget)
        self.pushButton_translate.setObjectName(u"pushButton_translate")
        self.pushButton_translate.setGeometry(QRect(330, 480, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_translate.setFont(font1)
        self.pushButton_translate.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 85, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(230, 0, 255);\n"
"}")
        self.pushButton_translate.setCheckable(True)
        self.sadPig = QLabel(self.centralwidget)
        self.sadPig.setObjectName(u"sadPig")
        self.sadPig.setGeometry(QRect(100, 480, 141, 81))
        self.sadPig.setPixmap(QPixmap(u"../assets/peppaPigSad.jpg"))
        self.sadPig.setScaledContents(True)
        self.happyPig = QLabel(self.centralwidget)
        self.happyPig.setObjectName(u"happyPig")
        self.happyPig.setGeometry(QRect(580, 470, 100, 100))
        self.happyPig.setPixmap(QPixmap(u"../assets/peppaPigHappy.jpg"))
        self.happyPig.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit_source_english_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text to be translated", None))
        self.textEdit_output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your translation will be displayed here", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Pig Latin Translator", None))
        self.pushButton_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.sadPig.setText("")
        self.happyPig.setText("")
    # retranslateUi

