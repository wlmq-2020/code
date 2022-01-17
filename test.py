# import sys
# import io

# from bs4 import BeautifulSoup

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# import hashlib

# a = {}
# b = ()
# c = set()
#
# print(type(a),type(b),type(c))

#
# def md5(url):
#     hash = hashlib.md5()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
#     hash.update(bytes(url,encoding='utf-8'))  # 要对哪个字符串进行加密，就放这里
#     print(hash.hexdigest())  # 拿到加密字符串
#     # a = hashlib.md5("url".encode("utf-8"))
#     # print(a.hexdigest())
# md5('123')

# a = '<img data-rootid="126940016" alt="玛丽莲·梦露的健身旧照曝光\n,照片中性感女神身着内衣举哑铃、做倒立，展现阳光性感。
# " data-iid="" src="https://c-ssl.duitang.com/uploads/blog/201403/13/20140313115405_BaV2u.thumb.400_0.jpeg"
# height="320">'
# #
# alt = re.findall('alt="(.*)\n',a)
# # img = re.findall('src="(.*)" h',a)
# print(a,'\n')
# print(alt)
# print(img[0])

# a = str(uuid.uuid4())
# print(type(a))

#
# class Princc:
#     def p_t(self):
#         print('t')
#
#     def p_ll(self):
#         print('ll')
#
#
# a = Princc()
# a.p_t()
# a.p_ll()
#

import socket
import time
import threading

#
# # 1 创建一个socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 服务器起不来，换个端口 试试看
# # 绑定IP和端口  端口不能用1024以下的，是系统的
# server.bind(('192.168.1.201', 162))
#
# # 监听
# server.listen(1)
# print("服务器启动成功......")
#
# # 等待链接
# # 可以接收两个值1socket和address地址
# ck = threading.local
#
#
# def run(ck):
#     data = ck.recv(1024)
#
#     print("收到的数据:" + data.decode("utf-8"))
#     # endData = input("输入返回给客户端的数据")
#
#     clientSocket.send("maike hong is good man".encode("utf-8"))
#
#
# while True:
#     clientSocket, clientAddress = server.accept()
#
#     #  print("%s---%s链接成功" % (str(clientSocket), clientAddress))
#
#     t = threading.Thread(target=run, args=(clientSocket,))
#     t.start()
#
#     print("线程")
# #

#
# import socket
#
# client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('127.0.0.1',8990))
#
# count=0
# while True:
#     count+=1
#     data = input("请输入给服务器发送的数据\n")
#     client.send(data.encode("utf-8"))
#     #接收
#     info=client.recv(8990)
#     print("服务器说:", info.decode("utf-8"))

# 描述符1
# class foo:
#     def get_aaa(self):
#         print('get时候运行我')
#
#     def set_aaa(self,value):
#         print('set时候运行我')
#
#     def del_aaa(self):
#         print('del的时候运行我')
#     aaa = property(get_aaa,set_aaa,del_aaa)
#
#
# f1 = foo()
# f1.aaa
# f1.aaa = 'AAA'
# del f1.aaa
# print('*'*22)
#
# # 描述符2
#
# class fooo:
#     @property
#     def aaa(self):
#         print('get的时候运行我啊')
#     @aaa.setter
#     def aaa(self,value):
#         print('set的时候运行我啊')
#     @aaa.deleter
#     def aaa(self):
#         print('del的时候运行我啊')
#
# f1 = fooo()
# f1.aaa
# f1.aaa = "111"
# del f1.aaa


# import requests
# from bs4 import BeautifulSoup
# import re
#
# url = 'https://m.laishu8.com/11/11522/53302325.html'
#
# page = requests.get(url=url).content
# soup = BeautifulSoup(page,features='html.parser').decode('gbk')
#
# print(soup.index('<div id="nr1">'))
# print(soup.index('<font color="red">'))
# print(soup[3694:5603])
#

# import requests
# import re
# from lxml import etree
# import time

# 下载abc.txt链接里的小说
#
# with open('abc.txt','r') as f:
#     for i in f.readlines():
#         print('准备开始下载%s'%i)
#         f = requests.get(url=i).content.decode('gbk')
#         time.sleep(2)
#         selsctor = etree.HTML(f)
#         title = str(selsctor.xpath('//*[@id="nr_title"]/text()')[0].strip()[0:-4])
#         text = str(selsctor.xpath('//*[@id="nr1"]/text()'))[1:-1]
#         with open(title + '.txt', 'a') as f:
#             print('正在写入', title)
#             f.write(text + ',\n')
#             print('写入%s完成' % title)
#             time.sleep(1)


# 多线程下载abc.txt里的小说  先并发30个请求，然后等着回来数据，在进行存储
#
# from concurrent.futures import ThreadPoolExecutor
# import time
# start = time.time()
# pool = ThreadPoolExecutor(50)
# a = []
#
# with open('abc.txt', 'r') as f:
#     for i in f.readlines():
#         a.append(i)
#
#
# def task(url):
#     print(url)
#     print('准备开始下载%s'%url)
#     f = requests.get(url=url).content.decode('gbk')
#     selsctor = etree.HTML(f)
#     title = str(selsctor.xpath('//*[@id="nr_title"]/text()')[0].strip()[0:-4])
#     text = str(selsctor.xpath('//*[@id="nr1"]/text()'))[1:-1]
#     with open(title+'.txt', 'w') as f:
#         print('正在写入', title)
#         f.write(text + ',\n')
#         print('写入%s完成' % title)
#
#
# for url in a:
#     pool.submit(task,url)
#
# pool.shutdown(wait=True)
# end = time.time() - start
# print('用时%s秒'%end)
# 20线程 用时 13.321978569030762
# 50线程 用时 5.888213157653809秒


# 20线程 用时 13.79185152053833
# 50线程 用时 6.197977542877197秒
# 多线程下载abc.txt里的小说  先并发30个请求， 然后结束，
# 继续发别的数据，等数据回来了，有进行自动进行接收
# from concurrent.futures import ThreadPoolExecutor
# import time
# import requests
# start = time.time()
# pool = ThreadPoolExecutor(50)
# url_list = [1,2,3,4,5]
# # with open('abc.txt', 'r') as f:
# #     for i in f.readlines():
# #         url_list.append(i)
#
#
# def task(url):
#     print('task',url)
#     # print('准备开始下载%s'%url)
#     # response = requests.get(url=url).content.decode('gbk')
#     return url
#
# def done(future,*args,**kwargs):
#     response = future.result()
#     print('done',future)
#     # selsctor = etree.HTML(response)
#     # title = str(selsctor.xpath('//*[@id="nr_title"]/text()')[0].strip()[0:-4])
#     # text = str(selsctor.xpath('//*[@id="nr1"]/text()'))[1:-1]
#     # with open(title + '.txt', 'w') as f:
#     #     print('正在写入', title)
#     #     f.write(text + ',\n')
#     #     print('写入%s完成' % title)
#
#
# for url in url_list:
#     v = pool.submit(task,url)
#     v.add_done_callback(done)
#
# pool.shutdown(wait=True)
# end = time.time() -start
# print('用时%s秒'%end)
# 20线程 用时 13.79185152053833
# 50线程 用时 6.197977542877197


# 多进程#
# from concurrent.futures import ProcessPoolExecutor
# import time
# import requests
# start = time.time()
# pool = ProcessPoolExecutor(5)
# url_list = []
# with open('abc.txt', 'r') as f:
#     for i in f.readlines():
#         url_list.append(i)
#
#
# def task(url):
#     print(url)
#     print('准备开始下载%s'%url)
#     response = requests.get(url=url).content.decode('gbk')
#     return response
#
# def done(future,*args,**kwargs):
#     response = future.result()
#     selsctor = etree.HTML(response)
#     title = str(selsctor.xpath('//*[@id="nr_title"]/text()')[0].strip()[0:-4])
#     text = str(selsctor.xpath('//*[@id="nr1"]/text()'))[1:-1]
#     with open(title + '.txt', 'w') as f:
#         print('正在写入', title)
#         f.write(text + ',\n')
#         print('写入%s完成' % title)
#
#
# for url in url_list:
#     v = pool.submit(task,url)
#     v.add_done_callback(done)
#
# pool.shutdown(wait=True)
# end = time.time() -start
# print('用时%s秒'%end)


# 多进程2
#
# import concurrent.futures
# import time
# import requests
# from lxml import etree
# url_list = []
# with open('abc.txt', 'r') as f:
#     for i in f.readlines():
#         url_list.append(i)
#
# def task(url):
#     print(url)
#     print('准备开始下载%s' % url)
#     f = requests.get(url=url).content.decode('gbk')
#     selsctor = etree.HTML(f)
#     title = str(selsctor.xpath('//*[@id="nr_title"]/text()')[0].strip()[0:-4])
#     text = str(selsctor.xpath('//*[@id="nr1"]/text()'))[1:-1]
#     with open(title + '.txt', 'w') as f:
#         print('正在写入', title)
#         f.write(text + ',\n')
#         print('写入%s完成' % title)
#
#
# def main():
#     with concurrent.futures.ProcessPoolExecutor(5) as pool:
#         for url in url_list:
#             pool.submit(task, url)
#             print(dir(pool))
#         # pool.map(task, url_list)
#         # print(dir(pool))
#
# if __name__ == '__main__':
#     start = time.time()
#     main()
#     end = time.time() - start
#     print('用时%s秒' % end)


# 1.asyncio示例1    多进程
# import asyncio
# # 可以实现多进程，但是asynio不支持http  只支持tcp，所以需要改造tcp数据格式
#
# @asyncio.coroutine
# def func1():
#     print('before...func1......')
#     yield from asyncio.sleep(5)
#     print('end...func1......')
#
#
# tasks = [func1(), func1()]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

'''
# 1.asyncio示例2，tcp改造成http

import asyncio


@asyncio.coroutine
def fetch_async(host, url='/'):
    print(host, url)
    reader, writer = yield from asyncio.open_connection(host, 80)

    request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
    request_header_content = bytes(request_header_content, encoding='utf-8')

    writer.write(request_header_content)
    yield from writer.drain()
    text = yield from reader.read()
    print(host, url, text)
    writer.close()

tasks = [
    fetch_async('www.cnblogs.com', '/wupeiqi/'),
    fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

'''

'''
import aiohttp
import asyncio


@asyncio.coroutine
def fetch_async(url):
    print(url)
    response = yield from aiohttp.request('GET', url)
    # data = yield from response.read()
    # print(url, data)
    print(url, response)
    response.close()


tasks = [fetch_async('http://www.google.com/'), fetch_async('http://www.chouti.com/')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()

2.asyncio + aiohttp

'''

# asyncio 和 requests
'''
import asyncio
import requests


@asyncio.coroutine
def fetch_async(func, *args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args)
    response = yield from future
    print(response.url, response.content)


tasks = [
    fetch_async(requests.get, 'http://www.cnblogs.com/wupeiqi/'),
    fetch_async(requests.get, 'http://dig.chouti.com/pic/show?nid=4073644713430508&lid=10273091')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

3.asyncio + requests

'''

'''
########################### http 请求数据本质，阻塞 ##########################
import socket

sk = socket.socket()
# 1.链接

sk.connect(('www.baidu.com', 80))  # IO阻塞
print('链接成功')

# 2.链接成功后发送信息

sk.send(b'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n')
# sk.send(b'POST / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\nk1=v1&k2=v2')


# 3 等着服务器响应

data = sk.recv(8096)  # IO阻塞
print(data)
# 关闭链接
sk.close()
'''

'''
########################### http 请求数据本质，非阻塞 ##########################
import socket

sk = socket.socket()
# sk.setblocking(False)   # 把socket变成非阻塞
# 1.链接
try:
    sk.connect(('www.baidu.com', 80))  # IO阻塞
    print('链接成功')
except BlockingIOError as e:
    print(e)
# 2.链接成功后发送信息

sk.send(b'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n')
# sk.send(b'POST / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\nk1=v1&k2=v2')


# 3 等着服务器响应

data = sk.recv(8096)  # IO阻塞
print(data)
# 关闭链接
sk.close()
'''

'''
import socket
import select


class HttpRequest:
    def __init__(self, sk, host, callback):
        self.socket = sk
        self.host = host
        self.callback = callback

    def fileno(self):
        return self.socket.fileno()


class HttpResponse:
    def __init__(self, recv_data):
        self.recv_data = recv_data
        self.heads = {}
        self.body = None
        self.initialize()

    def initialize(self):
        hreads, body = self.recv_data.split(b'\r\n\r\n', 1)
        self.body = body
        hreads_list = hreads.split(b'\r\n')
        for head in hreads_list:
            # print(head)
            str_hread = str(head, encoding='utf-8')
            v = str_hread.split(':', 1)
            if len(v) == 2:
                self.heads[v[0]] = v[1]
                # print('v1^^',v[1])


class AsyncRequest:
    def __init__(self):
        self.conn = []
        self.connection = []  # 用于监测谁还未链接成功

    def add_request(self, host, callback):
        try:
            sk = socket.socket()
            sk.setblocking(0)
            sk.connect((host, 80))
        except BlockingIOError as e:
            pass

        request = HttpRequest(sk, host, callback)

        self.conn.append(request)
        self.connection.append(request)

    def run(self, ):
        while True:
            rlist, wlist, elist = select.select(self.conn, self.connection, self.conn, 0.05)
            for w in wlist:
                # print(w,'链接成功')
                # 只要能循环到 说明socket和服务器已经连接成功
                tpl = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % (w.host,)
                w.socket.send(bytes(tpl, encoding='utf-8'))
                self.connection.remove(w)

            for r in rlist:
                # r,是HttpRequet
                recv_data = bytes()
                print(r.host, '准备接收数据')
                while True:

                    try:
                        chunck = r.socket.recv(8096)
                        # if len(chunck) != 0:
                        #     # print(chunck)
                        recv_data += chunck
                        # print(recv_data)
                    except BlockingIOError as e:
                        break

                response = HttpResponse(recv_data)

                r.callback(response)
                # print('返回信息', r.host, recv_data)
                r.socket.close()
                self.conn.remove(r)

            if len(self.conn) == 0:
                break


def task1(response):
    print('task1  返回头存入文件', response.heads)


def task2(response):
    print('task2  返回体存入数据库', response.body)


url_list = [{'host': 'www.baidu.com', 'callback': task1},
            {'host': 'www.163.com', 'callback': task2}, ]

req = AsyncRequest()
for item in url_list:
    req.add_request(item['host'], item['callback'])

req.run()

'''

'''
c = str(input('输入行和列：\n'))
m = int(c.split(' ')[0])
n = int(c.split(' ')[1])

for i in range(1, m * n + 1):
    if i % n == 0:
        print(i, end='\n')
    else:
        if i > 99:
            print(i, end='  ')
        elif i > 9:
            print(i, end='   ')
        else:
            print(i, end='    ')
'''

'''

# 十进制转换二进制
print(bin(3))  # 0b11

# 十进制换8进制
print(oct(9))  # 0o11

# 将十进制转换成16进制
print(hex(15))  # 0xf

print(bool(0))  # False
print(bool('a'))  # True

# 将一个数据转换成字节形势
print(bytes('你好', encoding='utf-8'))

# 将一个数字转换成对应ascII码值
print(chr(97))  # a
print(chr(65))  # A

# 将一个字符转换成对应的ascII值
print(ord('a'))  # 65


# 类方法，直接调用类的函数输出
class Foo:
    @classmethod
    def test(cls):
        print('正在使用test')


Foo.test()

print(dir())

# 将字符串里的数据提取出来
print(eval("{'k1':'v1'},{'k2':'v2'},(1,2,3,4)"))

# format格式化数据
print("{}已经{}岁了".format('李麒',30))
print("%s已经%s岁了"%('李麒',30))

print(globals())

# hash算法
print(hash('sdfsdf'))

# 打印内存地址
print(id(123))

# 判断数据格式
print(isinstance(123, str))
print(isinstance(123, int))

# # pow(目标，几次方，取余)
print(pow(2, 2, 3))

print(range(1,9))

print(round(1.5 ))
'''

# import xlrd
# import xlwt
# import re

# workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\新疆明达电力科技有限公司华电内网监测2019123施工进度表.xls')
# print(workbook.sheet_names())
# Sheet1 = workbook.sheet_by_name('Sheet1')
# h = Sheet1.nrows
# l = Sheet1.ncols
# print(h,l)
# for i in range(h):
#     print('\n')
#     for j in range(l):
#         value = Sheet1.cell(i,j)
#         print(value.value,'   ',end=' ',)


# def len_byte(value):
#     length = len(value)
#     utf8_length = len(value.encode('utf-8'))
#     length = (utf8_length - length) / 2 + length
#     return int(length)


# Apr 17 22:19:28 FFC3 user.info DLT645-97[013][6704]: < 68364399 32000068 810646E3 6B453537  h6C.2..h..F.kE57
#  提取桌面上的session.log文件，存储文件为excel表

# with open(r'C:\Users\Administrator\Desktop\session.log', 'r') as f:
#     h = 1
#     Excel = xlwt.Workbook()
#     sheet1 = Excel.add_sheet('采集报文')
#     # 设置字体
#     font = xlwt.Font()
#
#     font.bold = True
#     # 读取每个字符的长度
#
#     col_width = []
#     for line in f.readlines():
#         line = line.strip(' ')
#         if re.findall('(<--)|(-->)', line):
#             list_line = line.split()
#             list_line[0] = list_line[0] + ' ' + list_line[1] + ' ' + list_line[2]
#             if h == 6566: break
#             if len(line.split()) > 5:
#                 li = 0
#                 times = line.split()[0] + ' ' + line.split()[1] + ' ' + line.split()[2]
#                 sheet1.col(li).width = 256 * (len(times) + 1)
#                 sheet1.write(h, li, times)
#                 li += 1
#                 model = line.split()[3]
#                 sheet1.col(li).width = 256 * (len(model) + 3)
#                 sheet1.write(h, li, model)
#                 li += 1
#                 aler_mess = line.split()[4]
#                 sheet1.col(li).width = 256 * (len(aler_mess) + 1)
#                 sheet1.write(h, li, aler_mess)
#                 li += 1
#                 statute = line.split()[5]
#                 sheet1.col(li).width = 256 * (len(statute) + 1)
#                 sheet1.write(h, li, statute)
#                 li += 1
#                 mess = re.findall(']:(.*)', line.strip(' '))[0]
#                 # 设置宽度
#                 sheet1.col(li).width = 256 * 200
#                 sheet1.write(h, li, mess)
#                 h += 1
#                 # print('times:', times)
#                 # print('model:', model)
#                 # print('aler_mess:', aler_mess)
#                 # print('mess:', mess)
#
# Excel.save('采集报文.xls')


# status = [['年', '月'], ['2018', '10'], ['2017', '9'], ['2016', '6'], ['2015', '4']]
# Excel = xlwt.Workbook()
# sheet1 = Excel.add_sheet('电量报表', cell_overwrite_ok=True)
# h = 0
# l = 0
# for i in status:
#     l = 0
#     sheet1.write(h, l, i[0])
#     l += 1
#     sheet1.write(h, l, i[1])
#     h += 1
#
# Excel.save('电量报表.xls')


# # # # # # # # import random

