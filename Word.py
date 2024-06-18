# TODO: make the word class with all the following features/methods
class Word:

    # constructor (string parameter representing a singular word)
    def __init__(self, w):
        self.word = w
        self.capitalized = False
    
    # overall translate method
    def translate_word(self):
        if self.numbers_and_special_characters():
            return self.word
        if self.isCapitalized():
            self.word = self.word[:1].tolower() + self.word[1:]
            self.capitalized = True
        if self.vowel_or_consonant(self.word) is True:
             return self.vowel_translate()
        else:
            return self.consonant_translate()
            
    # determines if the word starts with a vowel or a consonant
    def vowel_or_consonant(w):
        vowels = ["a", "e", "i", "o", "u"]
        firstLetter = w[:1]
        print(firstLetter)
        for v in vowels:
            if firstLetter == v:
                return True # returns true if the letter is a vowel
        return False # returns false if the letter is a consonant
    
    # check for consonant chunks
    def consonant_chunks(self):
        num = 1
        temp = self.word[num:]
        while (True):
            # FINISH THIS IF STATEMENT
            if self.vowel_or_consonant(temp) is True:
                break
            num += 1
            temp = self.word[num:]
        return num
    
    # translates the words starting with consonant(s)
    def consonant_translate(self):
        num = self.consonant_chunks(self)
        translated_word = ""
        if self.capitalized:
            self.word = self.word[:1].lower() + self.word[1:]
            temp = self.word[num:]
            translated_word = temp[:1].upper() + temp[1:] + self.word[:num] + "ay"
            return translated_word
        translated_word = self.word[num:] + self.word[:num] + "ay"
        return translated_word
    
    # translates the words starting with vowel(s)
    def vowel_translate(self):
        translated_word = self.word + "yay"
        return translated_word
    
    # checks for punctuation
    def punctuation_check(self):
        # only checks at the end of the word
        punctuation = [".", ",", ":", ";", "!", "?"]
        lastLetter = self.word[-1]
        for p in punctuation:
            if lastLetter == p:
                return True
        return False
    
    # checks for numbers/special characters
    def numbers_and_special_characters(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        s_chars = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", 
                   "_", "+", "=", "/", "<", ">", "~", "[", "]", "{", "}"]
        
        for w in self.word:
            for n in numbers:
                if w == n:
                    return True
                
            for s in s_chars:
                if w == s:
                    return True
        return False
                
        
    # isCapitalized to check if the first letter of the word is capitalized
    def isCapitalized(self):
        firstLetter = self.word[:1]
        if firstLetter.isupper():
            return True
        return False