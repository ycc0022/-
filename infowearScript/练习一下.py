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
nums = 1
a = int(input('请输入测试次数:'))
d.app_start('com.xiaomi.wearable')
d(resourceId="com.xiaomi.wearable:id/main_tv_tab_name", text="设备").click()
d(resourceId="com.xiaomi.wearable:id/device_tv_synchronize").click(timeout=15)