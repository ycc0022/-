import os
import subprocess
import sys
import uiautomator2 as u2
import time

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

d = u2.connect_usb(devices[0])
i = 0
x = 0
y = 0
z = 0
d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=120)
message = d.toast.get_message(wait_timeout=120)
if message == '已存在此表盘':
    x = x + 1
    print('表盘传输成功次数', x)
    i = i + 1
    time.sleep(1)
    d.press('back')
elif message == '设备超时' or message == '同步失败':
    y = y + 1
    print('表盘传输失败', y)
    i = i + 1
    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
    time.sleep(2)
    d.press('back')
else:
    print('其它未知错误')
    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
    i = i + 1

d.toast.reset()