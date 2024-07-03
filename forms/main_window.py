# this will be the controller for my main ui
# imports 
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6 import QtGui
from gen.ui_main_window import Ui_MainWindow
from source.sentence import Sentence


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_to_ui()
        self._configure_logos()

    def connect_to_ui(self):
        # Output Textbox
        self.ui.textEdit_source_english_input.textChanged.connect(self.set_invisible)   # when the text is changed, the translation is not visible anymore
        self.ui.pushButton_translate.pressed.connect(self.translate)   # when the button is pressed, the words are translated and displayed in the right textbox

        # Sad Pig Connections
        self.ui.textEdit_source_english_input.textChanged.connect(self.ui.sadPig.show)   # the sad Peppa Pig appears when the original text is changed
        self.ui.pushButton_translate.pressed.connect(self.ui.sadPig.hide)   # when the translate button is pressed, the sad Peppa Pig disappears

        # Happy Pig Connections
        self.ui.textEdit_source_english_input.textChanged.connect(self.ui.happyPig.hide)   # the happy Peppa Pig disappears when the original text is changed
        self.ui.pushButton_translate.pressed.connect(self.ui.happyPig.show)   # the happy Peppa Pig appears when the translate button is pressed

    def set_invisible(self):
        # when the text is changed by the user, the translation won't be visible and the placeholder text is displayed again
        self.ui.textEdit_output.setText("")

    def translate(self):
        # when the button is pushed, the text in the left textbox will be translated and be set as the text in the right textbox
        text_to_translate = self.ui.textEdit_source_english_input.toPlainText()
        sentence = Sentence(text_to_translate)
        translated_sentence = sentence.translate_sentence()
        self.ui.textEdit_output.setText(translated_sentence)

    def _configure_logos(self):
        self.ui.sadPig.setPixmap(QtGui.QPixmap(u"assets/peppaPigSad.jpg"))
        self.ui.happyPig.setPixmap(QtGui.QPixmap(u"assets/peppaPigHappy.jpg"))