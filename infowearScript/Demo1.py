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

d(resourceId="com.android.systemui:id/center_group").click()
d(description="设置").click(timeout=15)
time.sleep(1)
d(text='蓝牙').click(timeout=15)
time.sleep(1)
d(resourceId="com.coloros.wirelesssettings:id/switchWidget").click()
if d(resourceId="com.coloros.wirelesssettings:id/switchWidget").get_text() == '开启':
    print('开始')
else:
    d(resourceId="com.coloros.wirelesssettings:id/switchWidget").click()