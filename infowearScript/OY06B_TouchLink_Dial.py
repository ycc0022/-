import datetime
import time

import uiautomator2 as ut2

# 连接手机 ADB AUMZWGFEUKEAG6NR pip install requests
device = ut2.connect('AUMZWGFEUKEAG6NR')
# 打开被测试的app
device.app_start("com.touch.touchgui", stop=True)
time.sleep(10)
try:
    # 下滑同步
    device.swipe_ext("down")
    device(resourceId="com.touch.touchelex:id/stepsLayout").wait(timeout=None)
except Exception as E:
    # 点击设备
    device(text='设备').click()
print("请输入需要OTA的次数：", end="")
cycle_index = int(input())
failure = 0
times = 0
while times < cycle_index:
    try:
        times = times+1
        # 点击设备
        device(text='设备').click()
        # 点击更多表盘
        device(text='更多表盘').click()
        # 上滑动
        device.swipe_ext("up")
        device.swipe_ext("up")
        device.swipe_ext("up")
        device.swipe_ext("up")
        # 点击简约
        device(text='简约').click()
        # 点击荧光
        device(text='荧光').click()
        device(text="删除").click()
        device(text='下载并使用').click()
        device(text="简约").wait(timeout=120)
        device(resourceId="com.touch.touchgui:id/tv_toolbar_icon").click()

        # 点击科技
        device(text='科技').click()
        # 点击深海
        device(text='深海').click()
        device(text="删除").click()
        device(text='下载并使用').click()
        device(text="科技").wait(timeout=120)
        device(resourceId="com.touch.touchgui:id/tv_toolbar_icon").click()
        time.sleep(3)
        device.app_start("com.touchgui.tool", stop=True)
        time.sleep(7)
        # 点击OTA MODE
        device(text='OTA MODE').click()
        # 点击REBOOT
        device(text='REBOOT').click()
        print('第：', times, '次重启')
        time.sleep(15)
    except Exception as E:
        device.app_start("com.touch.touchgui", stop=True)
        time.sleep(10)
        try:
            # 下滑同步
            device.swipe_ext("down")
            device(resourceId="com.touch.touchelex:id/stepsLayout").wait(timeout=None)
        except Exception as E:
            # 点击设备
            device(text='设备').click()
        print('APP异常：', times)
else:
    print('共传输： ', times, ' 次')
    print('失败：', failure, "次")
