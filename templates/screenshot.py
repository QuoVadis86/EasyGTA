

from mss import mss
import numpy as np
import cv2
import json
def capture_full_screen():
    with mss() as sct:
        monitor = sct.monitors[1]  # 使用主显示器
        sct_img = sct.grab(monitor)
        img_np = np.array(sct_img)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)  # 去除Alpha通道
        return img_bgr

def select_roi_and_save_from_screen():
    # 截取全屏画面
    screen_image = capture_full_screen()

    # 显示图像并让用户选择ROI
    roi = cv2.selectROI("Select ROI", screen_image, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()  # 关闭选择窗口

    # 解包roi元组 (x, y, width, height)
    x, y, w, h = roi

    # 构造monitor字典
    monitor = {
        "top": y,
        "left": x,
        "width": w,
        "height": h
    }

    # 将monitor参数保存到文件中
    with open('monitor_params.json', 'w') as f:
        json.dump(monitor, f, indent=4)

    print(f"选定的ROI参数已保存: {monitor}")

if __name__ == "__main__":
    select_roi_and_save_from_screen()