# 本程序可以测试服务器的压力值
import threading  # 多线程库
import requests  # 先导入爬虫的库，不然调用不了爬虫的函数


def d():  # 爬虫函数
    while True:
        response = requests.get("http://70.newow.org/")  # get方法
        print(response.status_code)  # 状态码


while True:
    my_thread = threading.Thread(target=d, args=())  # 开线程运行一个爬虫
    my_thread.start()  # 运行