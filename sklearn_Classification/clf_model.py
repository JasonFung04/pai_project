# -*- coding:utf-8 -*-

import os
from pdb import Restart
import pickle
import numpy as np
from sklearn import svm
#细分类模型import
from fuzzywuzzy import fuzz
from fuzzywuzzy import process




#粗分类模型代码

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


    #细分类模型代码
    choices_0 = ["请问石油钻井泵漏油了是为什么","石油钻井泵噪音很小是为什么","石油钻井泵有刺漏声是为什么","石油钻井泵噪音很大是为什么","石油钻井泵温度很低是为什么", "石油钻井泵温度很高是为什么","石油钻井泵过分晃动是为什么","石油钻井泵不动了是为什么","压力表变化很大是为什么","缸套处为什么有敲击声" ]

    a= process.extractOne(text, choices_0, scorer=fuzz.token_set_ratio)


    choices_1 = ["请问石油钻井泵漏油了怎么办","请问石油钻井泵裂开了怎么办","石油钻井泵噪音消失了怎么办","石油钻井泵噪音很大怎么办","石油钻井泵温度过低怎么办", "石油钻井泵温度很高怎么办","石油钻井泵不动了怎么办","空气包充不进气怎么办","怎么排出空气包气囊更换","石油钻井泵噪音很小是怎么办" ,"石油钻井泵有刺漏声是怎么办","石油钻井泵噪音很大是怎么办","石油钻井泵温度很低是怎么办","石油钻井泵温度很高是怎么办","石油钻井泵过分晃动是怎么办","石油钻井泵有泄漏怎么办","缸套处有敲击声怎么办","压力表下降怎么办","压力表上升怎么办","轴承好热，怎么办","无法排出空气怎么办","排泄孔盖的丝堵处是否积水"]

    b = process.extractOne(text, choices_1, scorer=fuzz.token_set_ratio)


    choices_2 = ["请问如何检查石油钻井泵","请问如何保养石油钻井泵","空气包充气注意事项有什么","石油钻井泵多久保养一次","上紧缸盖与阀盖前要多久涂润滑一次", "液力端的螺母和螺栓要多久检测一次","动力端油池的脏油多久换一次","十字头油池的脏油多久换一次","多久检测一次轴承状况","如何清洗活塞杆" ,"如何清洗缸套","泥浆管线上的所有阀门正确位置是什么样子的"]

    c = process.extractOne(text, choices_2, scorer=fuzz.token_set_ratio)

    choices_3 = ["请问石油钻井泵出现了什么问题","动力端出现什么故障了吗","液力端出现什么故障了吗","请问齿轮磨损情况如何","柴油机负荷多少", "现在哪些轴承有磨损","钻井平台排出液体是否正常","昨天石油钻井泵运行状况怎么样","前天石油钻井泵运行状况怎么样","本周石油钻井泵运行状况怎么样" ,"上周石油钻井泵运行状况怎么样","这个月石油钻井泵运行状况怎么样","早上石油钻井泵运行状况怎么样","下午石油钻井泵运行状况怎么样","昨天压力表示数变化大吗","昨天压力表示数值是多少吗","前天压力表示数变化大吗","前天压力表示数值是多少吗","这个月和上个月对比，压力表示数变化大吗","今天和昨天对比，压力表示数变化大吗","这段时间钻井平台排出液体有异常吗","这个月石油钻井泵泵速怎么样","早上石油钻井泵泵速怎么样","下午石油钻井泵泵速怎么样","喷淋泵水箱内水是否够用","排出空气包的充气压力，是否在正常范围","排出空气包的充气压力，是否在正常范围","现在轴承运行情况怎样"]
    d = process.extractOne(text, choices_3, scorer=fuzz.token_set_ratio)

    choices_4 = ["给我石油钻井泵的安装指引","动力端积油过多，怎么去油","石油钻井泵活塞用哪个","石油钻井泵齿轮润滑油用哪个","压力表灵敏度是多少","开泵时的注意事项","挂泵离合器的注意事项","泵的吸入管入口和泥浆地的距离多少合适","钻井泵是干嘛用的","钻井泵的动力端有什么作用","钻井泵的液力端有什么作用","钻井泵的基本性能参数有哪些"]
    e = process.extractOne(text, choices_4, scorer=fuzz.token_set_ratio)

    score = [a[1],b[1],c[1],d[1],e[1]];
    if max(score) == a[1]:
        i = "[0]故障原因"
    if max(score) == b[1]:
        i = "[1]解决方法"
    if max(score) == c[1]:
        i = "[2]监控及查询"
    if max(score) == d[1]:
        i = "[3]监控及查询"
    if max(score) == e[1]:
        i = "[4]其他"




    #粗分类模型代码
    if user_intent in ["greet","goodbye","deny","isbot"]:
        reply = gossip_robot(user_intent)
        print(reply)
    elif user_intent=="accept": #如用户输入：是的
        #待后续处理..
        print(0)
    elif user_intent=="Knowledge Inquiry":#用户输入是知识查询意图
        #待后续处理.#后续处理更新 2022/4/11

        text = "检查石油钻井泵" 
        #the text should be the question asked by the user in the front end website
        #some example of quesitions：
        # 1.检查石油钻井泵
        # 2.现在哪些轴承有磨损
        # 3. 石油钻井温度过高怎么办
        


        print("提问者最有可能的问题分类为", i)
        print("你是不是想问：", a[0],b[0],c[0],d[0],e[0])
        print("问题匹配程度：", a,b,c,d,e)
        print("非闲聊意图,待后续处理")\

    else: #其他：一些不相关的输入
        print(default_answer)

#载入模型，支持反复询问的代码
if __name__ == '__main__':
    model = CLFModel('./model_file/')
    j = 1
    while j != 0:
        chat_answer()
