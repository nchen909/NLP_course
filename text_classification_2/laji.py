#coding=utf-8
import numpy as np
import time
import random
import re
import warnings

import jieba
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding, Dropout, Conv1D, MaxPooling1D, Bidirectional, Activation

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
warnings.filterwarnings("ignore")
def process_line(line):
    tmp = [int(val) for val in line.strip().split(',')]
    x = np.array(tmp[:-1])
    y = np.array(tmp[-1:])
    return x, y


def generate_arrays_from_file(path, batch_size):
    print(11111111)
    while 1:
        f = open(path,'r',encoding='utf-8')
        print(111111111111111)
        cnt = 0
        X = []
        Y = []
        for line in f:
            # create Numpy arrays of input data
            # and labels, from each line in the file
            x, y = process_line(line)
            X.append(x)
            Y.append(y)
            cnt += 1
            if cnt == batch_size:
                cnt = 0
                yield (np.array(X), np.array(Y))
                X = []
                Y = []
        f.close()

if __name__ == '__main__':
    generate_arrays_from_file('./laji.txt',2)


    model = Sequential()
    #model.add(LSTM(input_dim=50, output_dim=50, return_sequences=True))
    model.add(LSTM(input_dim=50, units=50, return_sequences=True))#会记录之前信息
    model.add(Dropout(0.2))#防过拟合提高泛化能力 卷积之后一般不用因为参数少会过拟合，
    #全连接之后dropout好一点 断掉一些链接 而不是直接断维度
    model.add(LSTM(30, return_sequences=False))
    model.add(Dropout(0.2))#不过拟合不加dropout 欠拟合降dropout
    #dropout的直接作用是减少中间特征的数量，从而减少冗余，即增加每层各个特征之间的正交性
    # （数据表征的稀疏性观点也恰好支持此解释）。
    #以概率p对该层神经元进行保留 将输入X转为X/P来训练
    model.add(Dense(units=20))
    model.add(Activation("sigmoid"))
    model.compile(optimizer='sgd', loss='binary_crossentropy')

    model.fit_generator(generate_arrays_from_file('./laji.txt', batch_size=2),
                        steps_per_epoch=2,
                        verbose=1)
