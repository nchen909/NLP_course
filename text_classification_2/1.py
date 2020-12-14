# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import random
import warnings
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
warnings.filterwarnings("ignore")

def load_data(len1):#随机len1篇文章的词向量及二分类标签
    x_train=[]#20篇100字文章（随机化）
    for i in range(len1):
        x_train_last=[]#100个50维词向量（100个字的doc）
        for j in range(100):
            x_train_one=[]#一个50维词向量
            for j in range(50):
                random.seed(2)
                x=round(random.uniform(0, 1),4)#0.xxxx
                x_train_one.append(x)#[0.xxxx,0.yyyy,...]50维
            x_train_last.append(x_train_one)
        x_train.append(x_train_last)


    y_train = []#20篇文章的标签（随机化）
    for i in range(len1):
        y_train_one=[]
        for j in range(20):
            x = random.randint(0, 1)
            y_train_one.append(x)
        y_train.append(y_train_one)

    x_train = np.array(x_train)#列表转array
    y_train = np.array(y_train)#列表转array
    return x_train,  y_train


if __name__=='__main__':
    start = time.time()

    x_train, y_train=load_data(20)
    print(np.array(x_train).shape)#20,100,50 20篇100个50维词向量
    print(np.array(y_train).shape)#20,20 20篇20个0或1 多分类

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
    model.fit(x_train, y_train, batch_size=512, epochs=10, validation_split=0.2)
    print(model.summary())#可以看到序列模型的每一层

    #进行测试并得到精度
    predicted = model.predict(x_train)
    predicted=predicted.tolist()
    predicted_last=[]
    for i in range(len(predicted)):
        predicted_last+=predicted[i]
    for i in range(len(predicted_last)):
        if predicted_last[i]>0.5:
            predicted_last[i]=1
        else:
            predicted_last[i]=0
    y_train=y_train.tolist()
    y_train_last=[]
    for i in range(len(y_train)):
        y_train_last += y_train[i]

    acc=0
    for i in range(len(y_train_last)):
        if predicted_last[i]==y_train_last[i]:
            acc+=1
    print(acc/len(y_train_last))#215/(20*20)
