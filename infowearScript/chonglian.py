# coding: utf-8
#
import uiautomator2 as u2
import time
import random
import os
import subprocess

devices1 = str(subprocess.check_output("adb devices")).split("\n")
result = [x for x in devices1 if x != '']
devices = []  # 获取设备名称
for i in result:
    dev = i.split("\t")
    if len(dev) >= 2:
        devices.append(dev[0])
    if not devices:
        devices2 = str(subprocess.check_output("adb devices")).split("\\n")
        result1 = [x for x in devices2 if x != '']
        devices = []  # 获取设备名称
        for i in result1:
            dev = i.split("\\t")
            if len(dev) >= 2:
                devices.append(dev[0])
            if not devices:
                i = i
            else:
                print('当前连接设备：%s' % devices)
    else:
        print('当前连接设备：%s' % devices)
        
APPsite = "D:/开关APP.txt"
BTsite = "D:/开关蓝牙.txt"
file = open(APPsite,"w")
file = open(BTsite,"w")
i = 1
a = int(input('请输入测试次数:'))
while i < a:
    d = u2.connect_usb(devices[0])
    d.app_start("com.touch.touchgui")
    sat = time.time()
    d(text="设备").click(timeout=10)
    a1 = open(APPsite,"a")
    while(1):
        name = d(resourceId="com.touch.touchgui:id/tv_status").get_text()
        if "已连接" in name:
            end = time.time()
            lanya = end - sat
            print(str(1 * i),time.strftime('时间是：%Y年%m月%d日 %H:%M:%S', time.localtime()), "开关APP" , name , lanya)
            print(str(1 * i) , time.strftime('时间是：%Y年%m月%d日 %H:%M:%S', time.localtime()), "开关APP" , name , lanya , file=a1)
            break
        else:
            i = i
    a1.close()
    time.sleep(3)
    os.system("adb shell settings put global airplane_mode_on 1")
    d(resourceId="com.touch.touchgui:id/tv_status",text="未连接").exists(15)
    os.system("adb shell settings put global airplane_mode_on 0")
    sat1 = time.time()
    a2 = open(BTsite,"a")
    while(2):
        name1 = d(resourceId="com.touch.touchgui:id/tv_status").get_text()
        if "已连接" in name1:
            end1 = time.time()
            lanya1 = end1 - sat1
            print(str(1 * i),time.strftime('时间是：%Y年%m月%d日 %H:%M:%S', time.localtime()), "开关蓝牙" , name1 , lanya1)
            print(str(1 * i),time.strftime('时间是：%Y年%m月%d日 %H:%M:%S', time.localtime()), "开关蓝牙" , name1 , lanya1 , file=a2)
            break
        else:
            i = i
    a1.close()
    d.app_stop("com.touch.touchgui")
    
    i += 1
    print('第' + str(1 * i) + '次重连')
os.system("pause")