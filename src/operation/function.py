import json
import os
import time
from json import JSONDecodeError
from typing import *

import keyboard
import mouse
from song import *


def load_func(args) -> Optional[list]:
    # noinspection PyBroadException
    try:
        with open(f'func/{args.func}.is', 'r', encoding='utf-8') as func:
            func = json.load(func)
            return func

    except FileNotFoundError:
        print('文件不存在。')
        return None

    except JSONDecodeError:
        print('文件格式错误。')
        return None


def show_func(func) -> None:
    print('已加载宏：')
    for item in func:

        # 显示每个触发键及其对应的操作
        trigger = item.get('trigger', '')
        options = item.get('options', [])

        # 先打印触发键
        print(f"按键 '{trigger}' ->")

        # 再打印每个操作，缩进对齐
        for opt in options:
            if opt.get('key'):
                print(f"\t按键 '{opt['key']}', 间隔 {opt.get('time', 0)}s")
            elif opt.get('mouse'):
                print(f"\t鼠标 '{opt['mouse']}', 间隔 {opt.get('time', 0)}s")


def execute_option(option):
    if option.get('key') and option.get('time') is not None:
        key = option['key']
        interval = option['time']
        keyboard.press_and_release(key)
        time.sleep(interval)
    elif option.get('mouse') and option.get('time') is not None:
        m = option['mouse']
        interval = option['time']
        mouse.click(m)
        time.sleep(interval)


def run_func(func) -> None:
    if type(func) != list:
        return

    beep_sound()
    print('宏模式启动，按下F8退出。')
    show_func(func)

    while not keyboard.is_pressed('F8'):
        for item in func:
            trigger_key = item.get('trigger', None)
            options = item.get('options', [])

            if trigger_key and keyboard.is_pressed(trigger_key):
                for option in options:
                    # 在执行每个选项时也检查 F8
                    if keyboard.is_pressed('F8'):
                        break
                    execute_option(option)

                # 等待触发键释放，避免重复触发（同时检查 F8）
                while keyboard.is_pressed(trigger_key):
                    if keyboard.is_pressed('F8'):
                        break
                    time.sleep(0.05)

                # 如果按下了 F8，立即退出
                if keyboard.is_pressed('F8'):
                    break

        time.sleep(0.01)  # 降低CPU占用

    else:
        print('已退出宏模式。')
        beep_sound()


def view_func():
    beep_sound()
    print('有以下宏文件：')
    for filename in os.listdir('func'):
        if filename.endswith('.is'):
            print(filename[:-3])
