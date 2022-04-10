# pai_project
粗分类/细分类模型

**使用指南**

*1.使用Vs code 打开sklearn_Classification 文件夹并在终端安装python库*

*2.运行train.py 训练粗分类模型*

*3.运行 clf_model.py,开始机器人问答*

**2022年4月1日更新**

*1.使用convolutional neural network（CNN）进行细分类模型的构建，准确率还可以，目前模型通过 运行 train1.py 构建， 细分类文本储存在 data/data2.txt中*

*细分类文本分为reason，method，maintain，monitor和other五类。细分类模型准确度如下*  

![Alt text](sklearn_Classification/细分类模型准确度.jpg)

*2.使用fuzzywuzzy进行细分类问题的模糊匹配，并将其整合到小智的问答中。*

**目前需要解决的问题**  

*1.将使用CNN构建细分类模型应用在小智的问答中*  

*2.开始进行对应提问者的问题进行回答的代码的编写*
