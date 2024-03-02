import keyboard
import time
import threading
import sys

print('当按下键盘1就循环1 再次按下键盘1就停，当按下2就循环键盘2 再次按下键盘2就停，按下F7程序停止运行')


running = True
active_key = None
interval = 0.2


def key_action(key_to_press):
    while running and active_key == key_to_press:
        keyboard.press(key_to_press)
        time.sleep(interval)
        keyboard.release(key_to_press)


def key_event(e):
    global active_key

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "f7":
            stop_program()
        elif e.name == "1":
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
        # elif e.name == "3":
        #     if active_key != "3":
        #         active_key = "3"
        #         threading.Thread(target=key_action, args=("3",)).start()
        #     else:
        #         active_key = None
        # elif e.name == "4":
        #     if active_key != "4":
        #         active_key = "4"
        #         threading.Thread(target=key_action, args=("4",)).start()
        #     else:
        #         active_key = None
        elif e.name == "5":
            if active_key != "5":
                active_key = "5"
                threading.Thread(target=key_action, args=("5",)).start()
            else:
                active_key = None


def stop_program():
    global running
    running = False
    keyboard.unhook_all()


keyboard.hook(key_event)

# 让程序保持运行
while running:
    time.sleep(1)

print("程序已停止运行")
sys.exit()
