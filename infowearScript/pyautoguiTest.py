import pyautogui
import random
x, y = pyautogui.position()
print("x轴位置：{}，y轴位置：{}".format(x, y))

x, y = pyautogui.size()
print("当前屏幕分辨率是{}*{}".format(x, y))

pyautogui.moveTo(x=300, y=300, duration=0.25)

# pyautogui.click(x=100, y=100, button='left')
pyautogui.doubleClick(x=100, y=100, button='left')

# pyautogui.hotkey('win', "d")
i = 0
nums = 1
for i in range(10):
    img_path = r'D:\pythonProject-infowear\infowearScript\sreenshot\{}.png'.format(nums)
    nums += 1
    im = pyautogui.screenshot()
    im.save(img_path)
    i += 1
