# 1embedding方法

词相似度任务 词类比任务

用的是写好现成的py做测试

# 2新闻分类模型  可延伸阅读BiLSTM+CRF

两层单向或双向LSTM+MLP（全连接）组分类

word2vec+Fasttext+normal LSTM（可尝试用腾讯）

[腾讯的/NeuralNLP-NeuralClassifier: An Open-source Neural Hierarchical Multi-label Text Classification Toolkit](https://github.com/Tencent/NeuralNLP-NeuralClassifier)

# 3依存分析

LTP（pyLTP）进行句法分析

 NLTK和StandfordNLP

pyhanlp

用的是一堆直接调用的model做测试

# 4命名实体识别

Chinese NER Using Lattice LSTM

TENER（Adapting Transformer Encoder for Named Entity）

# 5seq2seq encoder decoder_keras

*博客*[https://blog.csdn.net/PIPIXIU/article/details/81016974#2-%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BF%BB%E8%AF%91%E5%AE%9E%E6%88%98](https://blog.csdn.net/PIPIXIU/article/details/81016974#2-中英文翻译实战)

*建议阅读*[**https://github.com/facebookresearch/fairseq**](https://github.com/facebookresearch/fairseq)

# 6实现自动问答功能 KB-QA-master

https://github.com/DouYishun/KB-QA

小的能跑通

https://github.com/zhihao-chen/QASystemOnMedicalGraph

大的 很慢 有兴趣可以跑

大的流程：爬取数据-》清洗-》构建知识图谱-》自动问答-》实体识别