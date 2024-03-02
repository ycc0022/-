import keyboard
import time
import threading

print('当按下键盘1就循环1 再次按下键盘1就停，当按下2就循环键盘2 再次按下键盘2就停，按下F9程序停止运行')

# 定义全局变量和标志
running = False
active_key = None
interval = 0.3


# 函数来执行按键的操作
def key_action(key_to_press):
    while running and active_key == key_to_press:
        keyboard.press(key_to_press)
        time.sleep(interval)
        keyboard.release(key_to_press)


# 监听键盘事件的回调函数
def key_event(e):
    global running, active_key

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "f9":
            if not running:
                running = True
                active_key = None
            else:
                running = False
        elif running:
            if e.name == "1":
                if active_key != "1":
                    active_key = "1"
                    threading.Thread(target=key_action, args=("1",)).start()
                else:
                    active_key = None
            elif e.name == "2":
                if active_key != "2":
                    active_key = "2"
                    threading.Thread(target=key_action, args=("2",)).start()
                else:
                    active_key = None
            elif e.name == "3":
                if active_key != "3":
                    active_key = "3"
                    threading.Thread(target=key_action, args=("3",)).start()
                else:
                    active_key = None
            elif e.name == "5":
                if active_key != "5":
                    active_key = "5"
                    threading.Thread(target=key_action, args=("5",)).start()
                else:
                    active_key = None


# 停止程序的函数
def stop_program():
    global running
    running = False
    keyboard.unhook_all()


# 监听键盘事件
keyboard.hook(key_event)

# 让程序保持运行
while True:
    time.sleep(1)
