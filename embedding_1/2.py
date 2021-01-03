# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    wiki_news = open('reduce_zhiwiki.txt', 'r',encoding='utf-8')
    #LineSentence加载语料 Word2Vec训练语料
    model = Word2Vec(LineSentence(wiki_news), sg=0,size=800, window=12, min_count=3, workers=8)
    #model = Word2Vec(LineSentence(wiki_news))
    model.save('zhiwiki_news.word2vec')
    model.wv.save_word2vec_format('word2vec_format.txt')

if __name__ == '__main__':
    my_function()
