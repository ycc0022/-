import os
import subprocess
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
d.app_start('com.zhapp.infowear')
d(text='设备').click(timeout=15)
d(text='启用中').click(timeout=15)
d(text='查找设备').click(timeout=15)
i = 0
while i < 10000:
    d(text='查找设备').click()
    i += 1
