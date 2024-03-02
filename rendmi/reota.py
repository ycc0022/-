import os
import subprocess
import sys
import uiautomator2 as u2
import time
import re


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger("D:\\Testlog.txt", sys.stdout)   #Log输出到D盘


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
z = 0
j = 0
nums = 1
a = int(input('请输入测试次数:'))
while i < a:
    d.app_start('com.xiaomi.wearable')  # com.xiaomi.wearable   com.zhapp.infowear
    time.sleep(2)
    try:
        # print("开始点击")
        d(resourceId="com.xiaomi.wearable:id/main_tv_tab_name", text="设备").click()
        # print("开始点击2")
        counts = 0
        while True:
            counts = counts + 1
            time.sleep(1)
            fail = d(resourceId="com.xiaomi.wearable:id/device_tv_status").get_text()
            if re.findall('电量', fail):
                d.swipe(500, 850, 500, 100, 0.2)
                time.sleep(0.5)
                d.swipe(500, 850, 500, 100, 0.2)
                time.sleep(0.5)
                d.swipe(500, 850, 500, 100, 0.2)
                time.sleep(0.5)
                d.swipe(500, 850, 500, 100, 0.2)
                time.sleep(1)
                break
            elif counts > 60 * 3:
                break
        time.sleep(3)
        d(resourceId="com.xiaomi.wearable:id/tv_feature_item_title", text="SD本地版本更新").click()
        time.sleep(1)
        d(resourceId="com.xiaomi.wearable:id/ota_directory_view").click()
        time.sleep(1)
        d(resourceId="com.google.android.documentsui:id/metadata").click()
        time.sleep(1)
        d(resourceId="com.xiaomi.wearable:id/upgrade_btn").click()
        time.sleep(1)
        count = 0
        while True:
            count = count + 1
            time.sleep(1)
            if d(text='重试').exists:
                x = x + 1
                print('OTA失败次数', x)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("picture{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                d.app_stop('com.xiaomi.wearable')
                break
            elif d(text='推送完成').exists:
                y = y + 1
                print('OTA成功次数', y)
                i = i + 1
                time.sleep(2)
                d.app_stop('com.xiaomi.wearable')
                break
            elif count > 60 * 5:
                z = z + 1
                print('OTA超时次数', z)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("picture{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                d.app_stop('com.xiaomi.wearable')
                break
    except:
        j = j + 1
        print("程序出错导致失败")
        i = i + 1
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        screenmap("picture{}.png".format(nums))
        nums = nums + 1
        d.app_stop('com.xiaomi.wearable')


print('OTA成功总次数=', x, 'OTA失败总次数=', y,  'OTA超时次数=', z, '程序出错=', j)
os.system("pause")
print("按任意键结束")

