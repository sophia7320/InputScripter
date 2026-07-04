import keyboard
import mouse
import time
from song import *


def key_click(args, standard_keys):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    running = True
    while running:
        # 执行一次按键序列
        for key in args.key:
            if key in standard_keys:
                keyboard.press_and_release(key)

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


def mouse_click(args, standard_mouse):
    print('连点2s后开始，长按F8停止。')
    time.sleep(2)
    beep_sound()

    running = True
    while running:
        # 执行一次鼠标点击序列
        for key in args.mouse:
            if key in standard_mouse:
                mouse.click(key)

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