# # # # # # # #
# # # # # # # # count = 0
# # # # # # # #
# # # # # # # # while count <100 :
# # # # # # # #     if count % 2 == 0 :
# # # # # # # #         print("我想让你得到我....." , count )
# # # # # # # #
# # # # # # # #     count += 1
# # # # # # #
# # # # # # #
# # # # # # # # import  random
# # # # # # # #
# # # # # # # # guess = random.randint(0,1000)
# # # # # # # #
# # # # # # # #     while guess < 2001 :
# # # # # # # #     if   guess >=900 :
# # # # # # # #         print('大于900',guess)
# # # # # # # #         guess = random.randint(0, 1000)
# # # # # # # #     elif guess >=500:
# # # # # # # #         print('大于500',guess)
# # # # # # # #         guess = random.randint(0, 1000)
# # # # # # # #     elif guess >=0:
# # # # # # # #         print('大于0',guess)
# # # # # # # #         guess = random.randint(0, 1000)
# # # # # # #
# # # # # # #
# # # # # # # # def WuYanHui():
# # # # # # # #     print('Dog Wu')
# # # # # # # #
# # # # # # # # WuYanHui()
# # # # # # # #
# # # # # # # # type(WuYanHui())
# # # # # # #
# # # # # # # #
# # # # # # # # while True :
# # # # # # # #     print('我的天啊！')
# # # # # # #
# # # # # # # # age = 30
# # # # # # # # n = 0
# # # # # # # # guess = int(input('猜猜我的年龄：'))
# # # # # # # # if guess == age:
# # # # # # # #     print('恭喜你猜对了！')
# # # # # # # #
# # # # # # # # elif guess != age:
# # # # # # # #     # n += 1
# # # # # # # #     # n < 3
# # # # # # # #     print(n)
# # # # # # # #     print('猜错了，请继续')
# # # # # # # #     guess = input('猜猜我的年龄：')
# # # # # # # # elif guess != age:
# # # # # # # #     # n += 1
# # # # # # # #     # n < 3
# # # # # # # #     print(n)
# # # # # # # #     print('猜错了，请继续')
# # # # # # # #     guess = input('猜猜我的年龄：')
# # # # # # #
# # # # # # #
# # # # # # # # age = 30
# # # # # # # # n = 1
# # # # # # # # #！最多回答3次，错误锁定。
# # # # # # # # while n <= 3:
# # # # # # # #
# # # # # # # #     guess = int(input('猜猜我的年龄：'))
# # # # # # # #     if guess == age:
# # # # # # # #         print("恭喜，回答正确")
# # # # # # # #         break
# # # # # # # #     else:
# # # # # # # #         print('猜错啦！')
# # # # # # # #         n +=1
# # # # # # # # else :
# # # # # # # #      print('输入错误，锁定')
# # # # # # #
# # # # # # #
# # # # # # # # age = 30
# # # # # # # # n = 1
# # # # # # # #
# # # # # # # # Buttn = []
# # # # # # # #
# # # # # # # # while n <= 3:
# # # # # # # #
# # # # # # # #     guess = int(input('猜猜我的年龄：'))
# # # # # # # #     if guess == age:
# # # # # # # #         print("恭喜，回答正确")
# # # # # # # #         break
# # # # # # # #     else:
# # # # # # # #         print('猜错啦！')
# # # # # # # #         n +=1
# # # # # # # # else
# # # # # # # #      print('输入错误，锁定')
# # # # # # #
# # # # # # # # buttn = 'y'
# # # # # # # # while buttn == 'y' :
# # # # # # # #       buttn = input('输入Y/y或者N/n：')
# # # # # # # #       print('not')
# # # # # # # # elif  buttn == 'Y':
# # # # # # # #       print('ok')
# # # # # # #
# # # # # # # # ################################  bug就是guess只能输数字   Buttn 只能输y和n  其他会直接结束
# age = 30
# x = 1
# yes = ['Y', 'y','1']
# no = ['N', 'n','2']
# Buttn = 'y'
#
# while Buttn in yes:
#
#     while x <= 3:
#         guess = int(input('猜猜我的年龄：'))
#
#         if guess == age:
#             print("恭喜，回答正确")
#             exit()
#         else:
#             print('猜错啦！')
#             x += 1
#     else:
#         print('输入错误')
#         Buttn = input('输入y/Y继续，取消输入n/N：')
#         x = 1
#         print()
#
# else:
#     print('程序结束')

# # # # # # # # ####################################
# # # # # # #
# # # # # # # # names = ['Michael', 'Bob', 'Tracy']
# # # # # # # # for name in names:
# # # # # # # #     print(name)
# # # # # # # #
# # # # # # #
# # # # # # # # n = 0
# # # # # # # # while n < 10:
# # # # # # # #     n = n + 1
# # # # # # # #     if n % 2 == 0:  # 如果n是偶数，执行continue语句
# # # # # # # #         continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
# # # # # # # #     print(n)
# # # # # # #
# # # # # # #
# # # # # # # #
# # # # # # # # age = 30
# # # # # # # # x = 0
# # # # # # # #
# # # # # # # # Button = 'y'
# # # # # # # #
# # # # # # # # while Button == 'Y' or Button == 'y':
# # # # # # # #     while x <= 3:
# # # # # # # #         guess = input('猜猜我的年龄：')
# # # # # # # #         # x +=1
# # # # # # # #         print(x)
# # # # # # # #         if guess == age:
# # # # # # # #             print("恭喜，回答正确")
# # # # # # # #             exit()
# # # # # # # #         else:
# # # # # # # #             print('猜错啦！')
# # # # # # # #             x += 1
# # # # # # # #     else:
# # # # # # # #         print('请输入Y/y继续或者N/n推出程序:')
# # # # # # # #         x=0
# # # # # # # #         Button = input()
# # # # # # # #         continue
# # # # # # # # while Button == 'N' or Button =='n':
# # # # # # # #     print('已经退出')
# # # # # # # #     exit()
# # # # # # # #     #continue
# # # # # # # # else:
# # # # # # # #     print('哈哈')
# # # # # # #
# # # # # # #
# # # # # # # name = "alex"
# # # # # # # print(id(name))     #内存地址
# # # # # # # name = 'jakc'
# # # # # # # print(id(name))     #内存地址
# # # # # # # #PYTHON 每隔一段时间会把没有和变量名关联的内存数据回收
# # # # # # #
# # # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # ######定义函数和return返回数值
# # # # # # # def maxmun(a,b):
# # # # # # #     if a>b :
# # # # # # #         return a
# # # # # # #     else:
# # # # # # #         return b
# # # # # # #
# # # # # # # print(maxmun(4,7))
# # # # # #
# # # # # # ####三元组，if else
# # # # # # # a = 4
# # # # # # # b = 7
# # # # # # # c = None
# # # # # # #
# # # # # # # c = a if a>b else b
# # # # # # # print(c)
# # # # # #
# # # # # # ##函数
# # # # # # # def func(a, b):
# # # # # # #     print(a * b)
# # # # # # # x=7
# # # # # # # y=8
# # # # # # # func(x,y)
# # # # # #
# # # # # # # def fuc(message,times=10):
# # # # # # #     print(message*times)
# # # # # # # fuc(5)
# # # # # # # fuc(5,8)
# # # # # # # fuc('abc',3)
# # # # # # #
# # # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # def  fuck(a,b=5,c=10):
# # # # # # #       print('a is' ,a , 'b is' ,b ,'c is' ,c,)
# # # # # # #
# # # # # # #
# # # # # # # fuck(3)
# # # # # # # fuck(4,b=10)
# # # # # # # fuck(a=20,b=10)
# # # # # # #
# # # # # # names = None
# # # # # # names = ['1', '3', '5', '7']
# # # # # # n2 = ['2', '3', 'a', 'b']
# # # # # # print(names)
# # # # # # print('显示names')
# # # # # # names.append('1')
# # # # # # print('append增加')
# # # # # # print(names)
# # # # # # names.insert(2, '2')
# # # # # # print('insert')
# # # # # # print(names)
# # # # # # names.extend(n2)
# # # # # # print('extend')
# # # # # # print(names)
# # # # # # del names[1]
# # # # # # print('del')
# # # # # # print(names)
# # # # # # names.pop()
# # # # # # print('pop')
# # # # # # print(names)
# # # # # # names.pop(0)
# # # # # # print('pop(0)')
# # # # # # print(names)
# # # # # # names[2] = 'C'
# # # # # # print('names[2]=a 序号2改成a')
# # # # # # print(names)
# # # # # # print('index 3查看3的序号')
# # # # # # print(names.index('3'))
# # # # # # print('判断2在names里')
# # # # # # print('2' in names)
# # # # # # names.remove('2')
# # # # # # print('remove 2,删除坐起第一个2')
# # # # # # names[0]='b'
# # # # # # print(names)
# # # # # #
# # # # # # print('切片')
# # # # # # print(names)
# # # # # # print(names[2:3])
# # # # # # print(names[1:])
# # # # # # print(names[:1])
# # # # # # print(names[1:5])
# # # # # # print(names[0:-1])
# # # # # # print(names[-2:-1])
# # # # # # print('-------')
# # # # # # print(names[-2])
# # # # # # print('-----')
# # # # # # print(names.index('a'))
# # # # # # print('-----    -5:-1')
# # # # # # print(names[-5:-1])
# # # # # # print('-----   -5:')
# # # # # # print(names[-5:])
# # # # # # print('步长为1')
# # # # # # print(names)
# # # # # # print(names[0:-1:1])
# # # # # # print('步长为2')
# # # # # # print(names)
# # # # # # print(names[0:-1:2])
# # # # # # print('步长为-1')#倒着切
# # # # # # print(names)
# # # # # # print(names[::-1])
# # # # # # print(names[-1:-5:-1])
# # # # # # print('反转')
# # # # # # names.reverse()
# # # # # # print(names)
# # # # # #
# # # # # # print('sort() 按字符表排序 askma')
# # # # # # names.sort()
# # # # # # print(names)
# # # # # # print('-------------')
# # # # # # print('打印出列表里的字符串')
# # # # # # for i in names:
# # # # # #     print(i)
# # # # # # print('-------------')
# # # # # #
# # # # # # print('names[]为可以增删改查的列表')
# # # # # # print('names()为只读列表')
# # # # # # print(len(names)
# # # # #
# # # # # #
# # # # # #
# # # # # # data = ('1','2',['a','b','c','d'],'4',5)
# # # # # # print(data)
# # # # # #
# # # # # # data[2][2]='4'
# # # # # # print(data)
# # # # # # print('type(data),type(data[0]),type(data[2]),type(data[-1])')
# # # # # # print(type(data),type(data[0]),type(data[2]),type(data[-1]))
# # # # #
# # # # #
#  s = 'My name is %s ， i am %s year old ' % ('liqi', 30)
#  print(s)
# # # # # # #
# # # # # # s1 = "My name is {A}, i am {B} year old "
# # # # # #
# # # # # # print(s1)
# # # # # #
# # # # # #
# # # # # # # print(s1.format(A="liq", B='30'))
# # # # # # {0}{1}.format(A='liqi',B='30')
# # # # # # print(s1)
# # # # #
# # # # #
#  print("{0} {1},{0}".format("hello", "world"))
# # # # # #
# # # # #
# # # # # #
# # # # # # # !/usr/bin/python
# # # # # # # -*- coding: UTF-8 -*-
# # # # # #
# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#
# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
#
# # 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# # # # # # dict = {'a':1,'b':2,'c':3}
# # # # # # print(dict)
# # # # # #
# # # # # # print(dict['b'])
# # # # # #
# # # # # # print(str(dict))
# # # # # #
# # # # # #
# # # # # # a= '10%'
# # # # # # print(type(a))
# # # # # #
# # # # # # print(dict.keys())
# # # # #
# # # import time
# # # ticks = time.time()
# # # print('shijian',ticks)
# # #
# # # ticks = time.localtime(time.time())
# # # print(ticks)
# # #
# # # ticks = time.asctime(time.localtime(time.time()))
# # # print(ticks)
# # #
# # # # # #
# # # # # # n = {'name':'Liqi','age':18,'job':'teacher'}
# # # # # # print(n)
# # # # # # n['name'] = 'Wuxuejing'
# # # # # # print(n)
# # # # # # n.setdefault('Chongwu','Chouyou')
# # # # # # print(n)
# # # # #
# # # # # a = [1,2,3,4,5]
# # # # # b = [2,4]
# # # # #
# # # # # both = []
# # # # #
# # # # # for i in a:
# # # # #     if i in b:
# # # # #         both.append(i)
# # # # #         print(both)
# # # #
# # # #
# # # # a = {1,2,3,4,5,3,4,5,'qw','qwq','dsfdf'}
# # # # print(a)
# # # # a = [1,2,3,4,5,3,4,5,'qw','qwq','dsfdf']
# # # # print(a)
# # # # print(set(a))
# # # # a = {1,2,3,4,5,3,4,5,'qw','qwq','dsfdf'}
# # # # a.add(9)
# # # # print(a)
# # # # a.discard(9)
# # # # print(a)
# # # # print(1 in a)
# # # #
# # # # for i in a :
# # # #     print(i)
# # #
# # #
# # #
# # #
# # #
# # # a = {1,2,3,4,5,'a','b','c','d','e'}
# # # b = {1,3,5,7,9,'a','c','e','f','h'}
# # # print('&')
# # # print(a & b)
# # #
# # # print('|')
# # # print(a|b)
# # #
# # # print('-')
# # # print(a-b)
# # # print(b-a)
# # #
# # # print('^对称差集')
# # # print(a^b)
# # #
# # # #相交
# # # print(a.isdisjoint(b))
# # # #子集
# # # print(a.issubset(b))
# # #
# # # print('dieeerence')
# # # print(a.difference(b))
# # # #交际
# # # print(a.intersection(b))
# # #
# #
# # #
# #
# # # !/usr/bin/python
# # # -*- coding: UTF-8 -*-
# #
# # # 定义函数
# # def printme(str):
# #     print('打印任何传入的字符串')
# #     str
# #     return
# #
# #
# # # 调用函数
# # printme("我要调用用户自定义函数!")
# # printme("再次调用同一函数")
# # printme('bo')
#
# def Numb(name, age):
#     print(name,age)
#     return
#
#
# Numb(name='Liqi', age=18)


# import os
# c = []
# c =[x for x in os.listdir(path='D:\\U盘备份1\\windows2000加固')]
#
# for i in c:
#     print(i)

# print('This is {name} ,  {age} old'.format(name='Liqi',age=30))
# print('this is %s , %s old'%('li qi',19))
#
# username = input('请输入用户名：')
# password = input('请输入密码：')
# U = open('User_pass.txt','r')
# U = U.readlines()
#
#
#
# for line in U:
#     line = line.split()
#     B = open('Blacklist.txt', 'r')
#     B = B.read()
#     B = B.split()
#     B = B.count(username)
#     if username == line[0] and password == line[1] and B <= 3:
#         print('登陆成功')
#         break
#     else:
#         print('登陆失败')
#         U = open('Blacklist.txt','a+')
#         U.write(username + ' ')
#         U.close()
#         break


# class people:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
#
#
# t = people()
# t.prt()


# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 实例化类
# # p = people('runoob', 10, 30)
# # p.speak()
#
#
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     def speak(self):
#         print('%s 说：我%d 岁 ，我上%s 年级' % (self.name, self.age, self.grade))
#
#
# c = student('li qi', 10, 60, 3)
# c.speak()


# x,y,z, 平均值为80， 三个数比例为  X =2Y = 3Z,求x,y,z

# for x in range(1,240):
#     for y in range(1,240):
#         for z in range(1,240):
#             if (x+y+z)/3 == 80 and x/y == 1/2 and x/z == 1/3:
#                 print(x,y,z)

# import hashlib
#
# hash = hashlib.md5()#md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
# hash.update(bytes('123akjhk',encoding='utf-8'))#要对哪个字符串进行加密，就放这里
# print(hash.hexdigest())#拿到加密字符串

# a = hashlib.md5("123123123".encode("utf-8"))
# print(a.hexdigest())


# 将r'C:\Program Files (x86)' 文件夹下所有的数据保存在列表 和文件夹中
# filename = []
# import os
#
# for root,dirs,files in os.walk(r'C:\Program Files (x86)'):
#     for name in files:
#         filename.append(os.path.join(root,name))
#
# c = open('filexxx.txt','a+')
# for i in filename:
#     c.write(i+'\r')

# 正则表达式

# line = 'cats are smarter than dogs'
# import re
# c = re.match('(.*) are(.*)',line)
# print('c',c)
# print(c.group())
# print(c.group(1))
# print(c.group(2))

# import re

# phone = "2004-959-559 # 这是一个电话号码"
# id = " 188882312365290119890502001X123123 "
#
# print('电话号码：', re.sub('#.*','',phone))   # re.sub 是替换
# print('电话号码：', re.sub('\D','',phone))  # \D 是所有非数字和字母
#
# print(pattern.findall(id))


# 用正则表达式 提取小说链接 标题 作者

# def wrt(text):
#     with open('111111111111.txt', 'ab') as f:
#         f.write(text + '\n'.encode('utf-8'))
#         print('写入完成')
#
#
# import requests
# from lxml import etree
#
# url = 'http://www.4xiaoshuo.com/48/347/'
# url_list = []
# page = requests.get(url).content.decode('utf-8')
# print(type(page))
#
# lis = '<a href ="(.*?)"(.*?)</a>'
# link = re.findall(lis, page, re.S)
# for i in link:
#     a,b = i
#     href_list = ('http://www.4xiaoshuo.com/48/347/'+a)
#     wrt(href_list.encode('utf-8')+' '.encode('utf-8')+b.encode('utf-8'))
#
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
# "referer": "http://www.4xiaoshuo.com"
# }


# import lxml

# xfpage = lxml.etree.HTML(fpage).xpath('//div')
# for i in xfpage:
#     # 'get', 'has_key', 'items', 'iteri# session = requests.Session()
# #
# #
# # furl = 'http://www.4xiaoshuo.com/48/347/33828957.html'
# # fpage = session.get(furl,headers=headers).text
# # print(fpage)tems', 'iterkeys', 'itervalues', 'keys', 'pop', 'update', 'values'
#     # print(dir(i.attrib))
#     print(i)


#
#
# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))


# import re
#
# # pattern = re.compile('[^a-z]+')
# # m = pattern.search('sdfsdfsdf234234wefr23432df234324')
# # print(m.group() + 'b')
#
# s = '2019-10-25'
# print(re.sub('(\d+)-(\d+)-(\d+)', r'\2/\3/\1/', s))
#

# import re
#
# ret = re.findall('o\\b', 'hello nano$')
# print(ret)
# ret = re.findall('o', 'hello nano$')
# print(ret)


# c = 'hh2jhj44khh44jack4dad'
#
# ret = re.split('[\D]', c)
# print(ret)
# ret = re.split('[a-z]', c)
# print(ret)
#
# ret = re.findall('[0-9]', c)
# print(ret)
#
#
#
# s = '9-2*5/3+7/3*99/4*2998+10*568/14'
#
#

# import time
#
# print(time.strftime('%Y-%m-%d %H-%M-%S'))
# print('time.ctime():    ',time.ctime())
#
#
# import datetime
# print('datetime.datetime.now():   ',datetime.datetime.now())
# print('datetime.datetime.today(): ',datetime.datetime.today())
# print('datetime.datetime.today(): ',datetime.datetime.fromtimestamp(time.time()))


# import mysql.connector

# 连接数据库
# mydb = mysql.connector.connect(host='localhost', user='root', passwd='123456', database='lq')
# 数据库把位置复制给mycursor
# mycursor = mydb.cursor()
# 创建一个数据库,已经创建过的库在创建会报错
# mycursor.execute('CREATE DATABASE wuxuejing_db')

# 显示所有数据库

# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)

# 进入一个数据库
# 创建一个数据表,已经创建过的库在创建会报错
# mycursor.execute('create table sites (name varchar(255),url varchar(255))')

# 显示所有表
# mycursor.execute('show tables')
# for i in mycursor:
#     print(i)

# 主键设置
# 创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY"
# 语句来创建一个主键，主键起始值为 1，逐步递增。
# 如果我们的表已经创建，我们需要使用 ALTER TABLE 来给表添加主键：
# mycursor.execute('use lq')
# mycursor.execute('create table stites1(ID INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),url VARCHAR(255))')

