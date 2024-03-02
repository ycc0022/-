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
i = 0
x = 0
y = 0
a = int(input('请输入测试次数:'))
d.app_start('com.touch.touchgui')
d(text='设备').click(timeout=15)
while i < a:
    os.system('adb shell settings put global airplane_mode_on 1')
    time.sleep(3)
    os.system('adb shell settings put global airplane_mode_on 0')
    time.sleep(3)
    if d(resourceId='com.touch.touchgui:id/tv_status').exists(timeout=20):
        x = x + 1
        print('成功次数', x)
        i = i + 1
        # break
    else:
        y = y + 1
        print('失败次数', y)
        i = i + 1
        # break

print('成功总次数=', x, '失败总次数=', y)

os.system("pause")