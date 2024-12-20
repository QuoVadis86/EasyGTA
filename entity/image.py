import cv2
import numpy as np
from mss import mss
import os

class Image():
    def __init__(self):
        self.sct=mss()

    def capture_game_window(self,monitor:dict):
        # 定义截图区域 (根据需要调整)
    #     monitor = {
    #     "top": 504,
    #     "left": 938,
    #     "width": 694,
    #     "height": 470
    # }
        # 截取指定区域的屏幕画面
        sct_img = self.sct.grab(monitor)

        # 将截图转换为numpy数组，以便OpenCV处理
        img_np = np.array(sct_img)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)  # 去除Alpha通道
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # 转换为灰度图

        return gray, img_bgr  # 返回灰度图和彩色图

    def save_screenshot(self,screenshot, template_path):
        # 构造保存路径（与模板图像同一目录）
        screenshot_dir = os.path.dirname(template_path)
        screenshot_filename = os.path.basename(template_path).replace('.png', '_screenshot.png')
        screenshot_fullpath = os.path.join(screenshot_dir, screenshot_filename)

        # 保存截图
        cv2.imwrite(screenshot_fullpath, screenshot)
        print(f"截图已保存至: {screenshot_fullpath}")

    def perform_template_matching(self,monitor:dict,template_path)->bool:
        """
        moitor:被截图区域
        template:被对比的模版
        
        """

        template = cv2.imread(template_path, 0)
        if template is None:
            raise FileNotFoundError(f"无法加载模板图像: {template_path}")
        
        #获取灰度图
        screen_gray, screenshot_color = self.capture_game_window(monitor)
        
        print(f"模板图像尺寸: {template.shape}")
        print(f"截图区域尺寸: {screen_gray.shape}")

        # 检查模板图像是否小于截图区域
        if screen_gray.shape[0] < template.shape[0] or screen_gray.shape[1] < template.shape[1]:
            raise ValueError("模板图像太大，无法在截图区域内进行匹配")

        # 执行模板匹配
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        # 设定阈值
        threshold = 0.8
        loc = np.where(res >= threshold)

        # 检查是否有匹配的位置
        if len(loc[0]) > 0:
            print("检测到匹配的图像！")
            return True
        print("没有检测到匹配的图像！")
        return False
