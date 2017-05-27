# coding:utf-8


import os

from gensim.models import word2vec


model = word2vec.Word2Vec.load(os.environ["WORD2VEC_PATH"])

def simword(target, topn=10):
    for word, score in model.most_similar(target, topn=topn):
        print word, score
