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
j = 0
k = 0
nums = 1
a = int(input('请输入测试OTA次数:'))
while i < a:
    # noinspection PyBroadException
    # 上面注释只是为了except不报格式错误
    try:
        d.app_stop('com.transsion.oraimohealth')
        # com.honbow.fitdock  com.zhapp.infowear  com.honbow.fitdock  com.transsion.oraimohealth
        d(resourceId="com.android.systemui:id/center_group").click()
        d.app_start('com.transsion.oraimohealth')
        time.sleep(6)
        counts = 1
        while True:
            counts = counts + 1
            if d(text='同步成功').exists:
                d(resourceId="com.transsion.oraimohealth:id/rb_device").click()
                break
            elif counts < 200:
                time.sleep(0.1)
            else:
                break
        time.sleep(1)
        d(resourceId="com.transsion.oraimohealth:id/iv_right_arrow").click()
        d.swipe(500, 850, 500, 100, 0.2)
        time.sleep(0.5)
        d.swipe(500, 850, 500, 100, 0.2)
        time.sleep(0.5)
        d.swipe(500, 850, 500, 100, 0.2)
        d(resourceId="com.transsion.oraimohealth:id/tv_title", text="关于设备").click()
        d.xpath(
            '//*[@resource-id="com.transsion.oraimohealth:id/ll_device_about_update"]/android.widget.RelativeLayout[1]'
        ).click()
        d(resourceId="com.transsion.oraimohealth:id/tv_right").click()
        count = 0
        while True:
            count = count + 1
            time.sleep(1)
            if d(text='升级包传输失败').exists:
                x = x + 1
                print('升级包传输失败次数', x)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("picture{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                # d.app_stop('com.transsion.oraimohealth')
                break
            elif d(text='升级包下载失败').exists:
                k = k + 1
                print('升级包下载失败次数', k)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("picture{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                # d.app_stop('com.transsion.oraimohealth')
                break
            elif d(text='升级包传输成功，设备会重启并更新至新版本').exists:
                y = y + 1
                print('OTA成功次数', y)
                i = i + 1
                time.sleep(30)
                # d.app_stop('com.transsion.oraimohealth')
                break
            elif count > 60 * 5:
                z = z + 1
                print('OTA超时次数', z)
                i = i + 1
                print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
                screenmap("picture{}.png".format(nums))
                nums = nums + 1
                time.sleep(2)
                break
    except Exception:
        j = j + 1
        print("其它错误导致失败次数", j)
        i = i + 1
        # d.app_stop('com.transsion.oraimohealth')

print('OTA成功总次数=', y, '升级包下载失败总次数=', k, '升级包传输失败总次数=', x, 'OTA超时次数=', z, '其它错误导致失败=', j)

print("按任意键结束")

os.system("pause")

