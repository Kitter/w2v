# coding:utf-8


import os
import sys
import logging

import re
import zenhan
import multiprocessing

from tqdm import tqdm
from gensim.models import word2vec
from utils import Tokenizer

# logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# load sysdic, usrdic path
sys_dic = os.environ["SYSDIC"]
usr_dic = os.environ["USRDIC"]

print sys_dic
print usr_dic


# load tokenizer
tokenizer = Tokenizer(
    sys_dic=sys_dic,
    usr_dic=usr_dic
)

def build_corpus(target, corpus=None, raw=False):

    targetfp = open(target, "rb")
    corpusfp = open(corpus, "wb")

    for line in tqdm(targetfp):

        # hankaku kana to zenkaku kana
        line = zenhan.h2z(line.decode("utf-8"), mode=4)

        # tokenize and normalize verb
        line = tokenizer.wakati(line, normalize_verb=True)

        corpusfp.write(line+"\n")

    targetfp.close()
    corpusfp.close()


def build_word2vec(corpus, model):

    corpus = word2vec.Text8Corpus(corpus)
    w2v = word2vec.Word2Vec(corpus, workers=multiprocessing.cpu_count())
    w2v.save(model)
