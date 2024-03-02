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
          'appPackage': 'com.zhapp.infowear',  # 启动APP Package名称
          'appActivity': '.ui.WelcomeActivity',  # 启动Activity名称
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
#        cls.driver.find_element_by_class_name("android.widget.Button").click()  # 测试版本加本行代码，非测试版本不用

    @classmethod
    def tearDownClass(cls):
        print("over")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dttest('test_clickmbsd'))

    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open('./report/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="Infowear",
                            description="运行环境：Windows 10, 小米9SE"
                            )

    runner.run(suite)
    fp.close()