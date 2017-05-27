# coding:utf-8


import MeCab


_NODE_KEYS = [
    "surface",  #表層形
    "pos",      #品詞
    "pos1",     #品詞細分類1
    "pos2",     #品詞細分類2
    "pos3",     #品詞細分類3
    "conj",     #活用形
    "conjtype", #活用型
    "base",     #原形
    "read",     #読み
    "pron",     #発音
]


class Tokenizer:

    def __init__(self, sys_dic=None, usr_dic=None):
        mecabopt = ""
        mecabopt += "-d {} ".format(sys_dic) if sys_dic else ""
        mecabopt += "-u {} ".format(usr_dic) if sys_dic else ""
        self._tagger = MeCab.Tagger(mecabopt)
        self._toNode = self._tagger.parseToNode
        self._wakati = MeCab.Tagger(mecabopt+" -Owakati")

    def parse(self, sentence):
        sentence = self.tostr(sentence)

        return self._tagger.parse(sentence)

    def wakati(self, sentence, normalize_verb=False):
        sentence = self.tostr(sentence)

        if normalize_verb is True:
            ret = []
            for node in self.toNode(sentence):
                ret.append(node["base"] if node["pos"]=="動詞" else node["surface"])

            return " ".join(ret)

        else:
            return self._wakati.parse(sentence)

    def toNode(self, sentence):
        sentence = self.tostr(sentence)

        node = self._toNode(sentence)
        while node:
            _node = [node.surface]+node.feature.split(",")
            yield dict(zip(_NODE_KEYS, _node))
            node = node.next

    def tostr(self, sentence):
        if isinstance(sentence, unicode):
            sentence = sentence.encode("utf-8")

        return sentence
