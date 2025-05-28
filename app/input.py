from threading import Thread
from time import sleep
from pynput import keyboard, mouse
import logging
from scripts import *
from config.config import load_config
from app.tools.utils import game_focused


class Controller:
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        logging.info("初始化输入控制器")

    def press(self, key):
        self.keyboard.press(key)

    def release(self, key):
        self.keyboard.release(key)

    def press_and_release(self, key, delay: float = 0):
        self.keyboard.press(key)
        sleep(delay)
        self.keyboard.release(key)

    def ahk(self, key, times: int = 1, delay: float = 0):
        for _ in range(times):
            self.press_and_release(key)
            sleep(delay)


class Listener:
    is_hack_speed = False
    current_weapon = "6"

    def __init__(self):
        self.initializes()
        logging.info("初始化监听器")

    def initializes(self):
        self.keyboard = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.mouse = mouse.Listener(on_click=self.on_click)
        self.config = load_config()
        print("---------->", self.config)

    def start(self):
        self.keyboard.start()
        self.mouse.start()
        logging.info("监听器已启动")

    def destroy(self):
        self.keyboard.stop()
        self.mouse.stop()
        logging.info("监听器已销毁")

    def restart(self):
        self.destroy()
        self.initializes()
        self.start()

    def on_click(self, x, y, button, pressed):
        # if game_focused():
        if not game_focused():
            return
        if pressed:
            if button.name == format(self.config.get("start_engine")):
                print("start_engine")
                start_egine()
            if button.name == format(self.config.get("kill_gta")):
                print("kill_gta")
                kill_gta()
            if button.name == format(self.config.get("suspend_gta")):
                print("suspend_gta")
                Thread(target=suspend_gta).start()
                # suspend_gta()
            if button.name == format(self.config.get("block_net")):
                print("block_net")
                block_net()
            if button.name == format(self.config.get("limit_net")):
                print("limit_net")
                limit_net()
            if format(button.name) == format(self.config.get("hack_speed")):
                print("hack_speed", button.__dict__)
                self.is_hack_speed = True
                Thread(target=hack_speed).start()
            if format(button.name) == format(self.config.get("eat_snack")):
                print("eat_snack")
                eat_snack()
            if format(button.name) == format(self.config.get("select_unarmed")):
                print("select_unarmed")
                select_unarmed()
            pass
            # if button ==AB.Start_Engine:
            #     Thread(target=start_egine).start()
            # else:
            #     pass
        else:
            if format(button.name) == format(self.config.get("hack_speed")):
                self.is_hack_speed = False

                print("hack_speed stop")
                print("hack_speed", button)

        # else:
        # pass
        # print(button)

    def on_press(self, key):
        if not game_focused():
            return
        try:

            if format(key.name) == format(self.config.get("start_engine")):
                print("start_engine")
                start_egine()
            if format(key.name) == format(self.config.get("kill_gta")):
                print("kill_gta")
                kill_gta()
            if format(key.name) == format(self.config.get("suspend_gta")):
                print("suspend_gta")
                Thread(target=suspend_gta).start()
            if format(key.name) == format(self.config.get("block_net")):
                print("block_net")
                block_net()
            if format(key.name) == format(self.config.get("limit_net")):
                print("limit_net")
                limit_net()
            if format(key.name) == format(self.config.get("hack_speed")):
                print("hack_speed")
                press_weapon_wheel()
            if format(key.name) == format(self.config.get("eat_snack")):
                print("eat_snack")
                eat_snack()
            if format(key.name) == format(self.config.get("select_unarmed")):
                print("select_unarmed")
                select_unarmed()
        except AttributeError:
            if not eval(self.config.get("auto_close")):
                return
            if 48 <= key.vk <= 57:
                if key.vk == int(self.config.get("special_weapon")):
                    return
                self.current_weapon = str(key.vk - 48)
                press_weapon_wheel()
            pass

    def on_release(self, key):
        pass

    def get_key(self, binding_key: str):
        if not binding_key:
            return
        if len(binding_key) == 1:
            print(f"{binding_key} is a char key")
            binding_key = keyboard.KeyCode.from_char(binding_key)
        elif hasattr(
            keyboard.Key, format(binding_key)
        ):  # 检查是否是pynput预定义的特殊键
            print(f"{binding_key} is a function key")
            binding_key = getattr(keyboard.Key, format(binding_key))
        else:
            binding_key = None
            print("binding_key is not a valid key")
        return binding_key


def format(key: str) -> str:
    if not key:
        return
    return key.split(".")[-1].lower()


if __name__ == "__main__":
    # Listener()
    pass
