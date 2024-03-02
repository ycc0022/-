import os
import subprocess
import sys
import uiautomator2 as u2
import time


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
#sys.stderr = Logger("D:\\Testlog.txt", sys.stderr)   #Log输出到D盘


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
    try:
        d.app_start('com.xiaomi.wearable')   #com.xiaomi.wearable   com.zhapp.infowear
        d(resourceId="com.xiaomi.wearable:id/main_tv_tab_name", text="设备").click()
        time.sleep(2)
        message = d.toast.get_message(wait_timeout=150)
        if message == "小米运动健康：设备数据同步成功":
            x = x + 1
            print('成功次数', x)
            i = i + 1
            d.toast.reset()
            d.app_stop('com.xiaomi.wearable')
            time.sleep(2)
        elif message == "小米运动健康：设备数据同步失败":
            y = y + 1
            print('失败次数', y)
            i = i + 1
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("picture{}.png".format(nums))
            nums = nums + 1
            d.toast.reset()
            d.app_stop('com.xiaomi.wearable')
            time.sleep(2)
        else:
            z = z + 1
            print('回连失败', z)
            i = i + 1
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("picture{}.png".format(nums))
            nums = nums + 1
            d.toast.reset()
            d.app_stop('com.xiaomi.wearable')
            time.sleep(2)

    except:
        j = j + 1
        print("程序出错导致失败")
        i = i + 1
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        screenmap("picture{}.png".format(nums))
        d.app_stop('com.xiaomi.wearable')
        d.app_start('com.xiaomi.wearable')
        time.sleep(10)


print('成功总次数=', x, '失败总次数=', y, '回连失败=', z, '程序出错=', j)

os.system("pause")
print("按任意键结束")

