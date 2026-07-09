import time

import keyboard
import mouse
from song import *


def key_press(args):
    print('长按2s后开始,长按F8停止。')
    time.sleep(2)
    beep_sound()

    for key in args.press:
        try:
            keyboard.press(key)
        except Exception as e:
            beep_sound()
            print(f'Error: {e}')
            return

    while not keyboard.is_pressed('f8'):
        time.sleep(0.1)

    else:
        for key in args.press:
            keyboard.release(key)

        beep_sound()
        print('已停止。')


def mouse_press(args):
    print('长按2s后开始,长按F8停止。')
    time.sleep(2)
    beep_sound()

    for key in args.pmouse:
        try:
            mouse.press(key)
        except Exception as e:
            beep_sound()
            print(f'Error: {e}')
            return

    while not keyboard.is_pressed('f8'):
        time.sleep(0.1)

    else:
        for key in args.pmouse:
            mouse.release(key)

        beep_sound()
        print('已停止。')
