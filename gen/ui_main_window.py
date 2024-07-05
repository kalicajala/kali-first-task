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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 662)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 170, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_images_and_button = QWidget(self.centralwidget)
        self.widget_images_and_button.setObjectName(u"widget_images_and_button")
        self.widget_images_and_button.setMinimumSize(QSize(0, 100))
        self.horizontalLayout = QHBoxLayout(self.widget_images_and_button)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_sad_pig = QWidget(self.widget_images_and_button)
        self.widget_sad_pig.setObjectName(u"widget_sad_pig")
        self.widget_sad_pig.setMinimumSize(QSize(150, 150))
        self.widget_sad_pig.setMaximumSize(QSize(150, 150))
        self.sadPig = QLabel(self.widget_sad_pig)
        self.sadPig.setObjectName(u"sadPig")
        self.sadPig.setGeometry(QRect(0, 0, 150, 150))
        self.sadPig.setMinimumSize(QSize(150, 150))
        self.sadPig.setMaximumSize(QSize(150, 120))
        self.sadPig.setPixmap(QPixmap(u"../assets/peppaPigSad.jpg"))
        self.sadPig.setScaledContents(True)
        self.sadPig.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.widget_sad_pig)

        self.pushButton_translate = QPushButton(self.widget_images_and_button)
        self.pushButton_translate.setObjectName(u"pushButton_translate")
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_translate.setFont(font)
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

        self.horizontalLayout.addWidget(self.pushButton_translate)

        self.widget_happy_pig = QWidget(self.widget_images_and_button)
        self.widget_happy_pig.setObjectName(u"widget_happy_pig")
        self.widget_happy_pig.setMinimumSize(QSize(150, 150))
        self.widget_happy_pig.setMaximumSize(QSize(150, 150))
        self.happyPig = QLabel(self.widget_happy_pig)
        self.happyPig.setObjectName(u"happyPig")
        self.happyPig.setGeometry(QRect(0, 0, 150, 150))
        self.happyPig.setMinimumSize(QSize(150, 150))
        self.happyPig.setMaximumSize(QSize(150, 150))
        self.happyPig.setPixmap(QPixmap(u"../assets/peppaPigHappy.jpg"))
        self.happyPig.setScaledContents(True)
        self.happyPig.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.widget_happy_pig)


        self.gridLayout.addWidget(self.widget_images_and_button, 4, 0, 1, 6)

        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 6)

        self.textEdit_source_english_input = QTextEdit(self.centralwidget)
        self.textEdit_source_english_input.setObjectName(u"textEdit_source_english_input")
        self.textEdit_source_english_input.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")

        self.gridLayout.addWidget(self.textEdit_source_english_input, 1, 1, 1, 1)

        self.textEdit_output = QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.textEdit_output.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_output, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pig Latin Translator", None))
        self.sadPig.setText("")
        self.pushButton_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.happyPig.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Pig Latin Translator", None))
        self.textEdit_source_english_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text to be translated", None))
        self.textEdit_output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your translation will be displayed here", None))
    # retranslateUi

