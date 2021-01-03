# coding=utf-8
import gensim
import pandas as pd


def my_function():
    model = gensim.models.Word2Vec.load(r'C:\Users\chenn\experiment\deepshare\NLP\1word2vecfasttext\code\zhiwiki_news.word2vec')
    print(model.similarity('西红柿', '番茄'))  # 相似度为0.7386878903088806
    print(model.similarity('西红柿', '香蕉'))  # 相似度为0.6641281040708612
    # print(model.similarity('人工智能','大数据'))
    # print(model.similarity('滴滴', '共享单车'))

    result = pd.Series(model.most_similar(u'阿里巴巴'))  # 查找近义相关词
    print(result)
    result1 = pd.Series(model.most_similar(u'故宫'))
    print(result1)
    for key in model.wv.similar_by_word('贪污', topn=10):
        print(key)
    print(model.wv['中国'])  # 查看中国的词向量（单个词语的词向量）


if __name__ == '__main__':
    my_function()