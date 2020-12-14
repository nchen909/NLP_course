#!/usr/bin/env python
# coding=utf-8
import importlib, sys
import re
importlib.reload(sys)
import os
from pyltp import SentenceSplitter, Segmentor, Postagger, NamedEntityRecognizer, Parser, SementicRoleLabeller, \
    CustomizedSegmentor


# 分句
def sentence_split(text):
    sents = SentenceSplitter.split(text)  # 分句
    print('\n'.join(sents))


class LtpModelAnalysis(object):
    def __init__(self, model_dir=r"C:\\Users\\chenn\\experiment\\deepshare\\NLP\\1word2vecfasttext\\code3"):
        self.segmentor = Segmentor()
        self.segmentor.load(os.path.join(model_dir, "cws.model"))  # 加载分词模型
        # 使用自定义词典
        # self.segmentor.load_with_lexicon(os.path.join(model_dir, "cws.model"), 'lexicon')  # 加载分词模型，第二个参数是外部词典文件路径
        # 使用个性化分词模型  #pyltp支持使用用户训练好的个性化模型
        # customized_segmentor = CustomizedSegmentor()  # 初始化实例
        # customized_segmentor.load(os.path.join(model_dir, "cws.model"), 'customized_model')  # 加载模型，第二个参数是增量模型的路径
        # 个性化分词模型的同时也可以使用外部词典
        # customized_segmentor = CustomizedSegmentor()  # 初始化实例
        # customized_segmentor.load_with_lexicon(os.path.join(model_dir, "cws.model"), 'customized_model'，'lexicon')

        self.postagger = Postagger()
        self.postagger.load(os.path.join(model_dir, "pos.model"))  # 加载词性标注模型

        self.recognizer = NamedEntityRecognizer()
        self.recognizer.load(os.path.join(model_dir, "ner.model"))  # 加载命名实体识别模型

        self.parser = Parser()
        self.parser.load(os.path.join(model_dir, "parser.model"))  # 加载依存句法分析模型

        self.labeller = SementicRoleLabeller()
        self.labeller.load(os.path.join(model_dir, "pisrl_win.model"))  # 加载语义角色标注模型

    def analyze(self, text):
        # 分词
        words = self.segmentor.segment(text)
        print('\t'.join(words))

        # 词性标注
        postags = self.postagger.postag(words)
        print('\t'.join(postags))

        # 命名实体识别
        netags = self.recognizer.recognize(words, postags)  # 命名实体识别
        print('\t'.join(netags))

        # 句法分析
        arcs = self.parser.parse(words, postags)
        print("\t".join(
            "%d:%s" % (arc.head, arc.relation) for arc in arcs))  # arc.head 表示依存弧的父节点词的索引，arc.relation 表示依存弧的关系。
        arcs_list = []

        # 语义角色标注

        roles = self.labeller.label(words, postags, arcs)   # arcs 使用依存句法分析的结果
        for role in roles:
            print([role.index,
                   "".join(["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])])
        # roles = self.labeller.label(words, postags, arcs)  # arcs 使用依存句法分析的结果
        # for role in roles:
        #     print(role.index,
        #           "".join(["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))

    def release_model(self):
        # 释放模型
        self.segmentor.release()
        self.postagger.release()
        self.recognizer.release()
        self.parser.release()
        # self.labeller.release()


if __name__ == '__main__':
    content1 = ''
    with open('./content.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            if line != "\n":
                content1=re.sub('######', '', line)
                break
    print(content1)
    contents=re.split(r'。', content1)
    contents_part=contents[0]+contents[1]
    #text = "你觉得我的博客写的怎么样？进一步交流请加QQ群：955817470"
    ltp = LtpModelAnalysis()
    ltp.analyze(contents_part)
    ltp.release_model()
    sentence_split(contents_part)#分句