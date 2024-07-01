class Word:

    # constructor (string parameter representing a singular word)
    def __init__(self, w):
        self.word = w  
        self.capitalized = False   
    
    # overall translate method
    def translate_word(self):
        if (self.numbers_and_special_characters()):
            # if a word contains a number or special character, the "word" will not be translated and will appear as is in the translation
            return self.word
        if self.isCapitalized():
            # will make the word lowercase and set the capitalized variable to true
            self.word = self.word[:1].lower() + self.word[1:]
            self.capitalized = True
        if (self.vowel_or_consonant(self.word)):
            # will translate the word that starts with a vowel
            return self.vowel_translate()
        else:
            # will translate the work that starts with a consonant
            return self.consonant_translate()
            
    # determines if the word starts with a vowel or a consonant
    def vowel_or_consonant(self, w):
        vowels = ["a", "e", "i", "o", "u"]  
        firstLetter = w[:1]   
        # iterates through the list of vowels and checks if the word starts with a vowel or not
        for v in vowels:
            if firstLetter == v:
                return True # returns true if the letter is a vowel
        return False # returns false if the letter is a consonant
    
    # check for consonant chunks
    def consonant_chunks(self):
        num = 1   
        temp = self.word[num:]   
        b = True   
        while (b):
            # checks if the next letter of the consonant word is a vowel or consonant
            if self.vowel_or_consonant(temp) is True:   # runs if the next letter of the word is a vowel
                b = False   
                break   
            # the letter "y" will count as a vowel if it isn't the first letter of the word, and it isn't accounted for in the vowel or consonant function
            elif temp[:1] == "y":   
                b = False 
                break
            num += 1   
            temp = self.word[num:]   
        return num   
    
    # translates the words starting with consonant(s)
    def consonant_translate(self):
        num = self.consonant_chunks()
        translated_word = ""
        punctuation = ""
        p = self.punctuation_check() - 1
        # accounts for punctuation and moves it (if any) to the back of the word
        if p >= 1:
            punctuation = self.word[-(p):]
            self.word = self.word[:-(p)]
        # capitalizes the first letter of the stranslated word because the word was originally capitalized
        if self.capitalized:
            temp = self.word[num:]
            translated_word = temp[:1].upper() + temp[1:] + self.word[:num] + "ay" + punctuation
            return translated_word
        # runs if the word wasn't capitalized and translated the word accordingly
        translated_word = self.word[num:] + self.word[:num] + "ay" + punctuation
        return translated_word
    
    # translates the words starting with vowel(s)
    def vowel_translate(self):
        translated_word = ""
        punctuation = ""
        num = self.punctuation_check() - 1
        # accounts for punctuation and moves it (if any) to the back of the word
        if num >= 1:
            punctuation = self.word[-(num):]
            self.word = self.word[:-(num)]
        # capitalizes the first letter of the stranslated word because the word was originally capitalized
        if self.capitalized:
            translated_word = self.word[:1].upper() + self.word[1:] + "yay" + punctuation
            return translated_word
        # runs if the word wasn't capitalized and translated the word accordingly
        translated_word = self.word + "yay" + punctuation
        return translated_word
    
    # checks for punctuation
    def punctuation_check(self):
        # only checks at the end of the word
        punctuation = [".", ",", ":", ";", "!", "?"]
        num = 1   # number of punctuation characters
        # will run until a punctuation character isn't detected
        while num <= len(self.word):
            if self.word[-num] in punctuation:
                num += 1
            else:
                break
        return num   # returns the number of punctuation characters detected at the end of the word
                    
    
    # checks for numbers/special characters
    def numbers_and_special_characters(self):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        s_chars = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", 
                   "_", "+", "=", "/", "<", ">", "~", "[", "]", "{", "}"]
        # iterates through the entire word looking for an instance of either a number of special character
        for w in self.word:
            if w in numbers or w in s_chars:
                return True
        return False
                
        
    # isCapitalized to check if the first letter of the word is capitalized
    def isCapitalized(self):
        firstLetter = self.word[:1]   # only checks the first letter
        if firstLetter.isupper():
            return True
        return False