import os
import subprocess
import sys
import uiautomator2 as u2
import time


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        # try:
        self.log = open(fileN, "a+")
        # except:
        #     pass

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def screenmap(file_name):
    # 截图
    os.popen("adb shell screencap /sdcard/{filename}".format(filename=file_name)).read()

    # 截图导出
    os.popen(r"adb pull /sdcard/{filename} {dir}".format(filename=file_name, dir="./sreenshot")).read()

    # 打开截图
    os.popen("adb shell rm /sdcard/{filename}".format(filename=file_name))


print("程序开始运行")
sys.stdout = Logger("./Testlog.txt")  # Log输出到D盘


devices1 = str(subprocess.check_output("adb devices", shell=True)).split('\n')
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
a = int(input('请输入测试表盘传输次数:'))

is_inited = False
while i < a:
    try:
        if is_inited is False:
            is_inited = True
            d.app_stop('com.zjw.noisefitsync')
            d.app_start('com.zjw.noisefitsync')
            time.sleep(10)
            d(resourceId="com.zjw.noisefitsync:id/bottom_menu_img3").click(timeout=15)
            time.sleep(1)
            d(text='表盘中心').click(timeout=15)
            time.sleep(1)
            d(text='在线表盘').click(timeout=15)
            time.sleep(1)
            d(text='树状图表').click(timeout=15)
            time.sleep(1)
            d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
            time.sleep(1)
            message = d.toast.get_message()
            if message == "已存在此表盘":
                d.press('back')
                d(text='我的表盘').click(timeout=15)
                d(text='表盘03').click(timeout=15)
                d(text='删除表盘').click(timeout=15)
                d(text='确定').click(timeout=15)
                d(text='在线表盘').click(timeout=15)
            else:
                d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=120)
                message = d.toast.get_message(wait_timeout=120)
                if message == '已存在此表盘':
                    x = x + 1
                    print('表盘传输成功次数', x)
                    i = i + 1
                    time.sleep(1)
                    d.press('back')
                elif message == '设备超时' or d.toast.get_message() == '同步失败':
                    y = y + 1
                    print('表盘传输失败', y)
                    i = i + 1
                    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                    screenmap("bpone{}.png".format(nums))
                    nums = nums + 1
                    time.sleep(2)
                    d.press('back')
                else:
                    print('其它未知错误')
                    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                    screenmap("bpone{}.png".format(nums))
                    nums = nums + 1
                    i = i + 1
        d(text='轻奢金属').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
        d(text='夜空繁星').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
        d(text='简约表盘').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
        d(text='全能数据').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
        d(text='彩浪').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
        d(text='电子风').click(timeout=15)
        time.sleep(1)
        d(resourceId='com.zjw.noisefitsync:id/btnSync').click(timeout=15)
        time.sleep(1)
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
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            time.sleep(2)
            d.press('back')
        else:
            print('其它未知错误')
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            screenmap("bpone{}.png".format(nums))
            nums = nums + 1
            i = i + 1
    except:
        print("程序出错导致失败")
        i = i + 1
        d.app_stop('com.zhapp.infowear')
        is_inited = False

print('表盘成功总次数=', x, '表盘失败总次数=', y)

os.system("pause")
