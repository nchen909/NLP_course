from gensim.models import FastText
# sentences = [["你", "是", "谁"], ["我", "是", "中国人"]]

sentences=[]
f = open('reduce_zhiwiki.txt', 'r',encoding='utf-8')
result = list()
for line in f.readlines():
    line = line.strip()
    line=line.split(' ')
    sentences.append(line)
    # print(line)
#model = FastText(sentences,  size=10, window=3, min_count=1, iter=20,min_n = 3 , max_n = 6,word_ngrams = 0)
#model = FastText(sentences,  size=200, window=12, min_count=3, iter=20,min_n = 5 , max_n = 10,word_ngrams = 1)
model = FastText(sentences,  size=310, window=32, min_count=1, sg=1, hs=1,iter=10, min_n=3, max_n=12, word_ngrams=1)
#model = FastText(sentences)
# print(model['你'])  # 词向量获得的方式
# print(model.wv['你']) # 词向量获得的方式
model.save('fasttext.model')
model.wv.save_word2vec_format('fasttext_wordembedding.txt', binary=False)
