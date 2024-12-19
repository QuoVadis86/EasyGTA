import cv2
import numpy as np
from mss import mss
import os

# 加载预先设定好的图像作为模板，并转换为灰度图
template_path = 'image/t.png'
template = cv2.imread(template_path, 0)
if template is None:
    raise FileNotFoundError(f"无法加载模板图像: {template_path}")

w, h = template.shape[::-1]

# 初始化 mss
sct = mss()

def capture_game_window():
    # 定义截图区域 (根据需要调整)
    monitor = {
        "top": 1360,  # 屏幕高度减去任务栏高度
        "left": 1920,  # 屏幕宽度减去截图宽度
        "width": 78,  # 截图宽度
        "height": 68   # 截图高度，覆盖任务栏
    }
    
    # 截取指定区域的屏幕画面
    sct_img = sct.grab(monitor)

    # 将截图转换为numpy数组，以便OpenCV处理
    img_np = np.array(sct_img)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)  # 去除Alpha通道
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # 转换为灰度图

    return gray, img_bgr  # 返回灰度图和彩色图

def save_screenshot(screenshot, template_path):
    # 构造保存路径（与模板图像同一目录）
    screenshot_dir = os.path.dirname(template_path)
    screenshot_filename = os.path.basename(template_path).replace('.png', '_screenshot.png')
    screenshot_fullpath = os.path.join(screenshot_dir, screenshot_filename)

    # 保存截图
    cv2.imwrite(screenshot_fullpath, screenshot)
    print(f"截图已保存至: {screenshot_fullpath}")

def perform_template_matching(screen_gray):
    print(f"模板图像尺寸: {template.shape}")
    print(f"截图区域尺寸: {screen_gray.shape}")

    # 检查模板图像是否小于截图区域
    if screen_gray.shape[0] < template.shape[0] or screen_gray.shape[1] < template.shape[1]:
        raise ValueError("模板图像太大，无法在截图区域内进行匹配")

    # 执行模板匹配
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)

    # 设定阈值
    threshold = 0.9
    loc = np.where(res >= threshold)

    # 检查是否有匹配的位置
    if len(loc[0]) > 0:
        print("检测到匹配的图像！")
    else:
        print("未检测到匹配的图像。")

if __name__ == "__main__":
    try:
        # 截取游戏窗口画面
        screen_gray, screenshot_color = capture_game_window()
        
        # 保存截图到与模板相同的位置
        save_screenshot(screenshot_color, template_path)
        
        # 进行模板匹配
        perform_template_matching(screen_gray)
    except Exception as e:
        print(f"发生错误: {e}")