# 插入一个数据
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="123456",
#     database="lq"
#     )
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
# # 更新数据库
# mydb.commit()
# print(mycursor.rowcount,'记录插入成功')
# mycursor.execute('SELECT * FROM family')
# for i in mycursor:
#     print('select * from family:',i)
#
# mycursor.execute('show tables')
# for i in mycursor:
#     print('show tables:',i)
#
# mycursor.execute('select database()')
# for i in mycursor:
#     print('select database()',i)
#
# mycursor.execute('show databases')
# for i in mycursor:
#     print('show databases',i)

# mycursor.execute('ALTER TABLE family ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
# mycursor.execute('select * from family')
# for i in mycursor:
#     print('new tables', i)


# # 加入多行数据
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="123456",
#     database="lq"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO family (name,age,sex) VALUES(%s,%s,%s)"
# val = [('李麒', 30,'m'),('吴雪婧', 30,'w'),('臭鼬', 30,'w')]
# mycursor.executemany(sql,val)
# mydb.commit()
# mycursor.execute('select * from family')
# for i in mycursor:
#     print(i)


import re

# [SSH-TELNET-login-fail]
# ^<\d+>\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d+\s+(?<sw_name>\S+)\s+.+LOGINFAIL+\S+\s+\S+\s+\S+\s+(?<user>\S+)\sfailed .+from\s+(?<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).+$
# <4> ${#time} ${sw_name} SW 0 5 ${user} ${login_ip}
# a = "2019-10-30 17:43:53 USG2110 %%01SHELL/4/LOGINFAIL(l): User login failed from con0(times=1)."
# b = "2019-10-30 17:57:32 USG2110 %%01HTTPD/4/FAIL(l): User admin(IP:192.168.100.249 ID:321) login failed"

# cpu
# b = "Sep 16 21:44:24 192.168.0.1 2020-09-16 22:00:49 USG2110 %%01SYSTATE/6/HEALTH(l): CPU Usage=2% Memory Usage=62%"
# cpu = re.findall('.*?-\d+-\d+\s+\d+:\d+:\d+\s+(?P<sw_nme>\S+).*CPU\s+Usage=(?P<CPU>\d+)%.*',b)
# Memory = re.findall('.*?-\d+-\d+\s+\d+:\d+:\d+\s+(?P<sw_nme>\S+).*Memory Usage=(?P<Memory>\S+)%',b)
# mess = "2020-09-16 22:01:53 USG2110 %%01SHELL/5/CMDRECORD(l): task:HTPR ip:192.168.0.3 user:gwadmin vrf:public command:undo info-center loghost source."
# mess_re = re.findall('^\S+.*?-\d+-\d+\s+\d+:\d+:\d+\s+(?P<sw_nme>\S+).*?ip:(?P<ip>\S+)\s+user:(?P<login_name>\S+)\s+.*command:(?P<command>.*?)\.',mess)
# print('mess_re',mess_re)
# print('cpu',cpu)
# print('Memory',Memory)


# time = re.findall('^\d+\S\d+\S\d+\s\d+\S\d+\S\d+\s(?<=:\d{2}\s)\w+',b)
# print(time)
# sw_name = re.findall('(?<=:\d{2}\s)\w+',b)
# print(sw_name)
# user = re.findall('(?<=User\s)\w+',b)
# print(user)
# login_ip = re.findall('(?<=IP:)\w+.\w+.\w+.\w+',b)
# print(login_ip)


# test = re.search('(?P<login_ip>\d+\.\d+\.\d+\.\d+)',b)
# print(test.groupdict())

# '^\d+\S\d+\S\d+\s\d+\S\d+\S\d+\s(?<=:\d{2}\s)\w+(?<sw_name>\S+)(?<=:\d{2}\s)\w+(?<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+UserName=(?<user>\S+),.+$


# 创建一个窗口
# import wx
#
# app = wx.App()
# # 设置标题,设置大小
# win = wx.Frame(None,title='我的记事本',size=(410,335))
# # 创建Button,设置位置，设置大小
# loadButton = wx.Button(win,label='open',pos=(225,5),size=(80,25))
# saveButton = wx.Button(win,label='save',pos = (310,5),size =(80,25))
#
# filesname = wx.TextCtrl(win,pos=(5,5),size=(210,25))
# contents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE |wx.HSCROLL)
# win.Show()
# # 进入应用程序主时间循环
# app.MainLoop()

# 组建布局

# import wx

# app = wx.App()
# win = wx.Frame(None,title="我的记事本",size=(410,335)) #创建一个单独的窗口
# bkg = wx.Panel(win)
#
# #创建组件
# loadButton = wx.Button(bkg,label="Open")
# saveButton = wx.Button(bkg,label="Save")
# filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)
#
# #布局容器
# hbox=wx.BoxSizer() #默认水平布局
# hbox.Add(filename,proportion=1,flag=wx.EXPAND)
# hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
# hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
#
# #布局容器
# vbox=wx.BoxSizer(wx.VERTICAL) #垂直布局
# vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
# vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=50)
#
# bkg.SetSizer(vbox)
#
# win.Show()
# app.MainLoop() #进入应用程序事件主循环
#
#

# 为按钮添加事件
# import wx
#
#
# def load(event):
#     """加载文件内容"""
#     file = open(filename.GetValue(), 'r')
#     contents.SetValue(file.read())
#     file.close()
#
#
# def save(event):
#     """保持文件内容"""
#     file = open(filename.GetValue(), 'w')
#     file.write(contents.GetValue())
#     file.close()
#
#
# app = wx.App
# import os
#
# # print(os.getcwd())
# # print(os.listdir())
# print(os.stat('test.py'))
#
# import time
#
# print(os.sep)
# print(os.path.abspath('test.py'))
# print(os.path.split(os.path.abspath('test.py')))
# print(os.path.split(os.path.abspath('test.py')))
#
# a = "C:\\Users\\Administrator\\PycharmProjects"
# b = "untitled\\venv\Scripts\\python.exe"
#
#
# print(a + b)
# # 组合路径
# print(os.path.join(a,b))
# # 上一次访问时间戳
# print(os.path.getatime('test.py'))
# # 上一次修改时间戳
# print(os.path.getmtime('test.py'))
# # 创建文件时间戳
# print(os.path.getctime('test.py'))


# from sys import argv
# a = argv
# for i in argv[2:]:
#     print(i,end=' ')


#
# b = []
# m = int(input('输入查询的人数：'))
# x = m
# n = str(input('输入每个分数')).split(' ')
# if m >= len(n):
#     m = len(n)
# else:
#     pass
# while m > 1:
#     for i in n[0:x]:
#         b.append(int(i))
#         m -= 1
#
# b.sort()
# print(x)
# for i in b:
#   print(i,end=' ')


# import requests
#
# url = 'https://www.cnblogs.com/wupeiqi/articles/6229292.html'
#
# response = requests.get(url=url)
#
# with open('python.html','wb') as f:
#     f.write(response.content)


# 加入多行数据
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="123456",
#     database="lq"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO messgram (name,age,sex) VALUES(%s,%s,%s)"
# val = [('李麒', 30,'m'),('吴雪婧', 30,'w'),('臭鼬', 30,'w')]
# mycursor.executemany(sql,val)
# mydb.commit()
# mycursor.execute('select * from messgram')
# for i in mycursor:
#     print(i)


# import re
# m = re.match("(..)", "a1b2c3")
#
# print(m.group())
# print(m.groups())
# print('----------')
# print(m.group(0))
# print(m.groups(0))
# print('----------')
# print(m.group(1))
# print(m.groups(1))
#


#  一个类下面的方法如果有   @classmethod    那么这个类实例化的时候会直接运行  __init__
# class task:
#     def __init__(self):
#         print('执行这个类')
#
#     @classmethod
#     def open(cls):
#         print('执行open')
#         return cls()
#
#     def close(self):
#         print('close')
#
# task()
# print('___________')
# task.open()
# print('___________')
# c =task()


# 线程

# import threading
# import time
#
#
# def Hi():
#     print('Hello %s'%time.ctime())
#     time.sleep(3)
#     print('stop Hello %s'%time.ctime())
#
#
# def game():
#     print('love game %s'%time.ctime())
#     time.sleep(5)
#     print('stop love %s'%time.ctime())
#
#
# if __name__ == '__main__':
#     s1 = threading.Thread(target=Hi)
#     s2 = threading.Thread(target=game)
#     s1.start()
#     s2.setDaemon(True) # 此线程和主线程一起结束，不用等是否完成
#     s2.start()
#
#     s1.join() # 等着s1运行完在打印
#
#
#     print('ending____________')


# import os
# import sys
# import re

# a = '%Jan  2 05:56:23:694 2013 SW-1 SHELL/5/SHELL_LOGIN: xjdl logged in from 172.20.99.241.'
#
# c = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}:\d{3}\s+\d+\s+(?P<sw_name>\S+).+LOGIN:\s+(?P<user>\S+).+from\s+('
#               r'?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+$', a)
#
#
# print(c.groups())
#
# usg = 'Dec 13 2019 18:56:09 USG6300 %%01SHELL/5/CMDRECORD(s)[536]:Recorded command information. (Task=HTPR, Ip=192.168.100.249, VpnName=, User=FXML-ADMIN, AuthenticationMethod="Null", Command="acl 3000")'
#
# usg_mess = re.search(r'\S+\s+\d+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+)\s+.+CMDRECORD.+Ip=.+User=(?P<user>\S+),.+Command="(?P<command>.+)".+$', usg)
#
# print(usg_mess.groups())

# import re
# # ssh 登录失败
# g1='Jan  2 05:58:58 2013 SW-1 %%SSHS/6/SSHS_LOG: Authentication failed for user xjdl from 172.20.99.241 port 17601 because of invalid username or wrong password.'
#
# g2='Jan 10 17:35:49 2020 wangkongshi %%10SHELL/5/SHELL_LOGINFAIL(l): SSH user xjdl failed to log in from 192.168.10.20 on VTY0.. '
# # [SSH-TELNET-login-fail]
# s5130_fail = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOG:\s+\S+\s+\S+\s+\S+\s+\S+\s+(?P<user>\S+)\s+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).+$',g1)
# s5130_fail2 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOG\S+:\s+SSH user\s+(?P<user>\S+)\s+failed.+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).+$',g2)
# print('login-fail:',s5130_fail.groups())
# print('login-fail:',s5130_fail2.groups())
# #
# import re
# # ssh 登录成功
# c1='Jan  2 05:56:23 2013 SW-1 %%SHELL/5/SHELL_LOGIN: xjdl logged in from 172.20.99.241.'
# c2='Jan 10 17:30:50 2020 wangkongshi %%10SHELL/5/SHELL_LOGIN(l): xjdl logged in from 127.0.0.1.'
# # [SSH-TELNET-login]
# s5130_login = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGIN:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).$',c2)
# print('login:',s5130_login.groups())


# # ssh 登录成功
# c1='Jan  2 05:56:23 2013 SW-1 %%SHELL/5/SHELL_LOGIN: xjdl logged in from 172.20.99.241.'
# c2='Jan 10 17:30:50 2020 wangkongshi %%10SHELL/5/SHELL_LOGIN(l): xjdl logged in from 127.0.0.1.'
# # [SSH-TELNET-login]
# s5130_login = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGIN\S+\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).$',c2)
# print('login:',s5130_login.groups())


# [SSH-TELNET-logout]
# # ssh 退出成功
# e1='Jan  2 05:57:43 2013 SW-1 %%SHELL/5/SHELL_LOGOUT: xjdl logged out from 172.20.99.241.'
# e2 ='Jan 10 17:33:37 2020 wangkongshi %%10SHELL/5/SHELL_LOGOUT(l): xjdl logged out from 127.0.0.1.'
# s5130_logout1 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGOUT:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).$',e1)
# s5130_logout2 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOG\S+:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).$',e2)
# print('logout:',s5130_logout1.groups())
# print('logout:',s5130_logout2.groups())


# 输入命令回显
# a1='Dec 17 13:15:38 2019 SW-1 %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=**; Command is sys'
# a2='Dec 17 13:15:41 2019 sw %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=**; Command is undo snmp-agent'
# # [SSH-TELNET-operate-command]
# s5130_fail1 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL\S+\s+.+IPAddr=(?P<login>\S+)-User=(?P<user>\S+);\s+Command\s+is\s+(?P<command>.+)$',a1)
# s5130_fail2= re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL\S+\s+.+IPAddr=(?P<login>\S+)-User=(?P<user>\S+);\s+Command\s+is\s+(?P<command>.+)$',a2)
# print('command:',s5130_fail1.groups())
# print('command:',s5130_fail2.groups())

#
# # # console 登陆失败
# g3 = 'Dec 17 16:49:54 2019 sw %%10LOGIN/5/LOGIN_FAILED: a failed to log in from aux0.'
# g4 = 'Jan 10 17:17:23 2020 wangkongshi %%10SHELL/5/SHELL_LOGINFAIL(l):  AUX user failed to log in on AUX0.'
# s5130_con_fail =re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).+LOGIN_FAILED:\s+.+from\s+(?P<user>\S+).+$',g3)
# s5130_con_fail4 =re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).+LOG\S+:\s+AUX user.+on\s+(?P<user>\S+).+$',g4)
# print(s5130_con_fail.groups())
# print(s5130_con_fail4.groups())
#
#
# # console 登陆成功)
# g4 = 'Dec 17 17:03:30 2019 sw %%10SHELL/5/SHELL_LOGIN: aaa logged in from aux0.'
# g5 = 'Jan 10 17:17:33 2020 wangkongshi %%10SHELL/5/SHELL_LOGIN(l): Console logged in from aux0.'
# s5130_con_login = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGIN:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\S+).$',g4)
# s5130_con_login5 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGIN\S+:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\S+).$',g5)
# print('con_login:',s5130_con_login.groups())
# print('con_login:',s5130_con_login5.groups())

# # console 退出
#
# g5 = 'Dec 17 17:07:02 2019 sw %%10SHELL/5/SHELL_LOGOUT: aaa logged out from aux0.'
# g6 = 'Jan 10 17:17:22 2020 wangkongshi %%10SHELL/5/SHELL_LOGOUT(l): Console logged out from aux0.'
# s5130_con_logout = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOGOUT:\s+(?P<user>\S+).+$',g5)
# s5130_con_logout6 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+LOG\S+:\s+.+from\s+(?P<user>\S+).+$',g6)
# print('con_logout',s5130_con_logout.groups())
# print('con_logout',s5130_con_logout6.groups())


# # console command
# g6 = 'Dec 17 17:07:02 2019 sw %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=aaa; Command is quit'
# g7 = 'Jan 10 17:16:40 2020 wangkongshi %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=**; Command is info-center loghost 192.168.10.100'
# s5130_con_com = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+Command\s+is\s+(?P<command>.+)$',g6)
# s5130_con_com7 = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+Command\s+is\s+(?P<command>.+)$',g7)
# print('con_command:',s5130_con_com.groups())
# print('con_command:',s5130_con_com7.groups())
# #
# #
# # console command password
# g7 = 'Dec 17 18:27:14 2019 sw %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=aaa; Command is password simple ******'
# s5130_con_passwd = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+User=(?P<User>\S+);\s+Command\s+is\s+password\s+simple.+$',g7)
# print('con passwd:',s5130_con_passwd.groups())

# ssh passwd
# g8 = 'Dec 17 17:30:57 2019 sw %%10SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=222.111.112.248-User=aaa; Command is password simple ******'
# s5130_ssh_passwd = re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+IPAddr=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<User>\S+);\s+Command\s+is\s+password\s+simple\s+.+$',g8)
# print(s5130_ssh_passwd.groups())

#
# g9 = 'Dec 17 18:05:37 2019 sw %%10SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=222.111.112.248-User=aaa; Command is dis current-configuration'
# s5130_fail2= re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL\S+\s+.+IPAddr=(?P<login>\S+)-User=(?P<user>\S+);\s+Command\s+is\s+(?P<command>.+)$',g9)
#
# print('command:',s5130_fail2.groups())

# g10 = 'Dec 17 18:40:09 2019 sw %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=aaa; Command is qu'
# print(re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+Command\s+is\s+(?P<command>.+)$',g10).groups())


# ssh command
# g11 = 'Dec 17 18:51:07 2019 sw %%10SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=222.111.112.248-User=aaa; Command is dis current-configuration'
# print('g11',re.search(r'^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL\S+\s+.+IPAddr=(?P<login>\S+)-User=(?P<user>\S+);\s+Command\s+is\s+(?P<command>.+).+$',g11).groups())


# # web登陆防火墙
# u1 = 'Dec 18 2019 12:08:57 USG6300 %%01HTTPD/6/PASS(l)[28086]:User FXML-ADMIN(IP:192.168.50.249 ID:418) login succeeded'
# print('login:', re.search(r'^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+login\s+succeeded$', u1).groups())
# # web退出登陆
# u2 = 'Dec 18 2019 12:07:25 USG6300 %%01HTTPD/5/OUT(l)[28084]:User FXML-ADMIN(IP:192.168.50.249 ID:412) logout'
# print('logout:',re.search(r'^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+logout$',u2).groups())
# # web登陆失败
# u3 = 'Dec 18 2019 12:00:06 USG6300 %%01HTTPD/5/FAIL(l)[28050]:User FXML-ADMIN(IP:192.168.50.249 ID:410) login failed'
# print('logout:',re.search(r'^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+failed$',u3).groups())
# # web修改防火墙策略
# u4 = 'Dec 18 2019 12:40:21 USG6300 %%01SHELL/5/CMDRECORD(s)[28308]:Recorded command information. (Task=HTPR, Ip=192.168.50.249, VpnName=, User=FXML-ADMIN, AuthenticationMethod="Null", Command="save")'
# u5 = 'Dec 18 2019 17:38:16 ZBS-TQYB-FIREWALL %%01SHELL/5/CMDRECORD(s)[30067]:Recorded command information. (Task=HTPR, Ip=192.168.0.3, VpnName=, User=ZBS-ADMIN, AuthenticationMethod="Null", Command="undo rule name 123")'
# u6 = 'Dec 18 2019 18:24:19 ZBS-TQYB-FIREWALL %%01SHELL/5/CMDRECORD(s)[30259]:Recorded command information. (Task=HTPR, Ip=192.168.0.2, VpnName=, User=ZBS-ADMIN, AuthenticationMethod="Null", Command="security-policy")'
#
# # print('rule:',re.search(r'^\S+.+Ip=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+.+User=(?P<user_name>\S+),\s+.+$',u4).groups())
# print('rule:',re.search(r'^\S+.+Ip=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+.+User=(?P<user_name>\S+),\s+.+\s+Command="(?P<command>.+)"\)$',u6).groups())
#
#
# # aa = re.search(r'^\S+\s\d+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\S+\s+.+Ip=(?P<user_name>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+\S+,\s+User=(?P<user_namelogin_ip>\S+),\s+.+$',u6).groups()
# # print(aa)
#
#
#
# mess = 'ZBS-ADMIN 192.168.0.2 hkj'
# mess1 = 'ZBS-ADMIN 192.168.0.2 security-policy'
# print(re.search(r'^(?P<mdf_info>(?P<user_name>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+)$',mess1).group())


# # 网神防火墙登陆成功
# login =r'Dec 18 15:26:57 10.50.10.45 WEBUI-登录: admin\0xd3\0xc3\0xbb\0xa7\0xb5\0xc7\0xc2\0xbc\0xb3\0xc9\0xb9\0xa6'
# # ^(?<login_info>(?<user_name>\S+)\s+(?<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))$'
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>\S+)\\0xd3\\0xc3.+',login).groups())
# mess = 'admin 10.50.10.45'
# print('网神防火墙登陆成功',re.search('^(?P<login_info>(?P<user_name>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))$',mess).group())

