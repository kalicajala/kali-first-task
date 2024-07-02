# import Word class
from source.word import Word

# make a sentence class to translate the user input
class Sentence:
    # constructor with sentence parameter
    def __init__(self, s):
        self.sentence = s

    # translate function
    def translate_sentence(self):
        total_translation = ""
        words_list = self.sentence.split()   # makes a list of the words in the sentence(s) by splitting by every whitespace
        for w in words_list:
            temp = Word(w)   # calls to the Word class
            total_translation += temp.translate_word()   # adds individual word translation to the total translation
            total_translation += " "   # adds a space to separate the words
        return total_translation   # returns the entire translation of the sentence(s)