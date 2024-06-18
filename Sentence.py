# import Word class
import Word

# make a sentence class to translate the user input
class Sentence:
    # constructor with sentence parameter
    def __init__(self, s):
        self.sentence = s

    # destructor
    # translate fucntion
    def translate_sentence(self):
        total_translation = ""
        words_list = self.sentence.split()
        for w in words_list:
            temp = Word.Word(w)
            total_translation += temp.translate_word()
        return total_translation

# def main():
#     test = input("enter a word: ")
#     s = Sentence(test)
#     s.translate_sentence()


# if __name__ == "__main__":
#     main()

test = input("enter a word: ")
s = Sentence(test)
s.translate_sentence()