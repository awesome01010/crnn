# 去除一个txt文件里面所有重复的字符

import os,sys,datetime
import codecs
with open('./train.txt', 'r') as f:      #读入文本中的文件
    l = f.readlines()  # txt中所有字符串读入data
    x=set(l[0])
    for i in range(1,len(l)):
        x.update(l[i])
    s="".join(list(x))
    print(s)
with open('./result.txt','wb') as f1:   #把结果写到文件result中
    b=bytes(s,encoding="utf-8")
    f1.write(b)
