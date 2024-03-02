import unittest
from appium import webdriver
from time import sleep
from HTMLTestRunner import HTMLTestRunner
import time
from appium.webdriver.common.touch_action import TouchAction
#  写在前面，将手机USB调试权限打开，将充电不熄屏打开，已经绑定手环，更好AGPS


class Dttest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("start setup")
        desired_caps = {
          'platformName': 'Android',  # 被测手机是安卓
          'platformVersion': '10',  # 手机安卓版本
          'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
          'appPackage': 'com.zjw.apps3pluspro',  # 启动APP Package名称
          'appActivity': '.SplashActivity',  # 启动Activity名称
          'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
          'resetKeyboard': True,  # 执行完程序恢复原来输入法
          'noReset': True,       # 不要重置App
          'newCommandTimeout': 6000,
          'automationName': 'UiAutomator2'
          }
    # 连接Appium Server，初始化自动化环境
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 设置缺省等待时间
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_class_name("android.widget.Button").click()  # 测试版本加本行代码，非测试版本不用

    # subprocess.call("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE",shell=Ture)    #打开蓝牙开关
    # driver.find_element_by_id("android:id/button1").click() #提示框点击是
    @classmethod
    def tearDownClass(cls):
        print("over")

    def test_clickmbsd(self):
        """" 点击：目标设定 """
        self.driver.find_element_by_id("layoutPen").click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "目标设定")

    def test_ydmbqd(self):
        """" 点击运动目标，滑动后，‘确定’ """
        self.driver.find_element_by_id("layoutStep").click()
        sleep(1)
        self.driver.swipe(550, 2000, 550, 1800, duration=3000)
        sleep(2)
        self.driver.find_element_by_id("tvOk").click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "目标设定")

    def test_ydmbqx(self):
        """" 点击：运动目标，滑动后，‘取消’ """
        self.driver.find_element_by_id("layoutStep").click()
        sleep(1)
        self.driver.swipe(550, 2000, 550, 1800, duration=3000)
        sleep(1)
        self.driver.find_element_by_id("tvCancel").click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "目标设定")

    def test_smmbqd(self):
        """" 点击：睡眠目标，滑动后，‘确定’ """
        self.driver.find_element_by_id("layoutSleep").click()
        sleep(1)
        self.driver.swipe(550, 2000, 550, 1800, duration=3000)
        sleep(2)
        self.driver.find_element_by_id("tvOk").click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "目标设定")

    def test_smmbqx(self):
        """" 点击：睡眠目标，滑动后，‘取消’ """
        self.driver.find_element_by_id("layoutSleep").click()
        sleep(1)
        self.driver.swipe(550, 2000, 550, 1800, duration=3000)
        sleep(1)
        self.driver.find_element_by_id("tvCancel").click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "目标设定")

    def test_fh(self):
        """" 点击：返回活动页面 """
        self.driver.find_element_by_id("public_head_back").click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "活动")

    def test_rchd(self):
        """" 点击：进入日常活动页面 """
        self.driver.find_element_by_id('layoutExercise').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "日常活动")

    def test_rchdrl(self):
        """" 点击：日常活动页面日历，左右滑动后，返回活动页面 """
        self.driver.find_element_by_id('layoutCalendar').click()
        sleep(1)
        self.driver.swipe(1000, 600, 100, 600, duration=3000)
        sleep(1)
        self.driver.swipe(100, 600, 1000, 600, duration=3000)

        self.driver.find_element_by_id('public_head_back').click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "活动")

    def test_sm(self):
        """" 点击：进入睡眠页面 """
        self.driver.find_element_by_id('layoutSleep').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "睡眠")

    def test_smrl(self):
        """" 点击：睡眠页面日历，左右滑动后，返回活动页面 """
        self.driver.find_element_by_id('layoutCalendar').click()
        sleep(1)
        self.driver.swipe(1000, 600, 100, 600, duration=3000)
        sleep(1)
        self.driver.swipe(100, 600, 1000, 600, duration=3000)

        self.driver.find_element_by_id('public_head_back').click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "活动")

    def test_xl(self):
        """" 点击：进入心率页面 """
        self.driver.find_element_by_id('layoutHeart').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "心率")

    def test_xlrl(self):
        """" 点击：心率页面日历，左右滑动后，返回活动页面 """
        self.driver.find_element_by_id('layoutCalendar').click()
        sleep(1)
        self.driver.swipe(1000, 600, 100, 600, duration=3000)
        sleep(1)
        self.driver.swipe(100, 600, 1000, 600, duration=3000)

        self.driver.find_element_by_id('public_head_back').click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "活动")

    def test_yd(self):
        """" 点击：进入运动页面 """
        self.driver.find_element_by_id('layoutSportCard').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "运动历史")

    def test_ydrl(self):
        """" 点击：运动历史页面日历，左右滑动后，返回活动页面 """
        self.driver.find_element_by_id('layoutCalendar').click()
        sleep(1)
        self.driver.swipe(1000, 600, 100, 600, duration=3000)
        sleep(1)
        self.driver.swipe(100, 600, 1000, 600, duration=3000)

        self.driver.find_element_by_id('public_head_back').click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "活动")

    def test_sz(self):
        """" 点击：设置栏，进入设置页面 """
        self.driver.find_element_by_id('bootom_menu_lin2').click()
        self.bt = self.driver.find_element_by_id('tvTitleTop')
        self.assertEqual(self.bt.text, "设置")

    def test_bpzx(self):
        """" 点击：进入表盘中心后返回 """
        self.driver.find_element_by_id('tvTitle').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "表盘市场")
        self.driver.find_element_by_id('public_head_back').click()

    def test_xxtz(self):
        """" 点击：进入消息通知后返回 """
        self.driver.find_element_by_id('tvTitle1').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "消息通知")
        self.driver.find_element_by_id('public_head_back').click()

    def test_txsz(self):
        """" 点击：进入提醒设置后返回 """
        self.driver.find_element_by_id('tvTitle2').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "提醒设置")
        self.driver.find_element_by_id('public_head_back').click()

    def test_lxxl(self):
        """" 打开连续心率后关闭,然后点击查找手机 """
        sleep(1)
        self.driver.find_element_by_class_name('android.widget.Switch').click()
        sleep(1)
        self.driver.find_element_by_id('tvOk').click()
        self.driver.find_element_by_id('scContinuousHeart').click()
        self.driver.find_element_by_id('tvTitle7').click()

    def test_gdsz(self):
        """" 点击：进入更多设置后返回 """
        self.driver.find_element_by_id('tvTitle10').click()
        self.bt = self.driver.find_element_by_id('public_head_title')
        self.assertEqual(self.bt.text, "更多设置")
        self.driver.find_element_by_id('public_head_back').click()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dttest('test_clickmbsd'))
    suite.addTest(Dttest('test_ydmbqd'))  # 网络原因 可能出现错误
    suite.addTest(Dttest('test_ydmbqx'))
    suite.addTest(Dttest('test_smmbqd'))  # 网络原因 可能出现错误
    suite.addTest(Dttest('test_smmbqx'))
    suite.addTest(Dttest('test_fh'))
    suite.addTest(Dttest('test_rchd'))
    suite.addTest(Dttest('test_rchdrl'))
    suite.addTest(Dttest('test_sm'))
    suite.addTest(Dttest('test_smrl'))
    suite.addTest(Dttest('test_xl'))
    suite.addTest(Dttest('test_xlrl'))
    suite.addTest(Dttest('test_yd'))
    suite.addTest(Dttest('test_ydrl'))
    suite.addTest(Dttest('test_sz'))
    suite.addTest(Dttest('test_bpzx'))
    suite.addTest(Dttest('test_xxtz'))
    suite.addTest(Dttest('test_txsz'))
    suite.addTest(Dttest('test_lxxl'))
    suite.addTest(Dttest('test_gdsz'))

#   suite.addTest(Dttest())


#    unittest.TextTestRunner(verbosity=1).run(suite)
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open('./report/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="3+PRO",
                            description="运行环境：Windows 10, redmi10X"
                            )

    runner.run(suite)
    fp.close()
