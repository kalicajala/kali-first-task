# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaliInternTaskV3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Sentence import Sentence

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
        self.textbox = QTextEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setGeometry(QRect(20, 110, 330, 350))
        self.textbox.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.unchanged_text = QTextEdit(self.centralwidget)
        self.unchanged_text.setObjectName(u"unchanged_text")
        self.unchanged_text.setGeometry(QRect(450, 110, 330, 350))
        self.unchanged_text.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.unchanged_text.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 240, 30))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(330, 480, 141, 41))
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
        self.sadPigButton = QPushButton(self.centralwidget)
        self.sadPigButton.setObjectName(u"sadPigButton")
        self.sadPigButton.setGeometry(QRect(100, 480, 141, 81))
        icon = QIcon()
        icon.addFile(u"sad.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sadPigButton.setIcon(icon)
        self.sadPigButton.setIconSize(QSize(140, 140))
        self.happyPigButton = QPushButton(self.centralwidget)
        self.happyPigButton.setObjectName(u"happyPigButton")
        self.happyPigButton.setGeometry(QRect(580, 470, 91, 100))
        icon1 = QIcon()
        icon1.addFile(u"download.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.happyPigButton.setIcon(icon1)
        self.happyPigButton.setIconSize(QSize(100, 100))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.textbox.textChanged.connect(self.set_invisible)   # when the text is changed, the translation is not visible anymore
        self.button.pressed.connect(self.translate)   # when the button is pressed, the words are translated and displayed in the right textbox
        self.textbox.textChanged.connect(self.sadPigButton.show)   # the sad Peppa Pig appears when the original text is changed
        self.button.pressed.connect(self.sadPigButton.hide)   # when the translate button is pressed, the sad Peppa Pig disappears
        self.textbox.textChanged.connect(self.happyPigButton.hide)   # the happy Peppa Pig disappears when the original text is changed
        self.button.pressed.connect(self.happyPigButton.show)   # the happy Peppa Pig appears when the translate button is pressed

        QMetaObject.connectSlotsByName(MainWindow)

    def set_invisible(self):
        # when the text is changed by the user, the translation won't be visible and the placeholder text is displayed again
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
        self.sadPigButton.setText("")
        self.happyPigButton.setText("")
    # retranslateUi

# this allows the application to run and open the Main Window
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from kaliInternTaskV3 import Ui_MainWindow

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