# # 网神防火墙登陆失败
# logfail = 'Dec 18 15:46:07 10.50.10.45 WEBUI-登录: admin用户登录失败，用户名或密码不正确'
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>[a-zA-Z0-9_-]{1,8})+.+$',logfail).groups())
# print(re.search('^(?P<login_info>(?P<user_name>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))$',mess).group())

# 网神防火墙登陆退出
# logout = 'Dec 18 15:26:53 10.50.10.45 WEBUI-登录: admin用户成功退出管理系统'
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>\S+)用户成功退出管理系统$',logout).groups())
# print(re.search('^(?P<login_info>(?P<user_name>\S+)\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$',mess).group())

# # # 网神防火墙修改策略
# # rule  = 'Dec 18 15:26:50 10.50.10.45 WEBUI: Config log server successfully.'
# rule1 = 'Dec 18 15:17:38 10.50.10.45 WEBUI: Send signal to system log pid  successfully.'
# rule2 = 'Dec 19 00:50:47 10.50.10.45 WEBUI-访问控制: 成功添加或编辑一条访问控制规则'
# # # ^(?<mdf_info>(?<user_name>\S+)\s+(?<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+)$
# mess1 = 'WEBUI 10.50.10.45 Send signal to system log pid  successfully'
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<user_name>\S+):\s+(?P<command>.+).+$',rule1).groups())
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<user_name>\S+):\s+(?P<command>.+).+$',rule2).groups())
# # print(re.search('^(?P<mdf_info>(?P<user_name>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+)$',mess1).group())

# 网神防火墙阻断数据
# deny1 ='ec 19 01:00:15 192.168.50.100 FW-ACCESS: 0 2019-12-19 01:00:15 198.120.0.187 TCP 198.120.0.187 58496 198.120.0.198 6000 ACCEPT 198.120.0.187 58496 198.120.0.198 6000 Normal\0x0a'
# deny2 ='Dec 18 15:46:10 10.50.10.45 FW-ACCESS: 0 2019-12-18 15:46:10 198.121.0.60 UDP 198.121.0.60 6002 198.121.255.255 6001 REJECT 0.0.0.0 0 0.0.0.0 0 Normal'
# deny3 ='Dec 18 15:34:01 10.50.10.45 FW-ACCESS: 0 2019-12-18 15:34:01 198.120.0.186 UDP 198.120.0.186 6002 198.120.255.255 6001 REJECT 0.0.0.0 0 0.0.0.0 0 Normal'
# deny4 ='Dec 18 15:34:02 10.50.10.45 FW-ACCESS: 0 2019-12-18 15:34:02 admin TCP 10.50.10.44 6639 42.236.9.57 80 REJECT 0.0.0.0 0 0.0.0.0 0 Normal\0x0a'
# #
# print(re.search('\S+.+TCP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',deny1).groups())
# print(re.search('\S+.+UDP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',deny2).groups())
# print(re.search('\S+.+UDP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',deny3).groups())
# print(re.search('\S+.+TCP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',deny4).groups())
#
# mess2 = 'REJECT 10.50.10.44 6953 111.206.63.22 80'
# print(re.search('^(?P<quintet>\S+\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5}\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5})$',mess2).group())


# # # 网神防火墙运行通过数据
# accept = 'Dec 18 15:46:10 10.50.10.45 FW-ACCESS: 0 2019-12-18 15:46:10 198.120.0.60 UDP 198.120.0.60 6002 198.120.255.255 6001 ACCEPT 198.120.0.60 6002 198.120.255.255 6001 Normal'
# accept1 = 'Dec 18 15:34:48 10.50.10.45 FW-ACCESS: 0 2019-12-18 15:34:48 198.120.0.200 TCP 198.120.0.200 3100 198.120.0.187 9500 ACCEPT 198.120.0.200 3100 198.120.0.187 9500 Normal'
#
# print(re.search('\S+.+UDP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',accept).groups())
# print(re.search('\S+.+TCP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$',accept1).groups())
# mess2 = 'ACCEPT 198.120.0.60 6002 198.120.255.255 6001'
# print(re.search('',mess2))


# a11 =r'Dec 19 02:03:50 192.168.50.100 FW-ACCESS: 1 2019-12-19 02:03:50 198.120.0.59 UDP 198.120.0.59 6002 198.120.255.255 6001 ACCEPT 198.120.0.59 6002 198.120.255.255 6001 Normal\0x0a'
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>\S+).+$',a11).groups())

# b'\xd3\xc3\xbb\xa7\xb3\xc9\xb9\xa6\xcd\xcb\xb3\xf6\xb9\xdc\xc0\xed\xcf\xb5\xcd\xb3'  用户成功退出管理系统
# b'\xd3\xc3\xbb\xa7\xb5\xc7\xc2\xbc\xb3\xc9\xb9\xa6' '用户登录成功'
# b'\xb5\xc7\xc2\xbc'                             '登录'
# b'\xd3\xc3\xbb\xa7\xb5\xc7\xc2\xbc\xca\xa7\xb0\xdc\xa3\xac\xd3\xc3\xbb\xa7\xc3\xfb\xbb\xf2\xc3\xdc\xc2\xeb\xb2\xbb\xd5\xfd\xc8\xb7' '用户登录失败，用户名或密码不正确'
# b = '用户登录失败，用户名或密码不正确'
#
# print(b.encode('gbk'))


# import re

# login = 'id=SecGate3600 time="2019-12-19 12:21:36" fw=10.50.10.45 pri=5 type=mgmt mu=WEBUI-登录 op="exec command" result=successed msg="admin用户登录成功"'
# logout = 'id=SecGate3600 time="2019-12-19 12:21:47" fw=10.50.10.45 pri=5 type=mgmt mu=WEBUI-登录 op="exec command" result=successed msg="admin用户成功退出管理系统"'
# logfail = 'id=SecGate3600 time="2019-12-19 12:21:31" fw=10.50.10.45 pri=5 type=mgmt mu=WEBUI-登录 op="exec command" result=failed msg="admin用户登录失败，用户名或密码不正确"'
# rule = 'id=SecGate3600 time="2019-12-19 12:16:05" fw=192.168.50.100 pri=5 type=mgmt mu=WEBUI op="exec command" result=successed msg="Config log server successfully."'

# a = 'id=SecGate3600 time="2019-12-19 12:16:05" fw=192.168.50.100 pri=5 type=mgmt mu=WEBUI op="exec command" result=successed msg="Config log server successfully."'

# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+pri.+mu=WEBUI-\S+\s+.+result=successed msg="(?P<user_name>\S{5}).+$',login).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+mu=(?P<user_name>\S{5})\s+op.+msg="(?P<command>.+)"',rule).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+result=successed msg="(?P<user_name>\S{5}).+$',logout).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+result=successed msg="(?P<user_name>\S{5}).+$',logfail).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+result=successed msg="(?P<user_name>\S{5}).+$',rule).groups())
# ^(?<login_info>(?<user_name>\S+)\s+(?<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))$
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+result=successed msg="(?P<user_name>\S{5}).+$',login).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+result=failed msg="(?P<user_name>\S{5}).+$',logfail).groups())
# print(re.search('^\S+\s+time="\d+-\d+-\d+\s+\d+:\d+:\d+"\s+fw=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+mu=(?P<user_name>\S{1,5})\s+op.+msg="(?P<command>.+)"',a).groups())

#
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>\S....).+xb3$',logout).groups())
# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+(?P<user_name>\S....).+xb7$',logfail).groups())

# print(re.search('^\S+\s+\S+\s+\d{2}:\d{2}:\d{2}\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<user_name>\S+):\s+(?P<command>.+).+!$',login).groups())

# udp_reject = 'id=SecGate3600 time="2019-12-19 14:24:08" fw=10.50.10.45 pri=6 type=firewall src=198.120.0.182 dst=198.120.255.255 proto=UDP group=defaultgroup user=198.120.0.182 result=REJECT sport=9801 dport=9802 commtype=Normal'
# tcp_reject = 'id=SecGate3600 time="2019-12-19 14:24:18" fw=10.50.10.45 pri=6 type=firewall src=198.120.0.201 dst=198.120.0.187 proto=TCP group=defaultgroup user=198.120.0.201 result=REJECT sport=4767 dport=9500 commtype=Normal'
# # \S+.+TCP\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<src_port>\d{1,5})\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<dst_port>\d{1,5})\s+(?P<rule>\S+)\s+.+$
# print(re.search('^id=(?P<user_name>\S+)\s+.+pri=6\s+.+src=(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+dst=(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.+result=REJECT\s+sport=(?P<src_port>.+)\s+dport=(?P<dst_port>.+)\scommtype=Normal$',tcp_reject).groups())


# a = 'ADMIN 198.120.0.182 9801 198.120.255.255 9802'
# print(re.search('^(?P<quintet>\S+\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5}\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5})$',a).group())

#
# import  re
# down = 'Jan  1 01:59:10 2013 H3C %%10IFNET/3/PHY_UPDOWN: Physical state on the interface GigabitEthernet1/0/1 changed to down.\0x00'
# up =  'Jan  1 02:01:55 2013 H3C %%10IFNET/3/PHY_UPDOWN: Physical state on the interface GigabitEthernet1/0/1 changed to up.\0x00'
# print(re.match('^\S+\s+\d+\s+\d+:\d+:\d+\s+\d+\s+\S+\s+\S+PHY_UPDOWN:\s+Physical state on the\s+(?P<port>.+)\s+changed to down.+$',down).groups())
# print(re.search('^\S+\s+\d+\s+\d+:\d+:\d+\s+\d+\s+\S+\s+\S+PHY_UPDOWN:\s+Physical state on the\s+(?P<port>.+)\s+changed to up.+$',up).groups())


# import  re
# down = 'Jan 10 17:17:02 2020 wangkongshi %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/1 link status is DOWN.'
# up = 'Jan 10 17:17:04 2020 wangkongshi %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/1 link status is UP.'
# print(re.search('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+LINK\S+\s+(?P<port>\S+)\s+.+is\s+DOWN.+$',down).groups())
# print(re.search('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+LINK\S+\s+(?P<port>\S+)\s+.+is\s+UP.+$',up).groups())
#
# # inter = 'interface GigabitEthernet1/0/1'
#
# print(re.search('^(?P<if_name>.+)$',inter).group())

# s5130 网口up-down
# up = 'Jan  2 21:54:39 2013 ZhanKomg_A1 %%10IFNET/5/LINK_UPDOWN: Line protocol state on the interface GigabitEthernet1/0/24 changed to up.'
# down = 'Jan  2 21:54:37 2013 ZhanKomg_A1 %%10IFNET/5/LINK_UPDOWN: Line protocol state on the interface GigabitEthernet1/0/22 changed to down.'
# print(re.search('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>\S+).*?LINK_UPDOWN.*?the\s+(?P<int_port>\S+\s+\S+).*?down',down).groups())
# print(re.search('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>\S+).*?LINK_UPDOWN.*?the\s+(?P<int_port>\S+\s+\S+).*?up',up).groups())

# # 三目运算符
# a = 5
# b = 4
#
# resturt = (a+b) if a > b else (a - b)
#
# print(resturt)

# 9*9 乘法表
# for i in range(1, 10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j,end='\t')
#     print()


# import random
# print(random.choice([1,2,3,4,5]))


# a = [1,2,3,4,5,6,7]
# print(max(a))


# t1 = (1,3,4,6,7,8,9,0)
#
# a, *_, c =t1
# b,d,*_ = t1
# print(a,c,_)
# print(b,d,_)


# # 闭包
#
#
# def func():
#     a = 100
#
#     def inner():
#         b = 50
#         print(a,b)
#
#     return inner
#
# func()()
#
# # 闭包


# def func(a,b):
#     c = 100
#
#     def inner():
#         s = a + b + c
#         return s
#
#     return inner
#
# x = func(100,100)
# y = func(200,200)
# print(x)
# print(y)
# print(x())
# print(y())
# print(func(100,100))
# print(func(200,200))

# 装饰器,传递一个函数
#
# def decorate(func):
#     def inner1():
#         print('---------> inner1')
#         func()
#     def inner2():
#         inner1()
#         print('---------> inner2')
#
#     return inner2
#
# @decorate
# def house():
#     print('引用装饰器')
#
#
# house()


# a = [2, 3, 5, 7, 8, 5, 3, 2, 7, 8, 5, 4, 2]
# a = map(lambda x: x + 2, a)
# print(list(a))
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = map(lambda x: x if x % 2 else x - x, b)
# print(list(result))

# from functools import reduce
#
# a = [1,2,3,4,5,6,7,8,9]
# result = reduce(lambda x,y:x+y,a)
# print(result)
#
# num = filter(lambda x:x<5,a)
# print(list(num))


# # 字典生成式
# dict1 = {'a':'A','b':'B','c':'C','d':'D'}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict2)

# a = [1,2,3,4,5,6,7,8,9]
# a1 = [x+1 for x in a]
# print(a1)

# a2 = (x+1 for x in range(10))
# print(a2.__next__())
# print(a2.__next__())
# print(next(a2))
# print(next(a2))


# # 生成器写斐波那契数列
# def func():
#     a = 0
#     b = 1
#     while b < 100:
#         a,b = b, b+a
#         yield b
#
#
# g = func()
# print(g.__next__())
# print(next(g))
# print('----------')
# # 打印方法1
# for i in g:
#     print(i)


#
# def gen():
#     i = 0
#     while i <5:
#         temp = yield i
#         print('temp:',temp)
#         i +=1
#     return '没有更多的数据'
#
# g = gen()
#
# ### print(g.__next__())
# g.send(None)
# g.send('haha')
# print(next(g))
# g.send('hehe')
# print(next(g))


# 生成器 多任务进行  yield   协程
#
# def game(i):
#     for x in range(1,i):
#         print('正在打第%d游戏'%x)
#         yield None
#
#
# def music(i):
#     for x in range(1,i):
#         print('正在打第%d游戏'%x)
#         yield None
#
# t1 = game(5)
# t2 = music(5)
#
# while True:
#     try:
#         t1.__next__()
#         t2.__next__()
#     except :
#         break


# from collections import Iterable
# # from typing import Iterable
# list2 = [1,2,3,4,5,6]
# list1 = (x for i in range(10))
# f1 = isinstance(list1,Iterable)
# f2 = isinstance(list2,Iterable)
# print(f1)
# print(f2)


# a = [x + 2 if x%2==0 else x -5 for x in range(1,50)]
# print(a)
#
# b = [x**2 for x in range(1,50) if x % 2==0]
# print(b)

#
# class Person:
#     __age = 18
#
#     def name(self):
#         Person.__age = 100
#         print('------> 对象调用类属性',Person.__age)
#
#     @classmethod
#     def show_age(cls):
#         print('----->类方法,在对象创建之前创建,只能访问类属性和方法', Person.__age)
#
#     @classmethod
#     def update_age(cls):
#         # Person.__age = 22
#         print('----->类方法', Person.__age)
#
#     @staticmethod
#     def test():
#         print('----->静态方法,只能访问类属性和方法,无法访问对象的属性和方法,无参数', Person.__age)
#
# p = Person()
# p.name()
# Person.show_age()
# Person.update_age()
# Person.test()


# import os
# print(os.chdir(r'D:\code'))
# print(os.path.abspath(__file__))
# import xlrd
# xlsx = xlrd.open_workbook('Excel_Workbook.xls','r')
# table = xlsx.sheet_by_index(0)       # 读取第0个表
# table = xlsx.sheet_by_name('My Worksheet') # 读取名字为My Worksheet的表
# print(table.cell_value(0,0))
# print(table.cell_value(0,1))
# print(table.cell_value(1,0))
# print(table.cell_value(1,1))


# class Base:
#     def showBase(self):
#         print('爸爸')
#
#
# class BigSon(Base):
#     def show(self):
#         print('我是大儿子')
#
# class Smallson(Base):
#     def show(self):
#         print('我是小儿子')
#
#
# a = BigSon()
# a.show()
# a.showBase()


# # 输入用户名和密码进行校验  当存够三个数据的时候  把所有用户都打印出来
# import re
#
#
# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#
#     def p(self):
#         print('%s今年%s,他的邮箱是%s' % (self.name, self.age, self.email))
#
#
# class account:
#     def __init__(self):
#         self.User_list = []
#
#
#     def login(self):
#         while True:
#             name = input('输入姓名:')
#             age = 18
#             email = 'liqi19890502@sina.com'
#             user = User(name, age, email)
#             if re.search('[a-zA-Z0-9]{4,12}@[(sina)|(163)|(126)].+\.+[(com)|(cn)]+', email):
#                 self.User_list.append(user)
#                 print(len(self.User_list))
#                 if len(self.User_list) == 3:
#                     for i in self.User_list:
#                         i.p()
#
#
# if __name__ == '__main__':
#     acc = account()
#     acc.login()


# A={1:0,2:0,3:0}
# B={'1':0,'2':0,'3':0}
# C={(1,2):0,(4,3):0}
# D={[1,2]:0,[4,3]:0}   # 错的
# E= {{1,2}:0,{4,3}:0}  # 错的

# for key,value in A.items():
#     print(key,value)

# class Foo:
#     country = "中国"
#
#     def __init__(self,name):
#         self.name = name
#     def func(self):
#         pass
#
# print(Foo.country)
# a = Foo('中国')
# print(a.country)
# print('*'*50)
# obj1 = Foo('中国')
# obj2 = Foo('美国')
# print(obj1.name)
# print(obj2.name)
# print('*'*50)
# obj1.country = '美国'
# print(obj1.country)
# print(obj2.country)
# print('*'*50)
# Foo.country = '美国'
# print(obj1.country)
# print(obj2.country)

#  私有实例化变量
# class Foo:
#     def __init__(self,name):
#         self.__name =name
#         self.age =100
#
#     def Func(self):
#         print(self.__name)
#
# obj1 = Foo(123)
# obj1.Func()

# 私有类变量
# class Foo(object):
#     _country = "中国"
#
#     def __init__(self,name):
#         self.name = name
#     def func(self):
#         print(self._country)
#         print(Foo._country)
#         print(self.name)
#
#     @staticmethod
#     def text():
#         print('静态方法')
#
#     @classmethod
#     def show(cls):
#         print('类方法')
#
#     @property
#     def start(self):
#         print('属性,调用时候不用加括号,对于简单的方法,当无需参数有返回值的时候可以使用@property')
#         return 1
# f = Foo('张三')
# f.func()
# f.name
# Foo.text()
# Foo.show()
# print(Foo.start)


# con改密码
# a = '%Jan 15 19:30:23 2020 D-CJ-XGB-S1-1 SHELL/6/SHELL_SECLOG: -Task=au0-IPAddr=**-User=XJcjdd_2016q2; Command is password cipher ******'
# a1= 'Jan 15 20:14:19 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=au0-IPAddr=**-User=xjdl; Command is password cipher ******'

# [console-change-password]
# b = '^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s:\d{3}\s++\d{4}\s+(?<sw_name>\S+)\s+.+SHELL_SECLOG:\s+.+User=(?<User>\S+);\s+Command\s+is\s+password\s+.+$'
#
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG\S+\s+.+User=(?P<user_name>\S+);',a1).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+Command\s+is\s+(?P<command>.+)$',a1).groups())
# # <4> ${#time} ${sw_name} SW 0 7 admin 0.0.0.0 ${command}

# # ssh 修改密码
# c1= 'Jan 15 20:15:28 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is password cipher ****** '
#
# # [SSH-TELNET-change-password]
# d = '^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?<sw_name>\S+)\s+.+IPAddr=(?<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?<User>\S+);\s+Command\s+is\s+password\s+cipher\s+.+$'
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',c1).groups())
# ^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$
# <4> ${#time} ${sw_name} SW 0 6 ${user} ${login_ip} ${command}
#


