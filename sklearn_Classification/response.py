# -*- coding:utf-8 -*-

import os
from pdb import Restart
import pickle
import numpy as np
from sklearn import svm


class CLFModel(object):
    def __init__(self, model_save_path):
        super(CLFModel, self).__init__()
        self.model_save_path = model_save_path
        self.id2label = pickle.load(open(os.path.join(self.model_save_path,'id2label.pkl'),'rb'))
        self.vec = pickle.load(open(os.path.join(self.model_save_path,'vec.pkl'),'rb'))
        self.LR_clf = pickle.load(open(os.path.join(self.model_save_path,'LR.pkl'),'rb'))
        self.gbdt_clf = pickle.load(open(os.path.join(self.model_save_path,'gbdt.pkl'),'rb'))

    def predict(self,text):
        text = ' '.join(list(text.lower()))
        text = self.vec.transform([text])
        proba1 = self.LR_clf.predict_proba(text)
        proba2 = self.gbdt_clf.predict_proba(text)
        label = np.argmax((proba1+proba2)/2, axis=1)
        return self.id2label.get(label[0])

__author__ = 'vincy'
from cProfile import label
import random
#闲聊回复模板
gossip_corpus = {
    "greet":[
        "hi",
        "你好呀",
        "我是智能工业设备诊断机器人，有什么可以帮助你吗",
        "hi，你好，你可以叫我小夏",
        "你好，你可以问我一些关于石油钻井泵诊断的问题哦"
    ],
    "goodbye":[
        "再见，很高兴为您服务",
        "bye",
        "再见，感谢使用我的服务",
        "再见啦，欢迎下次再来咨询"
    ],
    "deny":[
        "很抱歉没帮到您",
        "I am sorry",
        "那您可以试着问我其他问题哟"
    ],
    "isbot":[
        "我是小夏，你的智能工业设备顾问",
        "你可以叫我小夏哦~",
        "我是工业设备诊断机器人小夏"
    ]
    }

default_answer = """很抱歉我还不知道回答你这个问题\n
                    你可以问我一些有关石油钻井泵的\n
                    故障原因、故障解决方法、部件日常维护、部件状态查询\n
                    相关问题哦~"""
def gossip_robot(intent):
    return random.choice(
        gossip_corpus.get(intent)
    )

def chat_answer():
    text = input("please type something:")
    label = model.predict(text)
    user_intent = label
    print("查询类别" , label)
    if user_intent in ["greet","goodbye","deny","isbot"]:
        reply = gossip_robot(user_intent)
        print(reply)
    elif user_intent=="accept": #如用户输入：是的
        #待后续处理..
        print(0)
    elif user_intent=="Knowledge Inquiry":#用户输入是知识查询意图
        #待后续处理.
        print("非闲聊意图,待后续处理")\

    else: #其他：一些不相关的输入
        print(default_answer)


if __name__ == '__main__':
    model = CLFModel('./model_file/')
    j = 1
    while j != 0:
        chat_answer()



    



    