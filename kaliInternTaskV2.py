# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaliInternTaskV2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# class import
from Sentence import Sentence

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 594)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 170, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textbox = QTextEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setGeometry(QRect(20, 130, 330, 350))
        self.textbox.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.unchanged_text = QTextEdit(self.centralwidget)
        self.unchanged_text.setObjectName(u"unchanged_text")
        self.unchanged_text.setGeometry(QRect(450, 130, 330, 350))
        self.unchanged_text.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.unchanged_text.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 60, 240, 30))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(30, 500, 110, 40))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.button.setFont(font1)
        self.button.setStyleSheet(u"QPushButton {\n"
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
        self.button.setCheckable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.textbox.textChanged.connect(self.set_invisible)
        # self.button.pressed.connect(self.set_visible)
        self.button.pressed.connect(self.translate)

        QMetaObject.connectSlotsByName(MainWindow)

    # def set_visible(self):
    #     # when the button is pushed, the text will become visible
    #     self.unchanged_text.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def set_invisible(self):
        # when the text is changed by the user, the translation becomes invisible again
        # self.unchanged_text.setEchoMode(QLineEdit.EchoMode.NoEcho)
        self.unchanged_text.setText("")

    def translate(self):
        # when the button is pushed, the text in the left textbox will be translated and be set as the text in the right textbox
        text_to_translate = self.textbox.toPlainText()
        sentence = Sentence(text_to_translate)
        translated_sentence = sentence.translate_sentence()
        self.unchanged_text.setText(translated_sentence)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text to be translated", None))
        self.unchanged_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your translation will be displayed here", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pig Latin Translator", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from kaliInternTaskV2 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