# e = 'Jan 15 20:13:15 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=xjdl; Command is dis local-user'
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',e).groups())
#
# e1 = 'Jan 15 20:14:19 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=au0-IPAddr=**-User=xjdl; Command is password cipher ******'
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<command>.+)$',e1).groups())

# e2 = 'Jan 15 20:15:28 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is password cipher ******'
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<User>\S+);\s+Command\s+is\s+password\s+\S+\s+.+$'),e2)

#
# d1 = 'Jan 15 20:13:15 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=xjdl; Command is dis local-user  '
# d2 = 'Jan 15 20:13:28 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=au0-IPAddr=**-User=xjdl; Command is local-user guanli '
# d3 = 'Jan 15 20:15:17 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is sys'
# d4 = 'Jan 15 20:15:21 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is local-user guanli '

# ssh_passwd = 'Jan 15 20:15:28 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is password cipher ******'
# con_com = 'Jan 15 20:13:15 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=xjdl; Command is dis local-user'

# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',d1).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',d2).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',d3).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',d4).groups())

# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',ssh_passwd).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<User>\S+);\s+Command\s+is\s+password\s+\S+\s+.+$',ssh_passwd).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\S+)-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',con_com).groups())


# 串口命令回显
# a1 = 'Jan 15 20:13:15 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=xjdl; Command is dis local-user'
# # 串口修改密码
# a2 = 'Jan 15 20:14:19 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=au0-IPAddr=**-User=xjdl; Command is password cipher ******'
#
# # ssh命令回显
# a3 = 'Jan 15 20:15:17 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_CMD(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is sys'
# # ssh修改密码
# a4 = 'Jan 15 20:15:28 2020 XinGuBian-SW-2-3600-1 %%10SHELL/6/SHELL_SECLOG(l): -Task=vt0-IPAddr=65.101.10.254-User=xjdl; Command is password cipher ******'

# 串口回显
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=..-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',a2).groups())
# 串口修改密码
# print(re.search('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=..-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$',a2).groups())
# print(re.search('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=..-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$',a2).groups())
# print(re.search('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=..-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$',a3).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=..-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$',a2).groups())


# ssh修改密码
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<command>.+)$',a3).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<command>.+)$',a1).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<command>.+)$',a2).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_S\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<command>.+)$',a4).groups())


# ssh回显
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',a3).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',a1).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',a2).groups())
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',a4).groups())


# class School:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#
#     def speech(self):
#         print('python')
#
# obj1 = School('老男孩北京校区','沙河')
# obj2 = School('老男孩上海校区','浦东')
# obj3 = School('老男孩深圳校区','南山')
#
#
# class Teacher:
#
#     def __init__(self,name,age,salary):
#         self.name =name
#         self.age = age
#         self.__salary = salary
#         self.school = None
#
# t1 = Teacher('李杰',19,18888)
# t2 = Teacher('闫涛',18,8888)
# t3 = Teacher('女神',19,98888)
#
# t1.school = obj1
#
#
# print(t1.school.name)
# print(t1.school.address)
# print(t1.name)
# print(t1.age)
# t1.school.speech()

#
# class foo:
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self,num):
#         self.num =num
#         self.__salary = 1000
#
#     def get_data(self):
#         print(self.num+self.a1)
#
# obj = foo(666)
#
# print(obj.num)
# print(obj.a1)
# print('error')
# print('error')
# print(obj.a1)
# print('error')


# class pri:
#
#     def __new__(cls, *args, **kwargs):
#         print('先执行一次这个')
#         return object.__new__(cls)
#
#     def __init__(self):
#         print('在执行一次init')
#
#     @staticmethod
#     def __func():
#         print('__func')
#
#     def get(self):
#         print('get')
#         self.__func()

# def __enter__(self):
#     print('做一次enter')
#     return '返回这个东西'

# def __exit__(self, exc_type, exc_val, exc_tb):
#     print('做一次extel')


# obj = pri()
# obj.get()
#
#
# with obj:
#     print('执行with')


# class Foo:
#     def f1(self):
#         super().f1()
#         print('3个功能')
#
#
# class Bar():
#     def f1(self):
#         print('6个功能')
#
# class info(Foo,Bar):
#     pass
#
#
#
# obj = info()
# obj.f1()
#
#
# getattr()
# hasattr()
# setattr()
# delattr()

#
# import hashlib
#
# a = hashlib.md5()
# a.update('123'.encode('utf8'))
# print(a.hexdigest())
#
#
#
# import hashlib
#
# hash = hashlib.md5()#md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
# hash.update(bytes('123akjhk',encoding='utf-8'))#要对哪个字符串进行加密，就放这里
# print(hash.hexdigest())#拿到加密字符串
#
# a = hashlib.md5("123123123".encode("utf-8"))
# print(a.hexdigest())


# class func:
#     y = lambda self, x: x+1
#
#     def y(self, x):
#         return x + 1
#
# a = func()
# print(a.y(6))

# # 判断对象是否能调用 callable     可以加()运行的 必须是类,函数,方法
# def func(args):
#     if callable(args):
#         args()
#     else:
#         print('无法调用')
#
#
# def pri():
#     print('打印一哈 666')
#
# class PPlive:
#     def __init__(self):
#         print('调用我就打印PPlive 类')
#     @staticmethod
#     def WW():
#         print('我是个方法')
#
# func(pri)
#
# func(PPlive)
#
# func(PPlive.WW)


# # 检测第一个参数是否是第二个参数的子子孙孙类
# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# class Bar(Foo):
#     pass
#
#
# print(issubclass(Bar, Foo))
# print(issubclass(Bar, Base))
# print(issubclass(Base, Foo))


# 计算args 中函数,方法,Foo类对象的个数,并返回给调用者
# from types import MethodType, FunctionType
#
#
# class Foo(object):
#
#     def A(self):
#         pass
#
#     def B(self):
#         pass
#
#     def H(self):
#         pass
#
#     def K(self):
#         pass
#
#
# E = Foo()
# G = Foo()
# F = Foo()
#
#
# def C():
#     pass
#
#
# def D():
#     pass
#
#
# def func(*args):
#     func_num = 0
#     meth_num = 0
#     Foo_class = 0
#     """
#     计算args 中函数,方法,Foo类对象的个数,并返回给调用者
#     :param args:
#     :return:
#     """
#     for item in args:
#         if isinstance(item, FunctionType):
#             func_num += 1
#         elif isinstance(item, MethodType):
#             meth_num += 1
#         elif type(item) == Foo:
#             Foo_class += 1
#         else:
#             pass
#     print('函数有:',func_num, '方法有:',meth_num, 'Foo类对象有:',Foo_class)
#
#
# func(E.A, G.B, C, D, E, F, G, E.H, G.K)


# ## 代码流程,关系,分析 1(子类没有被实例化,不进行操作,StarkConfig类进行2次实例化,分别insert一次数据)
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#
# s1 = StarkConfig()
# s2 = StarkConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s2.get_list_display()
# print(result2)  # 33 33


# # ## 代码流程,关系,分析(2)
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#
# s1 = StarkConfig()
# s2 = RoleConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s2.get_list_display()
# print(result2)  # 33 11 22


# # # ## 代码流程,关系,分析(3)
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#
# s1 = RoleConfig()
# s2 = RoleConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33 11 22
#
# result2 = s2.get_list_display()
# print(result2)  # 33 33 11 22


# # iter 如果能被for循环那么函数里肯定有iter,并且返回一个可迭代对象
# class Foo:
#
#     def __iter__(self):
#         return iter([11,22,33,44])
#
# a = Foo()
# for i in a:
#     print(i)


# class Foo:
#
#     def __init__(self, num):
#         self.num = num
#         print('执行init方法')
#
#     def __new__(cls, *args, **kwargs):
#         print('执行new方法,必须返回一个object返回值才能继续初始化方法')
#         return object.__new__(cls)
#
#
# a = Foo(1)


# import handle
#
# def func():
#     objs = []
#     name_list = dir(handle)
#     print(name_list)
#     base_cls = getattr(handle,"Base")
#     for item in name_list:
#         val = getattr(handle,item)  # item
#         if val == base_cls:
#             continue
#         elif issubclass(val,base_cls):
#             obj = val()
#             objs.append(obj)
#
#
# if __name__ == '__main__':
#     func()


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# obj = Foo('li', 20)
# setattr(Foo, 'email', 'liqi')
#
# v1 = getattr(obj, 'email')
# v2 = getattr(Foo, 'email')
#
# print(v1, v2)


# # 把一个对象加括号运行（）
#
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print('123')
#
# obj = Foo()
# obj()


# 16 作业 补充选课系统（必须用反射）###
#
#
# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.course = []
#
#     def select_course(self):
#         """选择课程，已经存在的课程不在选"""
#         for i, item in enumerate(total_list, 1):
#             print(i, item)
#             clas = str(input('选择课程输入y或者课程编号,输入其他为不选择该课程:'))
#             if clas == 'y' or clas == str(i):
#                 if item not in self.course:
#                     self.course.append(item)
#                     print('------>选择该课程成功')
#                 else:
#                     print('已经选择该课程,请继续选择别的课程')
#
#     def show_course(self):
#         '''拆寻已经选择的课程'''
#         for i,item in self.course:
#             print(i,item)
#
#     def del_course(self):
#         '''删除已经选择的课程'''
#         print('del_course')
#
#
# total_list = ['chinese', 'english', 'mathematics', 'physics', 'chemistry',
#               'history', 'music', 'art', 'politics', 'Compiler']
#
#
# def run():
#     while True:
#         name = input('请输入学生姓名:')
#         print('%s同学的选课系统\n1,选择课程\n2，查询所有已选课程\n3.删除已选课程' % name)
#         name = Student(name)
#         '''
#         1.根据Course类创建一个课程
#         2.用户输入学生姓名，动态创建学生对象
#         3.查询所有课程
#         4.为学生选课
#         5.删除已选课程
#         :return:
#         '''
#         num = input('请输入要选择的项目编号:')
#         if num == '1':
#             select_course = getattr(Student, 'select_course')
#             select_course(name)
#         elif num == '2':
#             show_course = getattr(Student, 'show_course')
#             show_course(name)
#         elif num == '3':
#             del_course = getattr(Student, 'del_course')
#             del_course(name)
#         else:
#             print('输入错误,请重新输入')
#
#
# run()


# # # 抽象类和抽象类方法
#
# from abc import ABCMeta, abstractmethod
#
#
# class Base(metaclass=ABCMeta):  # 抽象类
#     def f1(self):
#         print(123)
#
#     @abstractmethod  # 抽象类方法
#     def f2(cls):
#         pass
#
#
# class Foo(Base):
#     def f2(self):  # 继承的时候必须要写父类的方法
#         pass
#
#
# obj = Foo()
# obj.f1()

#  1 什么是接口，作用

#  接口是一种数据类型，主要用于约束派生类中指定实现的方法。
#  python中不存在，而java和c#中存在的。
#
# 2 python中用什么约束

# --使用抽象类+抽象方法来对子类进行约束       大多使用抛异常   编写上比较麻烦。
# --人为主动抛出异常
#
# 3 结束时 是否可以抛出其他异常？
#
# 不专业的 raise Exception(".send() 必须被重写。")
# 专业的（raise NotImplementedError(".sned() 必须被重写。"）

# 4 写方法，写注释
# 5 写代码
# class BaseMessage(object):
#     def send(self,x1):
#         """
#         必须继承BaseMessage，然后其中必须编写send方法，用于完成具体业务逻辑
#         """
#         raise NotImplementedError(".send() 方法必须被重写")

###############报错的写法#############################
# class Email(BaseMessage):
#     pass
#
# func = Email()
# func.send(1)
###############报错的写法#############################

###############正确的写法#############################
# class Email(BaseMessage):
#     def send(self,x1):
#         print('发送邮件')
#
# func = Email()
# func.send(1)
###############正确的写法#############################


# 主动抛出自定义异常

# class PrintValueErroe(Exception):   # 继承异常类,创建一个异常类
#     def __init__(self,code,value):
#         self.code = code
#         self.value = value
#
#
# try:
#     raise PrintValueErroe(404,'网页不可达')  # 抛出一个异常，并赋异常值
#
# except PrintValueErroe as obj:              # 捕获自己的异常类
#     print(obj.code,obj.value)


# # 加密
#
# import hashlib
# # 加密方法1
# a = 'liqi-19890502'
# passwd = hashlib.md5(a.encode('utf8')).hexdigest()
# print(passwd)
#
# # 加密方法2
# passwd2 = hashlib.md5()
# passwd2.update(a.encode('utf8'))
# print(passwd2.hexdigest())
#
# # 加盐后加密
# passwd3 = hashlib.md5(b'12312312wedwdwew')
# passwd3.update(a.encode('utf8'))
# print(passwd3.hexdigest())
#
#
# # 定义一个加盐的函数
# def md5(pwd):
#     obj = hashlib.md5(b'wojiushijiadeyan')
#     obj.update(pwd.encode('utf8'))
#     return obj.hexdigest()
#
# print(md5(a))
#
# # 用加盐的密码进行登陆
# user = input('请输入用户名')
# pwd = input('请输入密码')
# if user == 'root' and md5(pwd) == '38e6faaabe276450256fba448418eda0':
#     print('登陆成功')
# else:
#     print('登陆失败')


#
# class Foo:
#     def __str__(self):
#         return 'str的用法'
#     pass
#
# func = Foo()
# print(func)
# print(type(func))


# #
# # 日志  只能打印一个日志文件
#
# import logging
# logger = logging.basicConfig(filename='x0.log',
#                              format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#                              datefmt='%Y-%m-%d %H-%M-%S',
#                              level=10)
#
# logging.debug("x1")
# logging.info("x2")
# logging.warning("x3")
# logging.error("x4")
# logging.critical("x5")
#
# # 获取当前的错误详细信息，并记录成日志文件，打印出来
#
# import traceback
#
# def func():
#     try:
#         a = a+1
#     except Exception as e:
#         # 获取当前错误的堆栈信息
#         msg = traceback.format_exc()
#         logging.error(msg)
#
# func()

# # 一次输出2个日志文件
#
# import logging
# file_handle = logging.FileHandler('x1.log','a',encoding='utf-8')
# file_handle.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',))
#
# logger1 = logging.Logger('s1',level=logging.ERROR)
# logger1.addHandler(file_handle)
#
# logger1.error(' yigerizhi')
#
#
# file_handle2 = logging.FileHandler('x2.log','a',encoding='utf-8')
# file_handle2.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',))
#
# logger2 = logging.Logger('s2',level=logging.ERROR)
# logger2.addHandler(file_handle2)
#
# logger2.error(' 第二个日志')
#
#
# import traceback
#
# def func():
#     try:
#         a = 1/0
#     except Exception as e:
#         # 获取当前错误的堆栈信息
#         msg = traceback.format_exc()
#         logger1.error(msg)
#         logger2.error(msg)
#
# func()


# # 多继承
# #
# # class A:
# #     def fi(self):
# #         print('a')
# #
# # class B:
# #     def fi(self):
# #         print('a')
# #
# # class c(A,B):   # 多继承,先找自己,找不到在做继承的左边,然后右边中在找
# #     pass
# #
# # func = c()
# # func.fi()
# #
# # print(c.__mro__) # 继承关系 顺序


# msg = '213123.2132erer213123.424dfgfg234234.234324'
# import re
# a = re.findall('[0-9\.]+',msg)
# print(float(a[1])+float(a[0])+float(a[2]))

# class StartConfig:
#     def __init__(self,num):
#         self.num = num
#
#     def run(self):
#         self()
#
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# class RoleConfig(StartConfig):
#     def __call__(self, *args, **kwargs):
#         print(345)
#
#     def __getitem__(self, item):
#         return self.num[item]
#
# v1 = RoleConfig('alex')
# v2 = StartConfig('wupeiqi')
#
# print(v1[1])
# print(v2[2])


# class UserIfo(object):
#     pass
#
# class De(object):
#     pass
#
# class startConfig(object):
#
#     def __init__(self,num):
#         self.num = num
#
#     def changlist(self,request):
#         print(self.num,request)
#
#     def run(self):
#         self.changlist(999)
#
# class RoleConfig(startConfig):
#
#     def changelist(self,erquest):
#         print(666,self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self,k,v):
#         self._registry[k] = v(k)
#
#
# site = AdminSite()
# site.register(UserIfo,startConfig)
# site.register(De,RoleConfig)
#
# site.register(UserIfo,startConfig)
# startConfig.run(site)

#
# class F3:
#     def f1(self):
#         ret = super().f1()
#         print(ret)
#         return 123
#
# class F2:
#     def f1(self):
#         print('123')
#
# class F1(F3,F2):
#     pass
#
# obj = F1()
# obj.f1()
#
#


#
# class S:
#     list = []
#
#     def f(self):
#         self.list.insert(0,33)
#         return self.list
#
# class B(S):
#     list = [11,22]
#
# s1 = S()
# s2 = B()
#
#
# res1 = s1.f()
# print(res1)
#
# res2 = s2.f()
# print(res2)
#


# 对象变成可迭代对象

# a = 0
# class func:
#     def __iter__(self):
#         return iter([11,22,33,44])
#
#
# a = func()
# for i in a:
#     print(i)


## 约束派生类
# class func:
#     def add(self):
#         pass
#         raise NotImplementedError
#
# class fun(func):
#     def add(self):
#         pass
#
# a = fun()
# a.add()


# 获取错误代码的堆栈信息
# import traceback
#
# def func():
#     try:
#         res = 1/0
#         print(res)
#     except :
#         v = traceback.format_exc()
#         print('--------->',v)
# func()


# class CsGame:
#     def __init__(self,name,life_value,arms,gender):
#         self.name = name
#         self.life_value = life_value
#         self.arms = arms
#         self.gender = gender
#
#
#
# class Police(CsGame):
#     def jieshao(self):
#         print('我是警察,我叫%s' % self.name)
#
#     def attack(self,other):
#         if isinstance(other,Police):
#             print('警察自己人,别打')
#         else:
#             other.life_value = other.life_value-10
#             print('%s攻击了%s,%s掉了10点血,还剩%s血' % (self.name, other.name, other.name, other.life_value))
#
# class Bandits(CsGame):
#     def jieshao(self):
#         print('我是匪徒,我叫%s' % self.name)
#
#     def attack(self,other):
#         if isinstance(other,Bandits):
#             print('匪徒自己人,别打')
#         else:
#             other.life_value = other.life_value -10
#             print('%s攻击了%s,%s掉了10点血,还剩%s血'%(self.name,other.name,other.name,other.life_value))
#
# alex = Police('alex',100,'M-16','man')
# # alex.jieshao()
# # print(alex.name)
#
# jack = Police('jack',100,'M-16','man')
# # jack.jieshao()
# # print(jack.name)
#
# wupeiqi = Bandits('wupeiqi',100,'AK-47','man')
# # print(wupeiqi.name)
# # wupeiqi.jieshao()
#
# # alex.attack(jack)
# alex.attack(wupeiqi)
# alex.attack(wupeiqi)
# wupeiqi.attack(jack)

# import requests
# url = 'https://www.nsfocus.com.cn/'
#
# page = requests.get(url).text
# print(page)


# import sys
# #GIL锁 执行的cpu指令次数
# v1 = sys.getcheckinterval()
# print(v1)


