import os
import subprocess
import sys
import uiautomator2 as u2
import time


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
a = int(input('请输入测试次数:'))
d.app_start('com.zhapp.infowear')
while i < a:
    # 安卓13以上使用 打开adb shell svc bluetooth enable  # 关闭adb shell svc bluetooth disable
    os.system('adb shell settings put global airplane_mode_on 1')
    time.sleep(3)
    os.system('adb shell settings put global airplane_mode_on 0')
    time.sleep(3)
    d(text='健康').click(timeout=15)
    time.sleep(1)
    if d(resourceId='com.zhapp.infowear:id/battery').exists(timeout=20):
        x = x + 1
        print('成功次数', x)
        i = i + 1
        # break
    else:
        y = y + 1
        print('失败次数', y)
        i = i + 1
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        # break

print('成功总次数=', x, '失败总次数=', y)

os.system("pause")