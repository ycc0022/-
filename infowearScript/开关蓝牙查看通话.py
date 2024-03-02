import os
import subprocess
import sys
import uiautomator2 as u2
import time
import random


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger("D:\\Testlog.txt")  #Log输出到D盘


def screenmap(file_name):
    # 截图
    os.popen("adb shell screencap /sdcard/{filename}".format(filename=file_name)).read()

    # 截图导出
    os.popen(r"adb pull /sdcard/{filename} {dir}".format(filename=file_name, dir="./sreenshot")).read()

    # 打开截图
    os.popen("adb shell rm /sdcard/{filename}".format(filename=file_name))


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
nums = 1
a = int(input('请输入测试次数:'))
is_inited = False
while i < a:
    try:
        if is_inited is False:
            is_inited = True
            d(resourceId="com.android.systemui:id/center_group").click()
            d(description="设置").click(timeout=15)
            time.sleep(1)
            d(text='蓝牙').click(timeout=15)
            time.sleep(1)
        if d(resourceId="com.coloros.wirelesssettings:id/switchWidget").get_text() == '开启':
            time.sleep(1)
            pass
        else:
            time.sleep(1)
            d(resourceId="com.coloros.wirelesssettings:id/switchWidget").click(timeout=15)
        if d(text="使用中，用于通话").exists(timeout=1):
            x = x + 1
            print('成功次数', x)
            i = i + 1
            # break
        else:
            y = y + 1
            print('失败次数', y)
            i = i + 1
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            d(resourceId="com.coloros.wirelesssettings:id/buttonPanel").click()
            # break
        time.sleep(1)
        d(resourceId="com.coloros.wirelesssettings:id/switchWidget").click(timeout=15)
        time.sleep(1)
    except:
        print("程序出错导致失败")
        i = i + 1
        is_inited = False

print('成功总次数=', x, '失败总次数=', y)

os.system("pause")
print("按任意键结束")

