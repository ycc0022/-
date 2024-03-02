import time
import keyboard

print("当按下F9程序不断按1，,再次按下F9暂停，F7退出程序")

# 设置一个标志变量，用于控制循环是否运行
running = False


def toggle_running():
    global running
    running = not running


# 注册F9和F7键的热键回调函数
keyboard.add_hotkey('F9', toggle_running)
keyboard.add_hotkey('F7', lambda: exit())

while True:
    # 如果标志变量为True，则每隔0.2秒按下键盘1
    if running:
        keyboard.press_and_release('1')
        time.sleep(0.2)