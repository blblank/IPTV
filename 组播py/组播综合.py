


import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import os
import threading
from queue import Queue
from datetime import datetime
import replace
import fileinput

# 合并自定义频道文件#################################################################################################
file_contents = []
file_paths = ["四川电信.txt", "广东电信.txt", "天津联通.txt", "江苏电信.txt", "湖北电信.txt", "湖南电信.txt", "河北电信.txt", "安徽电信.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)

# 写入合并后的文件
with open("合并.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))
    


#替换多余的关键字词###################################################################################################
for line in fileinput.input("合并.txt", inplace=True):  #打开文件，并对其进行原地替换
    line = line.replace("CCTV-1高清测试", "")
    line = line.replace("CCTV-2高清测试", "")
    line = line.replace("CCTV-7高清测试", "")
    line = line.replace("CCTV-10高清测试", "")
    line = line.replace("中央", "CCTV")
    line = line.replace("高清", "")
    line = line.replace("HD", "")
    line = line.replace("标清", "")
    line = line.replace("超清", "")
    line = line.replace("频道", "")
    line = line.replace("-", "")
    line = line.replace(" ", "")
    line = line.replace("CCTV风云剧场", "风云剧场")
    line = line.replace("CCTV第一剧场", "第一剧场")
    line = line.replace("CCTV怀旧剧场", "怀旧剧场")
    line = line.replace("熊猫影院", "熊猫电影")
    line = line.replace("熊猫爱生活", "熊猫生活")
    line = line.replace("爱宠宠物", "宠物生活")
    
    line = line.replace("CCTV10", "CCTW10")
    line = line.replace("CCTV11", "CCTW11")
    line = line.replace("CCTV12", "CCTW12")
    line = line.replace("CCTV13", "CCTW13")
    line = line.replace("CCTV14", "CCTW14")
    line = line.replace("CCTV15", "CCTW15")
    line = line.replace("CCTV16", "CCTW16")
    line = line.replace("CCTV17", "CCTW17")
    #需要排在前面的频道
    line = line.replace("湖南卫视", "一一湖南卫视")
    line = line.replace("湖北卫视", "一一湖北卫视")
    line = line.replace("江苏卫视", "一江苏卫视")
    line = line.replace("安徽卫视", "一安徽卫视")
    line = line.replace("第一", "一第一")
    line = line.replace("风云", "一风云")
    line = line.replace("都市", "一都市")
    line = line.replace("谍战", "一谍战")
    line = line.replace("热门", "一热门")
    
    
    line = line.replace("专区", "")
    line = line.replace("卫视超", "卫视")
    line = line.replace("CCTV风云剧场", "风云剧场")
    line = line.replace("CCTV第一剧场", "第一剧场")
    line = line.replace("CCTV怀旧剧场", "怀旧剧场")
    line = line.replace("IPTV", "")
    line = line.replace("PLUS", "+")
    line = line.replace("＋", "+")
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("CAV", "")
    line = line.replace("美洲", "")
    line = line.replace("北美", "")
    line = line.replace("12M", "")
    line = line.replace("高清测试(CCTV-1", "")
    line = line.replace("高清测试(CCTV-2", "")
    line = line.replace("高清测试(CCTV-7", "")
    line = line.replace("高清测试(CCTV-10", "")
    line = line.replace("LD", "")
    line = line.replace("HEVC20M", "")
    line = line.replace("S,", ",")
    line = line.replace("测试", "")
    line = line.replace("试看", "")
    line = line.replace("测试", "")
    line = line.replace("测试cctv", "CCTV")
    line = line.replace("CCTV1综合", "CCTV1")
    line = line.replace("CCTV2财经", "CCTV2")
    line = line.replace("CCTV3综艺", "CCTV3")
    line = line.replace("CCTV4国际", "CCTV4")
    line = line.replace("CCTV4中文国际", "CCTV4")
    line = line.replace("CCTV4欧洲", "CCTV4")
    line = line.replace("CCTV5体育", "CCTV5")
    line = line.replace("CCTV5+体育", "CCTV5+")
    line = line.replace("CCTV6电影", "CCTV6")
    line = line.replace("CCTV7军事", "CCTV7")
    line = line.replace("CCTV7军农", "CCTV7")
    line = line.replace("CCTV7农业", "CCTV7")
    line = line.replace("CCTV7国防军事", "CCTV7")
    line = line.replace("CCTV8电视剧", "CCTV8")
    line = line.replace("CCTV8纪录", "CCTV9")
    line = line.replace("CCTV9记录", "CCTV9")
    line = line.replace("CCTV9纪录", "CCTV9")
    line = line.replace("CCTV10科教", "CCTV10")
    line = line.replace("CCTV11戏曲", "CCTV11")
    line = line.replace("CCTV12社会与法", "CCTV12")
    line = line.replace("CCTV13新闻", "CCTV13")
    line = line.replace("CCTV新闻", "CCTV13")
    line = line.replace("CCTV14少儿", "CCTV14")
    line = line.replace("央视14少儿", "CCTV14")
    line = line.replace("CCTV少儿超", "CCTV14")
    line = line.replace("CCTV15音乐", "CCTV15")
    line = line.replace("CCTV音乐", "CCTV15")
    line = line.replace("CCTV16奥林匹克", "CCTV16")
    line = line.replace("CCTV17农业农村", "CCTV17")
    line = line.replace("CCTV17军农", "CCTV17")
    line = line.replace("CCTV17农业", "CCTV17")
    line = line.replace("CCTV5+体育赛视", "CCTV5+")
    line = line.replace("CCTV5+赛视", "CCTV5+")
    line = line.replace("CCTV5+体育赛事", "CCTV5+")
    line = line.replace("CCTV5+赛事", "CCTV5+")
    line = line.replace("CCTV5+体育", "CCTV5+")
    line = line.replace("CCTV5赛事", "CCTV5+")
    line = line.replace("凤凰中文台", "凤凰中文")
    line = line.replace("凤凰资讯台", "凤凰资讯")
    line = line.replace("CCTV4K测试）", "CCTV4K")
    line = line.replace("上海东方卫视", "上海卫视")
    line = line.replace("东方卫视", "上海卫视")
    line = line.replace("内蒙卫视", "内蒙古卫视")
    line = line.replace("福建东南卫视", "东南卫视")
    line = line.replace("广东南方卫视", "南方卫视")
    line = line.replace("湖南金鹰卡通", "金鹰卡通")
    line = line.replace("炫动卡通", "哈哈炫动")
    line = line.replace("卡酷卡通", "卡酷少儿")
    line = line.replace("卡酷动画", "卡酷少儿")
    line = line.replace("BRTVKAKU少儿", "卡酷少儿")
    line = line.replace("优曼卡通", "优漫卡通")
    line = line.replace("优曼卡通", "优漫卡通")
    line = line.replace("嘉佳卡通", "佳嘉卡通")
    line = line.replace("CCTV世界地理", "世界地理")
    line = line.replace("BTV北京卫视", "北京卫视")
    line = line.replace("BTV冬奥纪实", "冬奥纪实")
    line = line.replace("东奥纪实", "冬奥纪实")
    line = line.replace("卫视台", "卫视")
    line = line.replace("湖南电视台", "湖南卫视")
    line = line.replace("少儿科教", "少儿")
    line = line.replace("影视剧", "影视")
    line = line.replace("电视剧", "影视")
    line = line.replace("CCTV1CCTV1", "CCTV1")
    line = line.replace("CCTV2CCTV2", "CCTV2")
    line = line.replace("CCTV7CCTV7", "CCTV7")
    line = line.replace("CCTV10CCTV10", "CCTV10")
    print(line, end="")  #设置end=""，避免输出多余的换行符



#二次替换某些关键词为便于排序的自定义词####################################################################################################
for line in fileinput.input("合并.txt", inplace=True):  #打开文件，并对其进行原地替换
    
    line = line.replace("CCTV10", "CCTW10")
    line = line.replace("CCTV11", "CCTW11")
    line = line.replace("CCTV12", "CCTW12")
    line = line.replace("CCTV13", "CCTW13")
    line = line.replace("CCTV14", "CCTW14")
    line = line.replace("CCTV15", "CCTW15")
    line = line.replace("CCTV16", "CCTW16")
    line = line.replace("CCTV17", "CCTW17")
    #需要排在前面的频道
    line = line.replace("湖南卫视", "一一湖南卫视")
    line = line.replace("湖北卫视", "一一湖北卫视")
    line = line.replace("江苏卫视", "一江苏卫视")
    line = line.replace("安徽卫视", "一安徽卫视")
    line = line.replace("第一", "一第一")
    line = line.replace("风云", "一风云")
    line = line.replace("都市", "一都市")
    line = line.replace("谍战", "一谍战")
    line = line.replace("热门", "一热门")
    line = line.replace("专区", "")
    line = line.replace("卫视超", "卫视")
    line = line.replace("IPTV", "")
    line = line.replace("东奥纪实", "冬奥纪实")
    line = line.replace("卫视台", "卫视")
    line = line.replace("湖南电视台", "湖南卫视")
    line = line.replace("少儿科教", "少儿")
    line = line.replace("影视剧", "影视")
    line = line.replace("电视剧", "影视")
    line = line.replace("CCTV1CCTV1", "CCTV1")
    line = line.replace("CCTV2CCTV2", "CCTV2")
    line = line.replace("CCTV7CCTV7", "CCTV7")
    line = line.replace("CCTV10CCTV10", "CCTV10")
    print(line, end="")  #设置end=""，避免输出多余的换行符


#对替换完成的文本进行排序#####################################################################################################################

with open('合并.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines.sort()

with open('排序.txt', 'w', encoding='UTF-8') as f:
    for line in lines:
        f.write(line)


#再次替换自定义词为常规词##########################################################################################################################
for line in fileinput.input("排序.txt", inplace=True):  #打开文件，并对其进行原地替换
    line = line.replace("CCTW10", "CCTV10")
    line = line.replace("CCTW11", "CCTV11")
    line = line.replace("CCTW12", "CCTV12")
    line = line.replace("CCTW13", "CCTV13")
    line = line.replace("CCTW14", "CCTV14")
    line = line.replace("CCTW15", "CCTV15")
    line = line.replace("CCTW16", "CCTV16")
    line = line.replace("CCTW17", "CCTV17")
    line = line.replace("DCTW4K", "CCTV4K")
    line = line.replace("CCTV4K测试）", "CCTV4")
    line = line.replace("CCTV164K", "CCTV16 4K")
    line = line.replace("CCTV54K", "CCTV5 4K")
    line = line.replace("CCTV8K", "CCTV 8K")
    line = line.replace("CCTV4K", "CCTV 4K")
    line = line.replace("卫视台", "卫视")
    line = line.replace("iHOT", "")
    line = line.replace("一一", "")
    line = line.replace("CHC电影", "CHC高清电影")
    line = line.replace("影视剧", "影视")
    line = line.replace("电视剧", "影视")
    line = line.replace("淮北教育", "安徽CCTV ")
    line = line.replace("CCTV1CCTV1", "CCTV1")
    line = line.replace("CCTV2CCTV2", "CCTV2")
    line = line.replace("CCTV7CCTV7", "CCTV7")
    line = line.replace("CCTV10CCTV10", "CCTV10")
    line = line.replace("高清电影", "影迷电影")
    print(line, end="")  #设置end=""，避免输出多余的换行符



#从整理好的文本中按类别进行特定关键词提取#############################################################################################
keywords = ['CCTV1,', 'CCTV10,', 'CCTV11,', 'CCTV12,', 'CCTV13,', 'CCTV14,', 'CCTV15,', 'CCTV16,', 'CCTV17,', 'CCTV2,', 'CCTV3,', 'CCTV4,', 'CCTV5,', 'CCTV6,', 'CCTV7,', 'CCTV8,', 'CCTV9,', '环绕']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('c.txt', 'w', encoding='utf-8') as c:    #####定义临时文件名
    c.write('央视频道,#genre#\n')                                                                  #####写入临时文件名
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
         c.write(line)  # 将该行写入输出文件                                                          #####定义临时文件
for line in fileinput.input("c.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    line = line.replace("综合文艺", "")                                                                         ###########                                                      ###########
    line = line.replace("科教", "")                                                                         ###########                                                      ###########
    line = line.replace("社会与法", "")                                                                         ###########                                                      ###########
    line = line.replace("新闻", "")                                                                         ###########                                                      ###########
    line = line.replace("少儿", "")                                                                         ###########                                                      ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    line = line.replace("地理世界", "世界地理")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符          

#从整理好的文本中按类别进行特定关键词提取#############################################################################################
keywords = ['风云', '兵器', '女性', '地理', '央视文化', '风云', '怀旧剧场', '第一剧场', 'CHC']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('e.txt', 'w', encoding='utf-8') as e:    #####定义临时文件名
    e.write('\n央视频道,#genre#\n')                                                                  #####写入临时文件名
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
         e.write(line)  # 将该行写入输出文件                                                          #####定义临时文件
for line in fileinput.input("e.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    line = line.replace("综合文艺", "")                                                                         ###########                                                      ###########
    line = line.replace("科教", "")                                                                         ###########                                                      ###########
    line = line.replace("社会与法", "")                                                                         ###########                                                      ###########
    line = line.replace("新闻", "")                                                                         ###########                                                      ###########
    line = line.replace("少儿", "")                                                                         ###########                                                      ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    line = line.replace("地理世界", "世界地理")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符          




##########################################################################################################################################################################################
keywords = ['卫视', '凤凰']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('ws.txt', 'w', encoding='utf-8') as ws:
    ws.write('\n卫视频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          ws.write(line)  # 将该行写入输出文件


###############################################################################################################################################################################
keywords = ['4K', '8K']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('DD.txt', 'w', encoding='utf-8') as DD:
    DD.write('\n4K 频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          DD.write(line)  # 将该行写入输出文件

for line in fileinput.input("DD.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符      


###############################################################################################################################################################################            
keywords = ['热门剧场', '经典剧场', '抗战剧场', '谍战剧场', '军旅剧场', '华语影院', '影', '剧', '淘', '爱']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('ys.txt', 'w', encoding='utf-8') as ys:
    ys.write('\n影视频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          ys.write(line)  # 将该行写入输出文件

for line in fileinput.input("ys.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符      



###############################################################################################################################################################################
keywords = ['湖南', '广东', '武汉', '湖北', '安徽', '河北', '石家庄', '珠海', '广州']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('df.txt', 'w', encoding='utf-8') as df:
    df.write('\n省市频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          df.write(line)  # 将该行写入输出文件
for line in fileinput.input("df.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符      

###############################################################################################################################################################################
keywords = ['综合', '公共', '生活', '新闻', '电视', '教育', '科技', '文艺', '经济']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('xs.txt', 'w', encoding='utf-8') as xs:
    xs.write('\n地方频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          xs.write(line)  # 将该行写入输出文件
for line in fileinput.input("xs.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符      


###############################################################################################################################################################################
keywords = [',']  # 需要提取的关键字列表
pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字
#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制
with open('排序.txt', 'r', encoding='utf-8') as file, open('qt.txt', 'w', encoding='utf-8') as qt:
    qt.write('\n其他频道,#genre#\n')
    for line in file:
        if re.search(pattern, line):  # 如果行中有任意关键字
          qt.write(line)  # 将该行写入输出文件
for line in fileinput.input("qt.txt", inplace=True):  #打开文件，并对其进行关键词原地替换                     ###########
    line = line.replace("AA", "")                                                                         ###########                                                      ###########
    print(line, end="")  #设置end=""，避免输出多余的换行符      






# 读取要合并的频道文件，并生成临时文件##############################################################################################################
file_contents = []
file_paths = ["c.txt", "e.txt", "ws.txt", "DD.txt", "ys.txt", "df.txt", "xs.txt", "qt.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)
# 生成合并后的文件
with open("GAT.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))

           

 ###########################################################################################################################################################################     
# 读取临时文件，并生成结果文件。这一步其实多余，懒得改##############################################################################################################
file_contents = []
file_paths = ["GAT.txt"]  # 替换为实际的文件路径列表


for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)
###########################################################################################################################################################################



# 写入合并后的文件
with open("组播合并.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))

for line in fileinput.input("组播合并.txt", inplace=True):  #打开文件，并对其进行关键词原地替换  
    line = line.replace("固定源", "固定")   
    line = line.replace("更新", "")             
    line = line.replace("港澳频道/", "港澳/")    
    print(line, end="")  #设置end=""，避免输出多余的换行符   
for line in fileinput.input("组播合并.txt", inplace=True):  #打开文件，并对其进行关键词原地替换  
    line = line.replace("固定", "随时失效")  
    line = line.replace("频道", "")  
    line = line.replace("地波1080", "地波")  
    line = line.replace("自动", "自动更新")  
    print(line, end="")  #设置end=""，避免输出多余的换行符   


#########原始顺序去重，以避免同一个频道出现在不同的类中
with open('组播合并.txt', 'r', encoding="utf-8") as file:
 lines = file.readlines()
# 使用列表来存储唯一的行的顺序 
 unique_lines = [] 
 seen_lines = set() 
# 遍历每一行，如果是新的就加入unique_lines 
for line in lines:
 if line not in seen_lines:
  unique_lines.append(line)
  seen_lines.add(line)
# 将唯一的行写入新的文档 
with open('组播合并.txt', 'w', encoding="utf-8") as file:
 file.writelines(unique_lines)
#####################






###########################################################################################################################################################################
#任务结束，删除不必要的过程文件###########################################################################################################################
os.remove("GAT.txt")
os.remove("ws.txt")
os.remove("DD.txt")
os.remove("df.txt")
os.remove("ys.txt")
os.remove("xs.txt")
os.remove("qt.txt")
os.remove("c.txt")
os.remove("e.txt")
os.remove("排序.txt")
os.remove("合并.txt")
print("任务运行完毕，分类频道列表可查看文件夹内结果.txt文件！")
