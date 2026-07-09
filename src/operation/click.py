import keyboard
import mouse
import time
from song import *


def key_click(args):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    running = True
    while running:
        # 执行一次按键序列
        for key in args.key:
            try:
                keyboard.send(key)
            except Exception as e:
                beep_sound()
                print(f'Error: {e}')
                return

            # 每按一次键都检查 F8
            if keyboard.is_pressed('f8'):
                running = False
                break

        # 拆分 sleep，避免阻塞 F8 检测
        if running:
            elapsed = 0.0
            interval = 0.05  # 50ms 检查一次
            while elapsed < args.time and running:
                if keyboard.is_pressed('f8'):
                    running = False
                    break
                time.sleep(interval)
                elapsed += interval

    beep_sound()
    print('已停止。')


def mouse_click(args):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    running = True
    while running:
        # 执行一次鼠标点击序列
        for key in args.mouse:
            try:
                mouse.click(key)
            except Exception as e:
                beep_sound()
                print(f'Error: {e}')
                return

            if keyboard.is_pressed('f8'):
                running = False
                break

        # 拆分 sleep
        if running:
            elapsed = 0.0
            interval = 0.05
            while elapsed < args.time and running:
                if keyboard.is_pressed('f8'):
                    running = False
                    break
                time.sleep(interval)
                elapsed += interval

    beep_sound()
    print('已停止。')
