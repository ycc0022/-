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
z = 0
nums = 1
a = int(input('请输入测试OTA次数:'))
while i < a:
    d.app_stop('com.honbow.fitdock')    #com.honbow.fitdock    com.zhapp.infowear
    d.app_start('com.honbow.fitdock')
    time.sleep(2)
    try:
        d(text='设备').click()
        d(text='确定').click(timeout=60)
        # now = time.localtime()

        '''
        d(text='启用中').click(timeout=15)
        time.sleep(1)
        d.swipe_ext("up")
        time.sleep(1)
        d(text='更多设置').click(timeout=60)
        time.sleep(1)
        d(text='设备固件更新').click(timeout=15)
        time.sleep(1)
        d(text='立即前往').click(timeout=15)
        time.sleep(3)
'''
        count = 0
        while True:
            count = count + 1
            time.sleep(1)
            if d(text='固件升级失败，请重试。[-1]').exists or d(text='下载失败请重试').exists:
                x = x + 1
                print('OTA失败次数', x)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("bpone{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                d.app_stop('com.honbow.fitdock')
                break
            elif d(text='已连接').exists:
                y = y + 1
                print('OTA成功次数', y)
                i = i + 1
                time.sleep(2)
                d.app_stop('com.honbow.fitdock')
                break
            elif count > 60 * 5:
                z = z + 1
                print('OTA超时次数', z)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("bpone{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                break

            '''
            elif d(text='升级失败，请重新升级').exists:
                y = y + 1
                print('OTA失败次数', y)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("bpone{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                break
            elif count > 60*2:
                z = z + 1
                print('OTA超时次数', z)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("bpone{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                break
'''

        # d.app_stop('com.zhapp.infowear')
    except:
        print("脚本出错导致失败")
        d.app_stop('com.honbow.fitdock')

print('OTA成功总次数=', y, 'OTA失败总次数=', x, 'OTA超时次数=', z)

os.system("pause")
print("按任意键结束")
