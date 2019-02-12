# -*- coding: utf-8 -*-

import re
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


# Паттерны для слов русского и английского языка.
pattern_rus = r"^\W*((?:[а-яё]+[-]{1})*[а-яё]+)\W*$"
pattern_eng = r"^[\W^@]*((?:[a-z]*[-]{1})*[a-z]+)\W*$"


def word_normalization(word):
    """ Возвращает нормальную форму слова. """    
    word = word.lower().strip()
    
    # Обработка слов русского языка.
    word_reg = re.findall(pattern_rus, word)
    
    if word_reg != []:
        word = word_reg[0]
        # word_tag = morph.parse(word)[0].tag
        # surname = 0        
        normal_word = morph.parse(word)[0].normal_form
        return normal_word
    
     # Обработка слов английского языка.
    word_reg = re.findall(pattern_eng, word)
    
    if word_reg != []:
        word = word_reg[0]
        normal_word = morph.parse(word)[0].normal_form
        return normal_word
        
    return ''


def word_tokenization(word):
    """ Возвращает слово (без знаков препинания). """    
    word = word.lower().strip()
    
    # Обработка слов русского языка.
    word_reg = re.findall(pattern_rus, word)    
    if word_reg != []:
        return word_reg[0]
    
     # Обработка слов английского языка.
    word_reg = re.findall(pattern_eng, word)    
    if word_reg != []:
        return word_reg[0]
        
    return ''


class Text:
    """ Класс для хранения и обработки текста. """
    
    # Паттерн для извлечения URL из текста.
    url_pattern = r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?"
    
    # Знаки препинания.
    punctuations = "!\"'(),.:;?[]"
    
    def __init__(self, text):
        self._init_text = text
        self._words = text.split()

    @property
    def text(self):
        return " ".join(self._words)
    
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return str(self)
    
    def lower_text(self):
        """ Перевести текст в нижний регистр. """
        self._words = list(map(lambda x: x.lower(), self._words))
    
    # TODO проблема с пересылаемыми письмами
    def delete_signature(self):
        """ Удалить подпись к письму. """
        self.lower_text()  
        
        # TODO удалить
        if "from" in self.text:
            self._words = []
            return
        
        index = self.text.rfind("с уважением")
        if index != -1:
            mail_text = self.text[:index].rstrip()
            self._words = mail_text.split()
    
    def delete_url(self):
        """ Удалить URL. """
        text = re.sub(Text.url_pattern, "", self.text)
        self._words = text.split()
    
    def not_particle(self):
        """ 
        Обработать частицу "не": Не очень хорошо = "не_очень" "не_хорошо"
        """    
        if "не" in self._words:
            new_words = []
            words = self._words
            
            not_flag = False
            for word in words:
                if word == "не":
                    not_flag = True
                    continue
                
                tag = morph.parse(word)[0].tag
                
                if not_flag:
                    word = "не_{0}".format(word)
                
                if tag.POS not in {"ADVB"}:
                    not_flag = False
                
                new_words.append(word)
            
            self._words = new_words
    
    def add_whitespace(self):
        """ 
        Вставить пропущенные пробелы после знаков препинания 
        (например, "уточните,пожалуйста").
        """
        text = re.sub(r"([{0}]+)".format(re.escape(Text.punctuations)), 
                      r"\1 ", self.text)
        self._words = text.split()
    
    def tokenize(self):
        """ Токенизировать текст. """
        words = [word_tokenization(word) for word in self._words]
        self._words = [word for word in words if word != ""]

    def normalize(self):
        """ Нормализовать текст. """
        words = [word_normalization(word) for word in self._words]
        self._words = [word for word in words if word != ""]
    
    def delete_stop_words(self, stop_words):
        """ Удалить стоп-слова. """
        self._words = stop_words.delete_stop_words_from_list(self._words)


class StopWord:
    
    def __init__(self, word):       
        self._word_list = word.split()
        self._count = len(self._word_list)
        
    def __hash__(self):
        return hash(str(self))
            
    def __str__(self):
        return " ".join(self._word_list)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if type(other) is StopWord:
            return self._word_list == other._word_list
        elif type(other) is str:
            return str(self) == other
    
    @property
    def word(self):
        return str(self)
        
    @property
    def count(self):
        return self._count
    
    def delete_from_list(self, words):
        """ Удалить стоп-слово из списка слов. """
        text = " ".join(words)
        text = self.delete_from_string(text)
        return text.split()
    
    def delete_from_string(self, string):
        """ Удалить стоп-слово из строки. """
        new_string = re.sub("( |^){0}( |$)".format(str(self)), " ", string).strip()
        while new_string != string:
            string = new_string
            new_string = re.sub("( |^){0}( |$)".format(str(self)), " ", string).strip()
        return new_string


class StopWords:
    """ Класс для хранения списка стоп-слов. """
    
    def __init__(self, filepath):
        stop_words = set()
        with open(filepath, 'r', encoding="utf-8") as file:
            for word in file:
                word = StopWord(word.strip())
                stop_words.add(word)
        
        stop_words = sorted(stop_words, key=lambda x: x.count, reverse=True)
        self.stop_words = stop_words
       
    def delete_stop_words(self, text):
        """ Удалить стоп-слова. """
        return self.delete_stop_words_from_string(text)
    
    def delete_stop_words_from_string(self, string):
        """ Удалить стоп-слова из строки. """
        for word in self.stop_words:
            string = word.delete_from_string(string)
        return string.strip()
            
    def delete_stop_words_from_list(self, words):
        """ Удалить стоп-слова из списка слов. """        
        string = " ".join(words)
        string = self.delete_stop_words_from_string(string)
        return string.split()
    