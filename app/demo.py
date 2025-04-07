import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
import threading
import run
from conf import binding
from scripts import restart, exit_app, pause

def format(key):
    """格式化键名显示"""
    return str(key).split(".")[-1].capitalize()

class AppTray:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口
        
        # 加载托盘图标
        self.image = Image.open("png/icon.png")
        print(self.image)
        self.tray_icon = ImageTk.PhotoImage(self.image)
        
        # 创建系统托盘图标
        self.tray = tk.Label(self.root, image=self.tray_icon)
        self.tray.pack()
        
        # 绑定右键菜单
        self.tray.bind("<Button-3>", self.show_menu)  # 右键点击
        
        # 保持程序运行
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        
    def update_key(self, key, value):
        """更新键值回调"""
        print(key, value)
        return False  # 阻止菜单关闭
    
    def show_menu(self, event):
        """显示右键菜单"""
        menu = Menu(self.root, tearoff=0)
        
        # 功能子菜单
        submenu = Menu(menu, tearoff=0)
        submenu.add_command(
            label=f"启动引擎: {format(binding.App.Start_Engine)}",
            command=lambda: self.update_key("start_engine", 1)
        )
        submenu.add_command(
            label=f"断游戏: {format(binding.App.Kill)}",
            command=lambda: self.update_key("del", 1)
        )
        submenu.add_command(
            label=f"限制网络: {format(binding.App.Net_Limit)}",
            command=lambda: self.update_key("limit", 1)
        )
        submenu.add_command(
            label=f"卡单人占据: {format(binding.App.Suspend)}",
            command=lambda: self.update_key("singlee", 1)
        )
        menu.add_cascade(label="功能", menu=submenu)
        
        # 其他选项
        menu.add_command(label="重新加载", command=restart)
        menu.add_command(label="暂停", command=pause)
        menu.add_separator()
        menu.add_command(label="退出", command=self.on_exit)
        
        # 在鼠标位置显示菜单
        menu.post(event.x_root, event.y_root)
    
    def on_exit(self):
        """退出程序"""
        if messagebox.askokcancel("退出", "确定要退出吗？"):
            self.root.quit()
            exit_app()
    
    def run(self):
        """运行托盘图标"""
        self.root.mainloop()

# 创建并运行托盘图标
def create_ui():
    app = AppTray()
    app.run()

# 启动托盘（可在主线程或子线程运行）
if __name__ == "__main__":
    create_ui()