import time

import keyboard
from PIL import ImageGrab


class ScreenshotHelper:
    def __init__(self, *, screen_tool='snipaste'):
        self._tool = screen_tool

    @classmethod
    def screenshot(cls):
        keyboard.wait(hotkey="f1")
        keyboard.wait(hotkey="ctrl+c")
        time.sleep(0.01)

    @classmethod
    def save_image(cls, *, image_path=None):
        if image_path is None:
            image_path = "screenshot.png"
        image = ImageGrab.grabclipboard()
        image.save(image_path)
