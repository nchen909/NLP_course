# coding=utf-8
import pandas as pd
from gensim.models import FastText


def my_function():
    model = FastText.load('fasttext.model')
    print(model.similarity('西红柿', '番茄'))  # 相似度为0.823041730247136
    print(model.similarity('西红柿', '香蕉'))  # 相似度为0.8448946916339098
    # print(model.similarity('人工智能','大数据'))
    # print(model.similarity('滴滴', '共享单车'))

    result = pd.Series(model.most_similar(u'阿里巴巴'))  # 查找近义相关词
    print(result)
    result1 = pd.Series(model.most_similar(u'故宫'))
    print(result1)
    print(model.wv['中国'])  # 查看中国的词向量（单个词语的词向量）


if __name__ == '__main__':
    my_function()