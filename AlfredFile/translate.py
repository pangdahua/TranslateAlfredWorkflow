#-*- coding:utf-8

class TranslateDelegate():
    def __init__(self, translator):
        self.translator = translator

    def translate(self, word):
        return self.translator.translate(word)
