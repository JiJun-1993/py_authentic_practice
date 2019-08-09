from pyquery import PyQuery
import requests


def get_web_article(url):
    '''
    通过网络文章的链接，获取文章的正文内容
    '''
    # 把链接存储起来
    # 链接获取的内容
    response = requests.get(url)
    # 提取正文
    document = PyQuery(response.text) 
    # 返回正文字符串
    return document('#js_content').text()

import jieba
from collections import Counter
def stats_text_cn(text,count):
    '''
    给出一个文章的内容，返回文章中出现的两个字以上的单词以及频率

    text:文章内容
    count: 频率排名在前count的单词
    '''
    seg_list = jieba.cut(text,cut_all=False) #精确模式
    chars = []
    # 排除长度小于2的词语
    for item in seg_list:
        if len(item) > 1:
            chars.append(item)          
    return Counter(chars).most_common(count)

import matplotlib.pylab as plt
from matplotlib.font_manager import FontProperties
# 提取字体对象
font = FontProperties(fname='/Library/Fonts/Songti.ttc')
def  text_graph(data,image_path = "1.png"):
    '''
    根据传入统计后单词数据生成图片，并保存在给定的路径下面

    data：数据
    image_path: 存储路径
    '''
    labels = [v[0] for v in data]
    widths = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos,widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels,FontProperties = font)
    ax.invert_yaxis()
    ax.set_ylabel("关键字",FontProperties = font)
    ax.set_xlabel("词频",FontProperties = font)
    ax.set_title("词频统计",FontProperties = font)
    plt.savefig(image_path)
    return image_path
    # plt.show()
    

# url = "https://mp.weixin.qq.com/s?__biz=MjM5NjAxOTU4MA==&mid=3009227944&idx=1&sn=e49abe70e3f40dc48dde676f58a6866f&chksm=904620bba731a9ad7fef0e9da20a9a505dbbfc802300bc01f25826611682f6ae4c10091a3866&mpshare=1&scene=1&srcid=&sharer_sharetime=1565316989130&sharer_shareid=a650fe44233d15768e07550857984e6f#rd"

from wxpy import *
import pickle
def savemsg(msg):
    fn = 'a.pkl' 
    with open(fn, 'w') as f: # open file with write-mode  
        picklestring = pickle.dump(msg, f)