#
# import socket
# import select
#
# class Req(object):
#     def __init__(self,sk,func):
#         self.sk = sk
#         self.func = func
#         print('执行Req构造函数')
#
#     def fileno(self):
#         print('执行fileno函数')
#         return self.sk.fileno()
#
# class Nb(object):
#     def __init__(self):
#         self.conn_list = []
#         self.socket_list = []
#
#     def add(self,url,func):
#         client = socket.socket()
#         client.setblocking(False)
#         try:
#             client.connect((url,80))
#         except BlockingIOError as e:
#             pass
#
#         obj = Req(client,func)
#         self.conn_list.append(obj)
#         self.socket_list.append(obj)
#
#     def run(self):
#         while True:
#             rlist,wlist,elist = select.select(self.socket_list,self.conn_list,[],0.05)
#             for sk in wlist:
#                 sk.sendall('GET /s?wd=liqi HTTP/1.0\r\nhost:www.baidu.com \r\n\r\n')
#             for mes in rlist:
#                 mes_data = mes.recv(8096)
#                 print(mes_data)
#
#
#
# def baidu_response(data):
#     print('baidu')
#
# def sougou_response(data):
#     print('sogou')
#
# def oldboy_response(data):
#     print('oldboyedu')
#
# t1 = Nb()
# t1.add('www.baidu.com',baidu_response)
# t1.add('www.sogou.com',sougou_response)
# t1.add('www.oldboyedu.com',oldboy_response)
# t1.run()
#

# # 1.一行代码求和
# a = sum(range(11))
# print(a)
#
# # 2.修改全局变量的值
#
# a = 10
#
# def fun():
#     global a
#     a = 4
#     print(a)
# fun()

# i = 0
# j = 0
# k = 0
# num = 0
# a = 3
# i = a
#
# for i in range(a, a + 4):
#     for j in range(a, a + 4):
#         for k in range(a, a + 4):
#             if i != j and i != k and j != k:
#                 num += 1
#                 print('%d%d%d' % (i, j, k), end=' ')
#                 if num == 6:
#                     print()
#                     num = 0


# i = 0
# j = 0
# k = 0
# num = 0
# a = 2
# i = a
#
# while i <= a+3:
#     j = a
#     while j <=a+3:
#         k =a
#         while k <= a+3:
#             k +=1
#             if i!=j and i!=k and j!=k:
#                 print('%d%d%d'%(i,j,k),end=' ')
#                 num +=1
#                 if num ==6:
#                     print()
#                     num = 0
#         j += 1
#     i += 1

# 水仙花数
# for i in range(1, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             if i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k:
#                 print('%d%d%d' % (i, j, k))

# 水仙花数
# num = 0
# x = 101
# while x<1000:
#     k = x%10
#     j = int(x/10)%10
#     i = int(x/100)
#     if i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k:
#         print('%d%d%d' % (i, j, k))
#     x +=1


# git init  初始化
# git add test.py   把代码放入githun暂存区
# git commit 把代码从从暂存区放入仓库,   可以加 -m '添加修改原因'
# git status 查看当前代码修改状态
# git checkout 把代码从暂存区回滚到工作区
# git log - -pretty = oneline   查看每次修改代码的md5值得修改人员
# git reset --hard HEAD^  把代码回滚到上一次
# git reset --hard HEAD MD5值
# git reflog  查看所有的操作记录

# rm file    本地删除
# git add/rm file    缓存区上传修改的内容
# git reset HEAD file  从暂存区回滚到工作区
# git checkout file    把工作区里操作撤销

# import win32api
#
# import socket

# ser = socket.socket()
#
# ser.bind(('127.0.0.1', 8080))
# ser.listen(2)
# print('服务已经启动')
# while True:
#     ser.accept()


# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/78.0.3904.108 Safari/537.36',
#     'Cookie':'anonymid=k60bc4i5psbpr4; _r01_=1; __guid=238633222.2499836568309438500.1580363028767.5127; '
#              'taihe_bi_sdk_uid=4b2d4c9311131c7ec7c79168b419646a; '
#              '_de=961F83C680A7410F943EC906D67527C6F4489C1C70DDCBF9; ln_uact=liqi19890502@sina.com; '
#              'ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20110630/0210/h_main_MGrc_14cc0002911d2f75.jpg; '
#              'springskin=set; depovince=GW; jebecookies=7518eeb9-dc45-4dde-b801-3dc139b13275|||||; '
#              'JSESSIONID=abcrGGvC3tbc1_is5Vtax; ick_login=41566da2-dc36-4c50-a626-7444f0edd32d; '
#              'taihe_bi_sdk_session=497a5e2aa9fec1c9d7251b4fea4d9c8e; p=055a7cf7ebe469e5c110766375e1e1039; '
#              'first_login_flag=1; t=fc5b3dc1e1038cb2d3d1275a9f5695de9; '
#              'societyguester=fc5b3dc1e1038cb2d3d1275a9f5695de9; id=241751319; xnsid=ec40627f; ver=7.0; '
#              'loginfrom=null; wp_fold=0; monitor_count=6'}
# url = 'http://www.renren.com/241751319'
# req = requests.Request('GET',url,headers)
# ses = requests.Session()
#
# a = req.prepare()
# page = ses.send(a).text
# print(page)
#


# import re
#
# content = 'Hello 1234567 world!_This is a Regex Demo'
# result = re.match('^Hello.*?(\d+).*Demo$', content)
# print('result', result)
# print('group', result.group())
# print('group0', result.group(0))
# print('group1', result.group(1))
# print('groups', result.groups())
# print('groups0', result.groups(0))
# print('groups1', result.groups(1))


# from bs4 import BeautifulSoup
# import requests
# import lxml
# url = 'http://quote.eastmoney.com/center/qqzs.html'
# page_code = requests.get(url).text
# # print(page_code)
# soup = BeautifulSoup(page_code,'lxml')
# for num,i  in enumerate(soup.find_all('a')):
#     print(num,i)


# 猫眼top 100

# import requests
# import re
#
# url = []
# for i in range(0, 100, 10):
#     url.append('https://maoyan.com/board/4?offset=%s' % i)
# for i in url:
#     # print(i)
#     pass
#
# headers={
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'zh-CN,zh;q=0.9',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     }
#
# url_1 = 'https://maoyan.com/board/4?offset=0'
# page_code = requests.get(url_1,headers).content
# print(page_code)
#
# from selenium import webdriver
# import re
# import requests
#
# for offset in range(0, 100, 10):
#     url_1 = 'https://maoyan.com/board/4?offset=%s' % offset
#     d = webdriver.Chrome()
#     d.get(url_1)
#     mess = re.findall('<dd>.*?title="(.*?)".*?"star">(.*?)</p>.*?releasetime">(.*?)</p>.*?', d.page_source, re.S)
#
#     for num, i in enumerate(mess):
#         name = i[0].split()[0]
#         start = i[1].split()[0]
#         time = i[2].split()[0]
#         print(num, name, start, time)
#         message = str(num) + '\t' + name + '\t' + start + '\t' + time + '\n'
#         with open('maoyan.txt', 'a') as f:
#             f.write(message)


# # 淘宝美食
# import requests
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re
#
# url = 'https://www.taobao.com/'
#
# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 10)  # 浏览器响应等待最多时间
#
#
# def search():
#     try:
#         browser.get(url)
#         inputc = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
#         submit = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
#         inputc.send_keys('美食')
#         submit.click()
#         time.sleep(10)
#         total = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
#         return total.text
#
#     except Exception as e:
#         print(e)
#         return search()
#
#
# def nextpage(page_number):
#     print('准备开始翻第%s页' % page_number)
#     try:
#         inputc = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
#         submit = wait.until(EC.presence_of_element_located(
#             (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
#         inputc.clear()
#         inputc.send_keys(page_number)
#         submit.click()
#         wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), page_number)
#     except Exception as e:
#         print(e, '翻第%s页失败' % page_number)
#         exit()
#
#
# if __name__ == '__main__':
#     total = search()
#     total = int(re.search('(\d+)', total).group(1))
#     for i in range(2, 3):
#         nextpage(i)
#         time.sleep(2)


# import requests
# import re
# from time import sleep

# kxdaili_data = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
# }

# def get_page(url, options={}):
#     try:
#         ua = 'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
#     except Exception as f:
#         pass
#     base_headers = {
#         'User-Agent':  ua,
#         'Accept-Encoding': 'gzip, deflate, sdch',
#         'Accept-Language': 'zh-CN,zh;q=0.8'
#     }
#     print('================>',ua)
#     headers = dict(base_headers, **options)
#     print('Getting', url)
#     try:
#         r = requests.get(url, headers=headers)
#         print('Getting result', url, r.status_code)
#         if r.status_code == 200:
#             return r.content
#     except ConnectionError:
#         print('Crawling Failed', url)
#         return None
# base_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
# }
#
#
# def get_page(url):
#     """
#     抓取代理
#     :param url:
#     :param options:
#     :return:
#     """
#     print('page开始运行')
#     headers = dict(base_headers)
#     print('正在抓取', url)
#     print(url)
#     try:
#         response = requests.get(url, headers=headers)
#         sleep(1)
#         print('抓取成功', url, response.status_code)
#         if response.status_code == 200:
#             return response.text
#     except ConnectionError:
#         print('抓取失败', url)
#         return None


# def crawl_kxdaili():
#     for i in range(1, 3):
#         sleep(2)
#         start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
#         html = requests.get(start_url, kxdaili_data).content
#         ip_adress = re.compile('<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>')
#         # \s* 匹配空格，起到换行作用
#         re_ip_adress = ip_adress.findall(str(html))
#         print('re_ip_adress===>', re_ip_adress)
#         for adress, port in re_ip_adress:
#             result = adress + ':' + port
#             result = result.replace(' ', '')
#             print(result)


# crawl_kxdaili()


# def crawl_ip3366():
#     print('crawl_ip3366开始运行')
#     for page in range(1, 2):
#         print(page)
#         sleep(1)
#         start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
#         html = get_page(start_url)
#         print(html)
#         ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
#         # \s * 匹配空格，起到换行作用
#         re_ip_address = ip_address.findall(html)
#         for address, port in re_ip_address:
#             result = address + ':' + port
#             print(result)
#             yield result.replace(' ', '')
#
#
# crawl_ip3366()


# proxy_url = 'http://127.0.0.1:5555/random'
# proxy = requests.get(proxy_url).text
# proxies = {"http": "http://" + proxy}
# print('proxies', proxies)
#
# url = 'http://httpbin.org/get'
#
# # response = requests.request(method="GET", url=url, headers=data, proxies=proxies)
# resp = requests.request(method='GET' ,url=url ,proxies=proxies)
# print(resp.text)


# from selenium import webdriver
# import re
# import requests
#
# url_1 = 'https://www.bd-film.cc/gq/15676.htm'
# d = webdriver.Chrome()
# d.get(url_1)
# print(d.page_source)
# mess = re.findall('.*class="option".*data-clipboard-text="(.*?)">复制地址</a>\s+<a class="label label-info"', d.page_source)
# print(mess)
# d.close()


# 把usb里的文件拷贝出来
# import psutil
# import sys
# import os
# import time
# from datetime import datetime
#
# mobile = ""  # 移动设备盘符
#
# # 储存当前盘的盘符
# def updata():
#     global mobile
#     try:
#         part = psutil.disk_partitions()
#     except:
#         sys.exit(-1)
#     else:
#         # 驱动器分类
#         for i in range(len(part)):
#             tmplist = part[i].opts.split(",")
#             if "fixed" in tmplist:  # 本地设备
#                 pass
#             elif "cdrom" in tmplist:  # CD设备
#                 pass
#             else:
#                 # U盘
#                 mobile = part[i].device[:2]
#                 print('mobile',mobile)
#                 break
#
#
# # 读取U盘并复制到指定位置
# def copy_file_to_disk_hidden(USB_path):
#     # U盘的盘符
#     print('===')
#     usb_path = USB_path + "/"
#     print('save_path', usb_path)
#     # 要复制到的路径
#     mkdir("D:/usb_io/")
#     save_path = "D:/usb_io/" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
#     print('save_path',save_path)
#     f = open(save_path, "w", encoding='utf-8')
#     # 复制U盘的内容名称
#     while True:
#         if os.path.exists(usb_path):
#             filelist = []
#             filenames = os.listdir(USB_path)
#             for fn in filenames:
#                 fullfilename = os.path.join(USB_path, fn)
#                 filelist.append(fullfilename)
#             for j in filelist:
#                 f.write(str(j) + '\n')
#             break
#         else:
#             time.sleep(1)
#     f.close()
#
#
# # 创建指定位置
# def mkdir(path):
#     isExists = os.path.exists(path)
#     # 判断结果
#     if not isExists:
#         # 创建目录操作函数
#         os.makedirs(path)
#         return True
#     else:
#         # 如果目录存在则不创建
#         return False
#
#
# if __name__ == "__main__":
#     #读取驱动器信息
#     while True:
#         updata()
#         print('0',mobile)
#         if mobile != "":
#             print('1')
#             copy_file_to_disk_hidden(mobile)
#             time.sleep(60)
#         else:
#             print('2')
#             time.sleep(5)


import re
# # # 网神防火墙3600版本3.6.6阻断策略
# deny = 'devid=3 dname="SecGateNSG" date="2020-06-22 15:29:02" mod=policy pri=warning sip=192.168.150.200 dip=239.255.255.250 sport=51972 dport=1900 proto=UDP szone= dzone= appname=APP-NONE usrname= hit_num=0 action=deny from_tunnel= to_tunnel= msg="Match security policy, name:[any], action:[deny]"'
# print(re.search('devid=3\s+dname="(?P<name>\S+)"\s+\S+\s+\S+.*?sip=(?P<sip>\S+)\s+dip=(?P<dip>\S+)\s+sport=(?P<sport>\S+)\s+dport=(?P<dport>\S+)\s+.*?deny.*',deny).groups())
# # #  网神防火墙3600版本3.6.6保存配置
# # devid=3 dname="SecGateNSG" date="2020-06-22 14:40:12" mod=restore pri=info user=zfmd from=web msg="Save config"
# re_rule = 'devid=3 dname="SecGateNSG" date="2020-06-22 14:40:12" mod=restore pri=info user=zfmd from=web msg="Save config"'
# print(re.search('devid=3\s+dname="(?P<name>\S+)"\s+\S+\s+\S+.*?user=(?P<user>\S+).*?msg="(?P<msg>.*?)"',re_rule).groups())
#
#
# # #  网神防火墙3600版本3.6.6退出成功
# # devid=3 dname="SecGateNSG" date="2020-06-22 14:40:30" mod=admin pri=info msg=Admin logout success, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS]
# logout = 'devid=3 dname="SecGateNSG" date="2020-06-22 14:40:30" mod=admin pri=info msg=Admin logout success, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS]'
# print(re.search('devid=3\s+dname="(?P<name>\S+)"\s+\S+\s+\S+.*?logout success.*?name:\[(?P<user>\S+)\].*?from-ip:\[(?P<ip>.*?)\].*',logout).groups())
#
#
# # #  网神防火墙3600版本3.6.6登录失败
# # devid=3 dname="SecGateNSG" date="2020-06-22 14:41:01" mod=admin pri=err msg=Admin login fail, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS], reason:[Username or password is wrong]
# logfail = 'devid=3 dname="SecGateNSG" date="2020-06-22 14:41:01" mod=admin pri=err msg=Admin login fail, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS], reason:[Username or password is wrong]'
# print(re.search('devid=3\s+dname="(?P<name>\S+)"\s+\S+\s+\S+.*?login fail.*?name:\[(?P<user>\S+)\].*?from-ip:\[(?P<ip>.*?)\].*',logfail).groups())
#
# # #  网神防火墙3600版本3.6.6登录成功
# # devid=3 dname="SecGateNSG" date="2020-06-22 14:41:49" mod=admin pri=info msg=Admin login success, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS]
# login = 'devid=3 dname="SecGateNSG" date="2020-06-22 14:41:49" mod=admin pri=info msg=Admin login success, name:[zfmd], from-ip:[10.0.0.44], mode:[HTTPS]'
# print(re.search('devid=3\s+dname="(?P<name>\S+)"\s+\S+\s+\S+.*?login success.*?name:\[(?P<user>\S+)\].*?from-ip:\[(?P<ip>.*?)\].*',login).groups())


# 单电源故障及恢复
# g = 'Jun 22 2020 19:39:52 USG6300 %%01SRM/3/POWER_FAULT(l)[219]:Power slot 5 is faulty.'
# h = 'Jun 22 2020 19:40:02 USG6300 %%01SRM/5/POWER_FAULT_RESUME(l)[220]:Power slot 5 resume normal.'
# l = 'Jun 22 2020 19:40:22 USG6300 %%01SRM/3/POWER_FAULT(l)[221]:Power slot 6 is faulty.'
# i = 'Jun 22 2020 19:40:42 USG6300 %%01SRM/5/POWER_FAULT_RESUME(l)[222]:Power slot 6 resume normal.'
# print(re.search('\S+\s+\S+\s+\S+\s+\S+\s+(?P<name>\S+)\s.*?POWER_FAULT.*?Power slot 5 is faulty.',g).groups())
# print(re.search('\S+\s+\S+\s+\S+\s+\S+\s+(?P<name>\S+)\s.*?POWER_FAULT.*?Power slot 6 is faulty.',l).groups())
# print(re.search('\S+\s+\S+\s+\S+\s+\S+\s+(?P<name>\S+)\s.*?POWER_FAULT_RESUME.*?Power slot 5 resume normal.',h).groups())
# print(re.search('\S+\s+\S+\s+\S+\s+\S+\s+(?P<name>\S+)\s.*?POWER_FAULT_RESUME.*?Power slot 6 resume normal.',i).groups())

# # # 拦截到非法业务
# f =' Jun 22 2020 19:40:32 USG6300 %%01POLICY/6/POLICYDENY(l):vsys=public, protocol=1, source-ip=10.172.85.121, source-port=0, destination-ip=10.172.85.11, destination-port=0, time=2020/6/22 19:40:32, source-zone=local, destination-zone=untrust, application-name=, rule-name=default.'
# # print(re.search('\S+\s+\S+\s+\S+\s+\S+\s+(?P<name>\S+).*?DENY.*?source-ip=(?P<sip>\S+)..source-port=(?P<sport>\S+)..destination-ip=(?P<dip>\S+)..destination-port=(?P<dport>\S+).*',f).groups())
# #
# #
# # # 退出登录
# a = 'Jun 22 2020 19:34:04 USG6300 %%01HTTPD/5/OUT(l)[132]:User dlhadmin(IP:192.168.50.202 ID:478) logout'
# print(re.search('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+logout$',a).groups())
#
# # # 登录成功
# b = 'Jun 22 2020 19:34:15 USG6300 %%01HTTPD/6/PASS(l)[135]:User dlhadmin(IP:192.168.50.202 ID:508) login succeeded'
# print(re.search('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+login\s+succeeded$',b).groups())
# # # 登录失败
# c = 'Jun 22 2020 19:38:54 USG6300 %%01HTTPD/5/FAIL(l)[218]:User dlhadmin(IP:192.168.50.202 ID:31) login failed'
# print(re.search('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+failed$',c).groups())
# # # 修改配置
# d = 'Jun 22 2020 19:33:45 USG6300 %%01SHELL/5/CMDRECORD(s)[126]:Recorded command information. (Task=HTPN, Ip=192.168.50.202, VpnName=, User=dlhadmin, AuthenticationMethod="Null", Command="service udp514")'
# e = 'Jun 22 2020 19:38:36 USG6300 %%01SHELL/5/CMDRECORD(s)[211]:Recorded command information. (Task=HTPR, Ip=**, VpnName=, User=_system_, AuthenticationMethod="Null", Command="save all hda1:/vrpcfg.zip")'
# print(re.search('^\S+.+Ip=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+.+User=(?P<user_name>\S+),\s+.+\s+Command="(?P<command>.+)"\)$',d).groups())
# print(re.search('^\S+.+Ip=(?P<login_ip>\*\*),\s+.+User=(?P<user_name>\S+),\s+.+\s+Command="save all.*',e).groups())
#
# import time
# server = socket.socket(type=socket.SOCK_DGRAM)
# server.bind(('0.0.0.0',514))
# while 1:
#     data = server.recvfrom(80204)[0]
#     print('162端口已经开启',time.ctime())
#     print(data)

