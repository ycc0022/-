import datetime
import time

import uiautomator2 as ut2

# 连接手机 ADB
device = ut2.connect('b97c2659')
# 打开被测试的app  adb shell am monitor
device.app_start("com.touch.touchgui", stop=True)
# 未连接的次数
failure = 0
successful = 0
avg = 0
unusual = 0
# 需要OTA的次数
print("请输入需要OTA的次数：", end="")
cycle_index = int(input())
times = 0
while times < cycle_index:
    try:
        try:
            times = times + 1
            # 点击设备
            device(text='设备').click()
            time.sleep(3)
            device.swipe_ext("down")
            device.click(899, 374)
            time.sleep(5)
            # 上滑找到设备设置
            device.swipe_ext("up")
            # 点击设备更多设置
            device(text='设备更多设置').click()
            # 点击OTA升级
            time.sleep(3)
            device.click(76, 204)
            time.sleep(3)
            device(text='设备更多设置').click()
            time.sleep(3)
            device(text='OTA升级').click(timeout=None)
            # 点击开始升级
            time.sleep(5)
            device(text='开始升级').click(timeout=5)
            start = datetime.datetime.now()
            try:
                # 设置6分钟最大等待时间，如果6分钟内出现则点击完成
                device(text="恭喜你，升级已完成").wait(timeout=360)
            except Exception as E:
                # 异常加一
                failure = failure + 1
                device.app_stop('com.touch.touchgui')
                time.sleep(5)
                device.app_start("com.touch.touchgui", stop=True)
                time.sleep(15)
                continue
            # 结束时间
            end = datetime.datetime.now()
            # 平均时间的每次累加
            avg = end - start
            print('第', times, '次花费的时间：', end - start)
            device(text="确定").click()
            # 手表重启需要一个等待时间
            time.sleep(25)
            # 前面重启了，说明成功了+1
            successful = successful+1
        except Exception as E:
            # 异常加一
            unusual = unusual + 1
            device.app_stop('com.touch.touchgui')
            time.sleep(5)
            device.app_start("com.touch.touchgui", stop=True)
            time.sleep(15)
            continue
    except E:
        unusual = unusual + 1
        device.app_stop('com.touch.touchgui')
        time.sleep(5)
        device.app_start("com.touch.touchgui", stop=True)
        time.sleep(15)
        continue
else:
    print('共OTA： ', times, ' 次')
    print('成功：', successful, "次")
    print('失败：', failure, "次")
    print('APP异常：', unusual, "次")
    print('平均时间：', (avg/times))