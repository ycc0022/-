# coding: utf-8
import uiautomator2 as u2
import time
import random
from datetime import datetime
import subprocess
devices1 = str(subprocess.check_output("adb devices")).split('\n')
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
i = 0
a = int(input('请输入测试次数:'))
while i < a:   
    d = u2.connect_usb(devices[0])
    time.sleep(5)
    while(1):
        if(d(text="Update Watchface") != None):
            d(text="Update Watchface").click(timeout=15)
            print("开始下载")
            i = i
            time.sleep(20)
            d.app_start("com.touchgui.tool")
            time.sleep(2)
            d(text="REBOOT").click()
            time.sleep(3)
            d(resourceId="com.android.systemui:id/recent_apps").click(timeout=5)
            d.xpath('//*[@content-desc="NoiseFit"]/android.view.View[1]').click(timeout=5)
            time.sleep(15)
            break
          
        else: 
            time.sleep(10)
            break
    
    i += 1
    print(time.strftime('时间是：%Y年%m月%d日 %H:%M:%S')+'第' + str(1 * i) + '次重启')