import re

# # 162端口已经开启 Tue Jun 23 19:29:06 2020
# a = "user:'admin';loginip:192.168.1.201;time:2020-06-23 19:23:46;type:2;编辑流量管理策略，编号[1]"
# print(re.search("user:'(?P<user_name>\S+)';loginip:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?type:2;", a).groups())
# #
# # 162端口已经开启 Tue Jun 23 19:29:28 2020
# b = "user:'admin';loginip:192.168.1.201;time:2020-06-23 19:24:07;type:2;注销成功"
# print(re.search("user:'(?P<user_name>\S+)';loginip:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?type:2;注销成功", b).groups())
# #
# # 162端口已经开启 Tue Jun 23 19:29:36 2020
# c = "user:;loginip:192.168.1.201;time:2020-06-23 19:24:16;type:3;登录失败"
# print(re.search("user:.*?loginip:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?type:3.*", c).groups())
# #
# # 162端口已经开启 Tue Jun 23 19:29:48 2020
# d = "user:'admin';loginip:192.168.1.201;time:2020-06-23 19:24:28;type:1;登录成功"
# print(re.search("user:'(?P<user_name>\S+)';loginip:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?type:1;登录成功", d).groups())
# #


# 5130登录失败 和修改密码

# a = 'Jun 29 14:06:36 2020 A-SW %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=xjdl; Command is password simple ******'
# b = 'Jun 29 14:06:16 2020 A-SW %%10LOGIN/5/LOGIN_FAILED: xjdl failed to log in from aux0.'
#
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$", a).groups())
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*LOGIN_FAILED:\s+(?P<user>\S+).+$", b).groups())


# Version 5.170 (S5720 V200R010C00SPC600)
# HUAWEI S5720-28P-SI-AC

# 登录成功
# a = 'Jun 29 2020 17:06:27 switch_1 %%01SHELL/5/LOGIN(s)[38]:The user succeeded in logging in to CON0. (UserType=CON, UserName=dlhmanager, AuthenticationMethod="Local-user", Ip=**, VpnName=)'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*LOGIN.*?succeeded.*?UserName=(?P<user>\S+),.+$", a).groups())
#
# # # 登录退出
# b = 'Jun 29 2020 17:07:09 switch_1 %%01SHELL/5/LOGOUT(s)[40]:The user succeeded in logging out of CON0. (UserType=CON, UserName=dlhmanager, Ip=**, VpnName=)'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*LOGOUT.*?UserName=(?P<user>\S+),.+$", b).groups())
# # 登录失败
# c = 'Jun 29 2020 17:07:12 switch_1 %%01SHELL/4/LOGINFAILED(s)[44]:Failed to login. (Ip=**, UserName=asdfasf, Times=1, AccessType=CON, VpnName=)'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*LOGINFAILED.*?Failed to login.*?UserName=(?P<user>\S+),.+$", c).groups())
# # # 输入命令
# e = 'Jun 29 2020 17:54:11 switch_1 %%01SHELL/6/DISPLAY_CMDRECORD(s)[56]:Recorded display command information. (Task=co0, Ip=**, VpnName=, User=dlhmanager, AuthenticationMethod="Local-user", Command="display current-configuration")'
# print(re.search('\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*CMDRECORD.*?command information.*?User=(?P<user>\S+),.*Command="(?P<command>.*)".', e).groups())
# # # 修改密码
# f = 'Jun 29 2020 17:02:54 switch_1 %%01AAA/6/LOCALACCOUNT_MODIFY(s)[10]:Local account dlhmanager password has been modified.'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*Local account\s+(?P<user>\S+)\s+password has been modified", f).groups())
# # # 网卡up
# g = 'Jun 29 2020 17:03:52 switch_1 %%01IFPDT/4/IF_STATE(l)[13]:Interface GigabitEthernet0/0/19 has turned into UP state.'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*?IF_STATE.*?:(?P<interface>.*)\s+has.*?UP.*", g).groups())
# # # 网卡down
# h = 'Jun 29 2020 17:03:47 switch_1 %%01IFPDT/4/IF_STATE(l)[12]:Interface GigabitEthernet0/0/19 has turned into DOWN state.'
# print(re.search("\S+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*?IF_STATE.*?:(?P<interface>.*)\s+has.*?DOWN.*", h).groups())


# Version 5.20, Release 2112
# H3C S3600V2-28TP-EI

# 登录成功
# a = 'Sep 14 03:49:12 2011 CHD-DLHFDYC-FGLYC-S2 %%10SHELL/5/SHELL_LOGIN(l): xjdl logged in from aux0.'
# print(re.search("^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+5/SHELL_LOGIN\S+:\s+(?P<user>\S+)\slogged\s+in\s+from\s+(?P<login_ip>\S+).$", a).groups())
#
# # # 登录退出
# b = 'Sep 14 03:49:02 2011 CHD-DLHFDYC-FGLYC-S2 %%10SHELL/5/SHELL_LOGOUT(l): xjdl logged out from aux0.'
# print(re.search("^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+5/SHELL_LOGOUT\S+:\s+(?P<user>\S+)\s+logged out\s+from.*", b).groups())
# # 登录失败
# c = 'Sep 14 03:49:05 2011 CHD-DLHFDYC-FGLYC-S2 %%10SHELL/5/SHELL_LOGINFAIL(l):  AUX user qqq failed to log in on AUX0.'
# print(re.search("^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).+/5/SHELL_LOGINFAIL\S+:\s+AUX user\s+(?P<user>\S+)\s+failed to log in on AUX0.", c).groups())
# # # 输入命令

# e = 'Jun 29 20:18:09 2020 CHD-DLHFDYC-FGLYC-S2 %%10SHELL/6/SHELL_CMD(l): -Task=au0-IPAddr=**-User=xjdl; Command is sys'
# # print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*?SHELL/6/SHELL_CMD.*?-User=(?P<user>\S+);.*?Command\s+is\s+(?P<command>.*)', e).groups())
# ee = 'xjdl 0.0.0.0 sys'
# print(re.search('^(?P<user_oper>(?P<oper_user>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<oper_info>.+))$',ee).groups())
# # # 修改密码
# f = 'Sep 14 03:48:52 2011 CHD-DLHFDYC-FGLYC-S2 %%10SHELL/6/SHELL_SECLOG(l): -Task=au0-IPAddr=**-User=xjdl; Command is password simple ******'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_SECLOG.+IPAddr=..-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$", f).groups())
# # # # 网卡up
# g = 'Jun 29 19:45:46 2020 CHD-DLHFDYC-FGLYC-S2 %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/24 link status is UP.'
# print(re.search("^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+3/LINK_UPDOWN\S+\s+(?P<if_name>\S+)\s+.+is\s+UP.+$", g).groups())
# # # # 网卡down
# h = 'Jun 29 19:45:44 2020 CHD-DLHFDYC-FGLYC-S2 %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/24 link status is DOWN.'
# print(re.search("^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+3/LINK_UPDOWN\S+\s+(?P<if_name>\S+)\s+.+is\s+DOWN.+$", h).groups())


# # 登录成功
# a = 'Jun 30 22:55:50 2020 A-SW %%10SHELL/5/SHELL_LOGIN: xjdl logged in from aux0.'
# print(re.search("^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL/5/SHELL_LOGIN:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\S+).$", a).groups())
#
# # 登录失败
# c = 'Jun 30 22:57:04 2020 A-SW %%10LOGIN/5/LOGIN_FAILED: xjdl failed to log in from aux0.'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*LOGIN/5/LOGIN_FAILED:\s+(?P<user>\S+)\s+failed to log.*$", c).groups())
#
# # 登录退出
# c = 'Jun 30 22:56:51 2020 A-SW %%10SHELL/5/SHELL_LOGOUT: xjdl logged out from aux0.'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*SHELL/5/SHELL_LOGOUT:\s+(?P<user>\S+)\s+logged out.*$", c).groups())


# usg6306

# d = 'Jul  1 2020 15:39:42 USG6300 %%01POLICY/6/POLICYDENY(l):vsys=public, protocol=1, source-ip=192.168.50.111, source-port=0, destination-ip=192.168.50.200, destination-port=0, time=2020/7/1 15:39:42, source-zone=local, destination-zone=trust, application-name=, rule-name=default.'
# print(re.search(".*?\d{2}:\d{2}:\d{2}\s+(?P<sw_name>\S+).*POLICY/6/POLICYDENY.*?source-ip=(?P<sip>\S+), source-port=(?P<sport>\S+), destination-ip=(?P<dip>\S+), destination-port=(?P<dport>\S+).*", d).groups())


#  Version 7.1.070, Release 6113
# H3C S5130-v7-6113

# 登录成功
# a = 'Jan  2 02:36:12 2013 SYRDC-PMU-SW1 %%10SHELL/5/SHELL_LOGIN: xjdl logged in from aux0.'
# a1 = 'Aug  1 19:09:46 2014 H3C %%10SHELL/5/SHELL_LOGIN: xjdl logged in from aux0.'
# print(re.search("^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL/5/SHELL_LOGIN:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\S+).$", a).groups())

# 登录退出
# b = 'Jan  2 02:36:28 2013 SYRDC-PMU-SW1 %%10SHELL/5/SHELL_LOGOUT: xjdl logged out from aux0.'
# b1 = 'Aug  1 19:10:20 2014 H3C %%10SHELL/5/SHELL_LOGOUT: xjdl logged out from aux0.'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*SHELL/5/SHELL_LOGOUT:\s+(?P<user>\S+)\s+logged out.*$", a).groups())
#
# # 登录失败
# c = 'Aug  1 19:10:28 2014 H3C %%10LOGIN/5/LOGIN_FAILED: xjdl failed to log in from aux0.'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*LOGIN/5/LOGIN_FAILED:\s+(?P<user>\S+)\s+failed to log.*$", c).groups())
#
#  # 输入命令
# e = 'Aug  1 19:10:01 2014 H3C %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=xjdl; Command is display current-configuration'
# print(re.search('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+SHELL_\S+\s+.+r=..-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$', e).groups())

# 修改密码
# f = 'Jul 13 14:47:35 2020 AGC-SW %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=xjdl; Command is password simple ******'
# print(re.search("\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$", f).groups())
# # # # 网卡up
# g = 'Jun 29 19:45:46 2020 CHD-DLHFDYC-FGLYC-S2 %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/24 link status is UP.'
# print(re.search("^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+3/LINK_UPDOWN\S+\s+(?P<if_name>\S+)\s+.+is\s+UP.+$", g).groups())
# # # # 网卡down
# h = 'Jun 29 19:45:44 2020 CHD-DLHFDYC-FGLYC-S2 %%10IFNET/3/LINK_UPDOWN(l): Ethernet1/0/24 link status is DOWN.'
# print(re.search("^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+3/LINK_UPDOWN\S+\s+(?P<if_name>\S+)\s+.+is\s+DOWN.+$", h).groups())


# # usg 6300
# #读取cpu
# aa = 'Sep 17 2020 17:16:52 USG6300 %%01SHELL/6/DISPLAY_CMDRECORD(s)[11]:Recorded display command information. (Task=FW, Ip=**, VpnName=, User=_system_, AuthenticationMethod="Null", Command="display cpu-usage")'
# cc_mess = re.findall('\S+\s+\S+\s+\S+\s+\S+\s+(?P<user_name>\S+).+SHELL/6/DISPLAY.+Command="display cpu-usage".',aa)
# print('cc_mess',cc_mess)
# #读取内存
# bb = 'Sep 17 2020 17:16:52 USG6300 %%01SHELL/6/DISPLAY_CMDRECORD(s)[12]:Recorded display command information. (Task=FW, Ip=**, VpnName=, User=_system_, AuthenticationMethod="Null", Command="display memory-usage system-memory")'
# bb_mess = re.findall('\S+\s+\S+\s+\S+\s+\S+\s+(?P<user_name>\S+).+SHELL/6/DISPLAY.+Command="display memory-usage system-memory".',bb)
# print('bb_mess',bb_mess)
# #修改配置信息
# cc = 'Sep 17 2020 17:04:51 USG6300 %%01SHELL/5/CMDRECORD(s)[46]:Recorded command information. (Task=HTPN, Ip=192.168.0.3, VpnName=, User=xjdl, AuthenticationMethod="Null", Command="save")'
# cc_mess = re.findall('^\S+.+Ip=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+.+User=(?P<user_name>\S+),\s+.+\s+Command="(?P<command>.+)"\)$',cc)
# print('cc_mess',cc_mess)
# ccc = '192.168.0.3 xjdl save'
# cc_mess_cc = re.findall('^\S+.+Ip=(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}),\s+.+User=(?P<user_name>\S+),\s+.+\s+Command="(?P<command>.+)"\)$',ccc)
# print('===================',ccc)
# # 登录成功
# dd = 'Sep 17 2020 17:13:06 USG6300 %%01HTTPD/6/PASS(l)[3]:User admin(IP:192.168.0.4 ID:167) login succeeded'
# dd_mess = re.findall('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+login\s+succeeded$',dd)
# print('dd_mess',dd_mess)
# # 登录退出
# ee = 'Sep 17 2020 17:13:13 USG6300 %%01HTTPD/5/OUT(l)[4]:User admin(IP:192.168.0.4 ID:167) logout'
# ee_mess = re.findall('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+logout$',ee)
# print('ee_mess',ee_mess)
# # 登录失败
# ff = 'Sep 17 2020 17:13:18 USG6300 %%01HTTPD/5/FAIL(l)[6]:User admin(IP:192.168.0.4 ID:193) login failed'
# ff_mess = re.findall('^\S+.+User\s+(?P<user_name>\S+)\(IP:(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+ID.+failed$',ff)
# print('ff_mess',ff_mess)
#
# a = '15%'
# print(re.findall('^(?P<cur_util>\d{1,3})%',a))

# # S3600 V3
# #串口登陆成功
# bbb = "Oct 16 17:18:17 2020 SDB-220kV-ZHXCLB-sw-2-3600 %%10SHELL/5/LOGIN(l):- 1 - xjdl(aux0) in unit1 login"
# ff_success = re.findall('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*%%.*?LOGIN.*-\s+(?P<user>\S+)\(.*login$',bbb)
# print('ff_success',ff_success)
# #串口登陆退出
# bbbb = "Oct 16 17:17:14 2020 SDB-220kV-ZHXCLB-sw-2-3600 %%10SHELL/5/LOGOUT(l):- 1 - xjdl(aux0) in unit1 logout"
# ff_logout = re.findall('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*%%.*?LOGOUT.*-\s+(?P<user>\S+)\(.*logout$',bbbb)
# print('ff_logout',ff_logout)
# #串口登录失败
# aa = "Sep 23 20:33:20 2020 SD1ZDTMYTSFDYC-SW-1-3600-2 %%10VTY/5/VTY_LOG(l):- 1 - AUX user fgsd failed to login on AUX0."
# ff_fail = re.findall('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).*user\s+(?P<user>\S+)\s+failed to login.*$',aa)
# print('ff_fail',ff_fail)
# #串口修改用户密码
# cc = "Sep 23 20:34:11 2020 SD1ZDTMYTSFDYC-SW-1-3600-2 %%10SHELL/5/CMD(l):- 1 -task:au0 ip:** user:ZDTMYTSFDYCgly command:password cipher ******"
# ff_edit = re.findall('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?CMD.*?user:(?P<user>\S+)\s+\S+\s+\S+\s+(?P<passwd>.+)$',cc)
# print('ff_edit',ff_edit)
# #串口用户操作信息
# dd = "Sep 23 20:34:13 2020 SD1ZDTMYTSFDYC-SW-1-3600-2 %%10SHELL/5/CMD(l):- 1 -task:au0 ip:** user:ZDTMYTSFDYCgly command:qu"
# ff_mess = re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*CMD.*user:(?P<user>\S+)\s+command:(?P<command>.+)$',dd)
# print('ff_mess',ff_mess)
# #串口网口down
# ee = "Sep 23 20:36:36 2020 SD1ZDTMYTSFDYC-SW-1-3600-2 %%10L2INF/5/PORT LINK STATUS CHANGE(l):- 1 -  Ethernet1/0/10 is DOWN"
# ee = "Oct 16 17:18:57 2020 SDB-220kV-ZHXCLB-sw-2-3600 %%10L2INF/5/PORT LINK STATUS CHANGE(l):- 1 -  Ethernet1/0/2 is DOWN"
# ff_down = re.findall('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+\s+LINK\s+.*-\s+(?P<if_name>\S+)\s+is\s+DOWN',ee)
# print('ff_down',ff_down)
# #串口网口up
# ff = "Oct 16 17:19:00 2020 SDB-220kV-ZHXCLB-sw-2-3600 %%10L2INF/5/PORT LINK STATUS CHANGE(l):- 1 -  Ethernet1/0/2 is UP"
# ff_up = re.findall('^\S+\s+\S+\s+\S+\s+\S+\s+(?P<sw_name>.+)\s+\S+\s+LINK\s+.*-\s+(?P<if_name>\S+)\s+is\s+UP',ff)
# print('ff_up',ff_up)

#
# a = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+(?P<file_name>.+)\s+[0-3]\s+\d{1,3}\s+\d{1,3}$'
# mess = '10.86.12.77 用户名 /ffc/etc/bbb 1 2 3'
# print(re.findall(a,mess))

# ATTACK = 'rule_id:2;time:2020-12-18 21:27:42;module:fw;src_intf:G1/1;dst_intf:G1/2;action:accept;proto:udp;src_addr:172.20.88.1;src_port:45268;dst_addr:172.20.220.23;dst_port:1032;src_addr_nat:;src_port_nat:;dst_addr_nat:;dst_port_nat:;info:;user:'
#
# attack_mess = re.findall('.*?src_addr:(?P<src_addr>.*?);src_port:(?P<src_port>.*?);dst_addr:(?P<dst_addr>.*?);dst_port:(?P<dst_port>.*?);.*?info:;(?P<user>.*?):',ATTACK)
# print(attack_mess)
# mess11 = 'dos icmp 172.20.88.1 0 172.20.88.1 0'
# att_rule = '^(?P<att_info>\S+\s+(?P<att_name>\S+)\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5}\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5})$'
# print(re.findall(att_rule,mess11))
#
# def get_mac_info():
#     os.environ['LC_ALL'] = 'C'
#     cmd = '''44:8a:5b:32:07:74
#         44:8a:5b:32:07:75
#         44:8a:5b:32:07:76
#         44:8a:5b:32:07:77
#         44:8a:5b:32:07:78
#         44:8a:5b:32:07:79
#         44:8a:5b:32:07:7a
#         44:8a:5b:32:07:7b'''
#     mac_info = ''
#     mac_info = os.popen(cmd).readlines()
#     return str(mac_info)

# cmd = '''44:8a:5b:32:07:74
#         44:8a:5b:32:07:75
#         44:8a:5b:32:07:76
#         44:8a:5b:32:07:77
#         44:8a:5b:32:07:78
#         44:8a:5b:32:07:79
#         44:8a:5b:32:07:7a
#         44:8a:5b:32:07:7b'''
# import os
# # print('',cmd.readlines())
#
# print(os.popen('dir').readlines())
# with open('test.txt','r') as f:
#     f.readlines()
# #     print(f)


