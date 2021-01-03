# -*- coding: utf-8 -*-
from gensim.corpora import WikiCorpus
import jieba
from langconv import *

#https://blog.csdn.net/weixin_40547993/article/details/97781179
def my_function():
    space = ' '
    i = 0
    l = []
    zhwiki_name = 'zhwiki-20200820-pages-articles-multistream1.xml-p1p162886.bz2'
    f = open('reduce_zhiwiki.txt', 'w', encoding='utf-8')
    wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  # 从xml文件中读出训练语料
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter('zh-hans').convert(temp_sentence)  # 繁体中文转为简体中文
            seg_list = list(jieba.cut(temp_sentence))  # 分词
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i % 200 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()


if __name__ == '__main__':
    my_function()