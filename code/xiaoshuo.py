# -*- coding: utf-8 -*-
import time,requests as r
from tqdm import tqdm
from lxml import etree
def log(func):
    def wrapper(*args, **kw):
        print('run %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
def timeit(func):
    def wrapper(*args, **kwargs):
        d={"time":time.ctime(),"name":func.__name__}
        start_time = time.time()
        for i in tqdm(range(100),postfix=d,desc="%s:运行中" % func.__name__,ncols=100):
            time.sleep(0.01)
        res = func(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间为：%.8f" %(func.__name__, end_time - start_time))
        return res
    return wrapper
@timeit
def get(*url):
    global xpath1,xpath5
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
         #  "Cookie": "LIVE_BUVID=AUTO6715546997211617; buvid3=07192BD6-2288-4BA5-9259-8E0BF6381C9347193infoc; stardustvideo=1; CURRENT_FNVAL=16; sid=l0fnfa5e; rpdid=bfAHHkDF:cq6flbmZ:Ohzhw:1Hdog8",
        }
    for wz in url:
        html=r.get(wz,headers=headers).text
        html=etree.HTML(html,etree.HTMLParser())
        xpath1=html.xpath('//div[@class="main"]/div[@class="conter"]/ul/li[@class="conter1"]//text()')
        xpath2=html.xpath('//div[@class="main"]/div[@class="conter"]/ul/li[@class="conter2"]//text()')
        xpath3=html.xpath('//div[@class="main"]/div[@class="conter"]/ul/li[@class="conter4"]//text()')
        xpath4=html.xpath('//div[@class="main"]/div[@class="conter"]/ul/li[@class="conter3"]/text()')
        xpath5=html.xpath('//div[3]/div[2]/ul/li[1]/a')
        li=[]
        for cnmb in range(len(xpath1)):
            li.append(str(cnmb))
        for lis,fq,fk,fr,ft in zip(li,xpath1,xpath2,xpath3,xpath4):
            print(" %s. %s : %s : %s : %s " % (lis,fq,fk,fr,ft))
def wc(x):
    xs=xpath5[x].attrib
    print("http://530p.com"+xs['href'])
@log
def main():
    rb=[]
    for tt in range(0,30):
        rb.append(str(tt))
    global ym
    strs=input("输入搜索书名: ")
    while True:
        urll='http://www.530p.com/s/%s/%s/' % (strs,ym)
        dicts=[urll]
        get(*dicts)
        cd=input("输入序号获取,a d上下页,exit退出: ")
        if cd in rb:
            print("《"+xpath1[int(cd)]+"》: 获取中")
            wc(int(cd))
        elif cd == "a":
            if ym <= 1:
                print("没有上一页了")
                break
            else:
                ym-=1
        elif cd == "d":
            ym+=1
            print("下一页")
        elif cd == "exit":
            break
        else:
            print("参数错误")
            break
if __name__ == "__main__":
    ym=1
    main()