# #H3C F1020
# #退出登录
# login_out = 'Aug 26 11:25:15 2021 H3C %%10SHELL/5/SHELL_LOGOUT: admin logged out from con0.'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+10SHELL/5/SHELL_LOGOUT:\s+.+from\s+(?P<user>\S+).+$',login_out))
# print(re.findall('^(?P<login_info>(?P<user_name>\S+)\s+(?P<login_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))$','ADMIN 0.0.0.0'))
# #登录失败
# login_fail = 'Aug 26 11:25:29 2021 H3C %%10LOGIN/5/LOGIN_FAILED: xjdl failed to log in from console0.'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).+10LOGIN/5/LOGIN_FAILED:\s+(?P<user>\S+)\s+failed.+$',login_fail))
# #登录成功
# login_success = 'Aug 26 14:34:10 2021 H3C %%10SHELL/5/SHELL_LOGIN: admin-liqi logged in from con0.\0x00'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+10SHELL/5/SHELL_LOGIN:\s+(?P<user>\S+)\slogged.+from\s+(?P<login_ip>\S+).$',login_success))
# #修改密码
# changepasswd = 'Aug 26 11:26:05 2021 H3C %%10SHELL/6/SHELL_CMD: -Line=con0-IPAddr=**-User=admin; Command is password simple ******'
# print(re.findall('\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+10SHELL/6/SHELL_CMD.*?-User=(?P<user>.+);\s+Command\s+is\s+password\s+\S+\s+(?P<passwd>.+)$',changepasswd))
# #修改配置
# re_rule1 = 'Aug 26 11:26:00 2021 H3C %%10SHELL/6/SHELL_CMD: -Line=con0-IPAddr=**-User=admin; Command is local-user xjdl class manage'
# re_rule2 = '<190>Aug 26 13:09:14 2021 H3C %%10SHELL/6/SHELL_CMD: -Line=con0-IPAddr=**-User=admin; Command is dis current-configuration'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+10SHELL/6/SHELL_CMD\S+\s+.+r=..-User=(?P<user>.+);\s+Command\s+is\s+(?P<command>.+)$',re_rule2))
# ###################网页登录失败
# weblogin_fail = 'Aug 26 11:44:46 2021 H3C %%10WEB/5/LOGIN_FAILED: admin failed to log in from 192.168.0.249'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+).+WEB/5/LOGIN_FAILED:\s+(?P<user>\S+)\s+failed.+.*?from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',weblogin_fail))
# #网页登录成功
# weblogin_success = 'Aug 26 11:44:57 2021 H3C %%10WEB/5/LOGIN: admin logged in from 192.168.0.249'
# print('登录成功',re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+%%10WEB/5/LOGIN:\s+(?P<user>\S+)\slogged\s+in\s+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',weblogin_success))
# #网页登录退出
# weblogin_out = 'Aug 26 11:45:02 2021 H3C %%10WEB/5/LOGOUT: admin logged out from 192.168.0.249'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.+10WEB/5/LOGOUT:\s+(?P<user>\S+)\s+logged\s+out\s+from\s+(?P<login_ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',weblogin_out))
# #网页修改策略
# webre_rule = 'Aug 26 11:40:59 2021 H3C %%10OBJP/6/OBJP_RULE_UPDATE_SUCCESS: RuleName(1080)=Any-Any;RuleID(1078)=0;Type'
# print('网页修改策略',re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?OBJP/6/OBJP_RULE_UPDATE_SUCCESS:(?P<mess>.*)',webre_rule))
# #电源
# single_power = 'Aug 26 12:26:55 2021 H3C %%10DEV/3/POWER_ABSENT: Power 1 is absent.'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?10DEV/3/POWER_ABSENT:\s+(?P<mess>.*).',single_power))
# #CPU
# CPU = 'Aug 26 11:39:45 2021 H3C %%10SHELL/6/SHELL_CMD: -Line=con0-IPAddr=**-User=admin; Command is display cpu-usage'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d(?P<cpu>\S+)\s+\d{4}\s+(?P<sw_name>\S+).*?10SHELL/6/SHELL_CMD.*?display cpu-usage',CPU))
# #MEMORY
# MEMORY = 'Aug 26 11:39:43 2021 H3C %%10SHELL/6/SHELL_CMD: -Line=con0-IPAddr=**-User=admin; Command is display memory'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d(?P<cpu>\S+)\s+\d{4}\s+(?P<sw_name>\S+).*?10SHELL/6/SHELL_CMD.*?display memory',MEMORY))
# #不符合安全策略告警
# DENY_rule = 'Aug 26 11:24:04 2021 H3C %%10FILTER/6/FILTER_ZONE_IPV4_EXECUTION: SrcZoneName(1025)=环保主站;DstZoneName(1035)=烟气子站;Type(1067)=ACL;ObjectPolicy(1072)=环保主站-烟气子站;RuleID(1078)=2;Protocol(1001)=TCP;Application(1002)=microsoft-ds;SrcIPAddr(1003)=65.64.59.11;SrcPort(1004)=3081;DstIPAddr(1007)=96.43.127.16;DstPort(1008)=445;MatchCount(1069)=1;Event(1048)=Deny;'
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?FILTER_ZONE_IPV4_EXECUTION.*?SrcIPAddr.*?=(?P<sourceip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3});SrcPort.*?=(?P<sourceport>\d+);DstIPAddr.*?=(?P<DstIPAddr>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3});DstPort.*?=(?P<DstPort>\d+).*?Event.*?=Deny;',DENY_rule))
# print(re.findall('^\S+\s+\d+\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+(?P<sw_name>\S+)\s+.*?FILTER_ZONE_IPV4_EXECUTION.*?SrcIPAddr.*?=(?P<sourceip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3});SrcPort.*?=(?P<sourceport>\d+);DstIPAddr.*?=(?P<DstIPAddr>9\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3});DstPort.*?=(?P<DstPort>\d+).*?Event.*?=Deny;',DENY_rule))
#
# a = 'Deny 65.64.59.11 3081 96.43.127.16 445'
# print(re.findall('^(?P<quintet>\S+\s+(?P<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5}\s+(?P<dst_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,5})$',a))


# day01

# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             print('{} * {} ='.format(j,i),i*j,end=' ')
#     print('\t')

# day02
#
# data = []
# while 1:
#     mess = input('请输入敏感字符：').strip()
#     if mess == 'Q' or mess == 'q':
#         print(data)
#         break
#     else:
#         data.append(mess)


# import os
#
# all_file = []
# file_lists = os.listdir(r'D:\AAA')
# for i in file_lists:
#     if os.path.isdir('D:\AAA\\'+ i):
#         all_file.append('D:\AAA\\'+ i)
# print(all_file)
#


# v1 = 123
# v2 = (123)
# v3 = (123,)
# print(v1,type(v1))
# print(v2,type(v2))
# print(v3,type(v3))

# import random
# poke_list = ['黑桃','梅花','红桃','方片']
# all_card = [[j,str(x)] for x in range(1,14) for j in poke_list]
#
# # print(all_card)
# a = random.shuffle(all_card)
#
# print(all_card[:3])
# print(all_card[3:6])
# print(all_card[6:9])


# def fun1(a1):
#     """
#
#     :param a1:
#     :return:
#     """
#     return 1
#

# import json
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.autohome.com.cn/news/'
#
# res = requests.get(url)
# text = res.content.decode('gbk')
#
# soup = BeautifulSoup(text,features='html.parser')
# soup = soup.find(name='div',attrs={'class':'editor-wrap'})
# soup = soup.find_all(name='li')
# mess = []
# for i in soup:
#     bk_add = 'https:'+i.find(name='img').attrs['src']
#     pic_add = 'https:'+i.find(name='a').attrs['href']
#     name_mess = i.find(name='div',attrs={'class':'editorname'}).text
#     position = i.find(name='div',attrs={'class':'position'}).text
#     # print('博客地址',bk_add)
#     # print('照片地址',pic_add)
#     print('姓名信息',name_mess)
#     # print('职位信息',position)
#     # print('*'*100)
#     mess.append({'博客地址':bk_add,'照片地址':pic_add,'姓名信息':name_mess,'职位信息':position})
#
# mess = json.dumps(mess)
# print(mess)
# with open('mess.json','w',encoding='utf8') as f:
#     f.write(mess)


# import time
#
#
# def out(func):
#     def inner(*args):
#         start = time.time()
#         res = func(*args)
#         end = time.time() - start
#         print('执行的时间是', end)
#         return res
#     return inner
#
#
# @out
# def fun1(x, y, z=10):
#     time.sleep(0.123)
#     return x + y + z
#
#
# print(fun1(2, 5))
# print(fun1(2, 5, 11))
#
# a_list = (x for x in range(10))
# a_list1 = [x for x in range(10)]
#
# def func2():
#     for i in range(10):
#         yield i
#
#
# a = func2()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#
# for j in a:
#     print(j)


# bin int list dict oct eval abs open set hex enumerate max min len map

# a1_list = [1, 2, 3, 4, 5]
#
# a1 = map(lambda x: x * 2, a1_list)
# for i in a1:
#     print(i)
#
# a2 = filter(lambda x: x % 2 == 1, a1_list)
# for j in a2:
#     print(j)


# class func1:
#     def __init__(self, name):
#         self.name = name
#         print('123')
#
#     def __new__(cls, *args, **kwargs):
#         # print(cls, *args)
#         return object.__new__(cls)
#
#
# opp = func1(777)
# print(opp.name)

# class fun2:
#     def __call__(self, *args, **kwargs):
#         print('1')
#
# opp2 = fun2()
# opp2()


# class Foo(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         pass
#
#     def __setitem__(self, key, value):
#         pass
#
#     def __delitem__(self, key):
#         pass
#
#
# obj = Foo("武沛齐", 19)
#
# obj["x1"]
# obj['x2'] = 123
# del obj['x3']


# class Context:
#
#     def do_something(self):
#         print('内部执行2')
#
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__')
#         pass
#
# with Context() as ctx:
#     print('内部执行1')
#     ctx.do_something()


# class Foo(object):
#     a1 = 1
#
#     def __init__(self, num):
#         self.num = num
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj1 = Foo(666)
# obj2 = Foo(999)
#
# print(obj1.num)  # 666
# print(obj1.a1)  # 1
#
# obj1.num = 18
# obj1.a1 = 99
#
# print(obj1.num)  # 18
# print(obj1.a1)  # 99
#
# print(obj2.a1)  # 1
# print(obj2.num)  # 999
# print(obj2.num)  # 999
# print(Foo.a1)  # 1
# print(obj1.a1)  # 99


# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run()
# print(v1)
#
# # 'f3'
# # 'f2'
# # 999
# # none


# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @staticmethod
#     def f2():
#         print('f2')
#
#
# obj = Foo()
# obj.f1()  # 'f1'
# obj.f2()  # 'f2'
#
# Foo.f1(obj)  # 'f1'
# Foo.f1()  # 报错
# Foo.f2()  #  'f2'


# class Foo(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def f1(self):
#         print("绑定方法", self.name)
#
#     @classmethod
#     def f2(cls):
#         print("类方法", cls)
#
#     @staticmethod
#     def f3():
#         print("静态方法")
#
#
# # 绑定方法（对象）
# obj = Foo("武沛齐", 20)
# obj.f1()  # Foo.f1(obj)
#
# # 类方法
# Foo.f2()  # cls就是当前调用这个方法的类。（类）
# obj.f2()  # cls就是当前调用这个方法的对象的类。
#
# # 静态方法
# Foo.f3()  # 类执行执行方法（类）
# obj.f3()  # 对象执行执行方法


# class Foo(object):
#
#     def f1(self):
#         print('f1')
#         self.f2()
#         self.f3()
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#     @staticmethod
#     def f3():
#         print('f3')
#
#
# obj = Foo()
# obj.f1()

#
# class Base(object):
#     @classmethod
#     def f2(cls):
#         print('f2', cls)
#
#     @staticmethod
#     def f3():
#         print('f3')
#
#
# class Foo(Base):
#     def f1(self):
#         print('f1', self)
#         self.f2()
#         self.f3()
#
#
# obj = Foo()
# obj.f1()


# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj = Foo(666)

# print(obj.num)  # 666
# print(obj.a1)  # 1
# print(obj.__salary) # 无此方法
# print(obj.__a2) # 无此方法
# print(obj.__a2)  # 无此方法
# print(Foo.a1)  # 1
# print(Foo.__salary)  # 无此方法
# print(Foo.__a2) # 无此方法
# obj.show_data()   # 667

#
# class Foo(object):
#
#     def __init__(self, age):
#         self.age = age
#
#     def display(self):
#         print(self.age)
#
#
# data_list = [Foo(8), Foo(9)]
# # print(data_list[0].age)
# # data_list[1].display()
#
# for item in data_list:
#     print(item.age, item.display())


# class Base(object):
#     def __init__(self, a1):
#         self.a1 = a1
#
#     def f2(self, arg):
#         print(self.a1, arg)
#
#
# class Foo(Base):
#     def f2(self, arg):
#         print('666')
#
#
# obj_list = [Base(1), Foo(2), Foo(3)]
#
# for item in obj_list:
#     item.f2(1)

# class Foo(object):
#     def __init__(self, num):
#         self.num = num
#
#
# v1 = [Foo for i in range(10)]
# v2 = [Foo(5) for i in range(10)]
# v3 = [Foo(i) for i in range(10)]
#
# print(v1)  # 十个函数
# print(v2)  # 十个函数
# print(v3)  # 十个函数


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [ StarkConfig(1),  StarkConfig(2),  StarkConfig(3) ]
# for item in config_obj_list:
#     print(item.num)

# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
#
# site.register('武沛齐', StarkConfig(19))  # num=19 5
# site.register('root', StarkConfig(20))  # num=20 5
# site.register("admin", RoleConfig(33))  # num=666 33
#
# print(len(site._registry))
#
# for k, row in site._registry.items():
#     row.changelist(5)


# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def run(self):
#         self()
#
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# class RoleConfig(StarkConfig):
#     def __call__(self, *args, **kwargs):
#         print(345)
#
#     def __getitem__(self, item):
#         return self.num[item]
#
#
# v1 = RoleConfig('alex')  # self.num = 'alex'
# v2 = StarkConfig("wupeiqi")  # self.num = "wupeiqi"
#
# print(v1[1])
# print(v2[2])


# class Context:
#     pass
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def do_something(self):
#         pass
#
#
# with Context() as ctx:
#     ctx.do_something()


# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
#
# p1.message()
# p2.message()


# class Node(object):
#     def __init__(self, title):
#         self.title = title
#         self.children = []
#
#     def add(self, node):
#         self.children.append(node)
#
#     def __getitem__(self, item):
#         return self.children[item]
#
#
# root = Node("中国")
#
# root.add(Node("河南省"))
# root.add(Node("河北省"))
#
# print(root.title) # "中国"
# print(root[0]) # "河南省"
# print(root[0].title)
# print(root[1]) # "河北省"
# print(root[1].title)


# class Node(object):
#     def __init__(self, title):
#         self.title = title
#         self.children = []
#
#     def add(self, node):
#         self.children.append(node)
#
#     def __getitem__(self, item):
#         return self.children[item]
#
#
# root = Node("中国")
#
# root.add(Node("河南省"))
# root.add(Node("河北省")) # Node("河北省") [Node("石家庄")[Node("雄安") Node("望都")]] Node("保定") Node("廊坊")
# root.add(Node("陕西省"))
# root.add(Node("山东省")) # Node("山东") Node("潍坊") Node("烟台") Node("威海")
#
# root[1].add(Node("石家庄"))
# root[1].add(Node("保定"))
# root[1].add(Node("廊坊"))
#
# root[3].add(Node("潍坊"))
# root[3].add(Node("烟台"))
# root[3].add(Node("威海"))
#
# root[1][1].add(Node("雄安"))
# root[1][1].add(Node("望都"))
#
# print(root.title) # "中国"
# print(root[0].title) # "中国"
# print(root[1].title) # "石家庄
# print(root[1][0].title) # "雄安"
# print(root[1][2].title) # 无
# print(root[1][1][0].title)


# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def message(self):
#         return "{}-{}".format(self.name, self.age)
#
#
# class Bar(Foo):
#     def __init__(self, email, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.email = email
#
#     def total(self):
#         data = "{}-{}-{}".format(self.name, self.age, self.email)
#         return data
#
#
# obj1 = Foo("武沛齐", 20)
# print(obj1.message)  # "武沛齐"-20
#
# obj2 = Bar("xx@live.com", "root", 100)
# print(obj2.message)
# print(obj2.total())


# class Foo(object):
#     def __call__(self, *args, **kwargs):
#         return 666
#
#
# data_list = [
#     "武沛齐",
#     dict,
#     lambda: 123,
#     True,
#     Foo,
#     Foo()
# ]
#
# for item in data_list:
#     if callable(item):
#         val = item()
#         print(val)
#     else:
#         print(item)

# "武沛齐"
# {}
# 123
# True
# <__main__.Foo object at 0x000002CE857EEF10>
# 666

# class func1():
#
#     @property
#     def run(self):
#         return 15
#
#
# funa = getattr(func1(), 'run')
#
# print(func1().run)
# print(funa)
# funb = func1()
# print(funb.run)


# class Person(object):
#     title = "北京"
#
#     def __init__(self, name, wx):
#         self.name = name
#         self.wx = wx
#
#     def show(self):
#         message = "姓名{}，微信：{}".format(self.name, self.wx)
#         return message
#
#     @property
#     def message(self):
#         return 666
#
#     @staticmethod
#     def something():
#         return 999
#
#
# obj = Person("武沛齐", "wupeiqi666")
#
# print(getattr(obj, 'wx'))	# "wupeiqi666"
# print(getattr(obj, 'message'))	# 666
# print(getattr(obj, 'show')()) 	# "姓名武沛齐，微信：wupeiqi666"
# print(getattr(obj, 'something')())	# 999

# import threading
# import time
# import threading
#
# lock = threading.RLock()
#
# class Singleton:
#     instance = None
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         with lock:
#             if cls.instance:
#                 return cls.instance
#             time.sleep(0.1)
#             cls.instance = object.__new__(cls)
#             return cls.instance
#
#
# def task():
#     obj = Singleton('x')
#     print(obj)
#
#
# for i in range(10):
#     t = threading.Thread(target=task)
#     t.start()


# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait)
# t.setDaemon(True)
# t.start()
# # flag b


# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait)
# t.setDaemon(False)
# t.start()
# # flag b


# import threading
# import time
# def _wait():
# 	time.sleep(5)
# # flag a
# t = threading.Thread(target=_wait)
# t.start()
# t.join()
# # flag b

# import threading
#
# loop = int(1E7)
#
#
# def _add(loop=1):
#     global number
#     for _ in range(loop):
#         number += 1
#
#
# def _sub(loop=1):
#     global number
#     for _ in range(loop):
#         number -= 1
#
#
# number = 0
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# print(number)


# import threading
#
# loop = int(1E7)
# number = 0
#
#
# def _add(loop=1):
#     global number
#     for _ in range(loop):
#         number += 1
#
#
# def _sub(loop=1):
#     global number
#     for _ in range(loop):
#         number -= 1
#
#
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# print(number)

# 单线程
import re
import time

all_nums = 0
def sums(txt_list):
    global all_nums
    sum_num = 0
    for j in range(len(txt_list)):
        num = int(re.findall(r'\d{4,}', txt_list[j])[0])
        sum_num += num
    all_nums += sum_num
    print(all_nums,time.time()-start_time)


with open(r'D:\code\111111111111.txt', 'r') as f:
    start_time = time.time()
    fs = f.readlines()
    page_num = len(fs)//100+1
    for i in range(page_num):
        sums(fs[i*100:(i+1)*100])


# 多线程
import re
import threading


all_nums = 0
def sums(txt_list,start_time):
    global all_nums
    sum_num = 0
    for j in range(len(txt_list)):
        num = int(re.findall(r'\d{4,}', txt_list[j])[0])
        sum_num += num
    all_nums += sum_num
    print(all_nums,time.time()-start_time)


def run():
    with open(r'D:\code\111111111111.txt', 'r') as f:
        start_time = time.time()
        fs = f.readlines()
        page_num = len(fs)//100+1
        for i in range(page_num):
            t = threading.Thread(target=sums, args=(fs[i*100:(i+1)*100],start_time))
            t.start()

# if __name__ == '__main__':
#     run()