import os
import sys
import shutil
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

GAME_NAME = "Grand Theft Auto V"
GTA5 = "GTA5.exe"
BE="GTA5_BE.exe"
LAUNCHER = "Launcher.exe"
PLAY_GTA5 = "PlayGTAV.exe"
ROCKSTAR_SERVICE = "RockstarService.exe"
ERROR_HANDLER = "RockstarErrorHandler.exe"
SC_HELPER = "SocialClubHelper.exe"

PROCESS=[GTA5, BE, LAUNCHER, PLAY_GTA5, ROCKSTAR_SERVICE, ERROR_HANDLER, SC_HELPER]


def get_external_config_path():
    """返回外部配置文件的绝对路径（用户可修改的位置）"""

    if getattr(sys, 'frozen', False):
        # 打包后，使用 sys.executable 的目录
        base_dir = Path(sys.executable).parent
    else:
        # 开发时，使用当前脚本的目录
        base_dir = Path(__file__).parent
    # base_dir=base_dir / "default.ini"  # 配置文件目录
    base_dir.mkdir(parents=True, exist_ok=True)  # 确保目录存在
    return base_dir / "default.ini"  # 配置文件路径

    # config_dir = Path(os.getenv('APPDATA')) / "YourAppName"
    # config_dir.mkdir(parents=True, exist_ok=True)  # 确保目录存在
    # return config_dir / "config.ini"

def init_config():
    """初始化配置：如果外部配置不存在，则从内部默认配置复制"""
    external_config = get_external_config_path()
    
    # 如果外部配置不存在，且程序是打包后的
    if not external_config.exists() and getattr(sys, 'frozen', False):
        internal_config = Path(sys._MEIPASS) / "default.ini"
        if internal_config.exists():
            shutil.copy(internal_config, external_config)
            print(f"初始化配置：已从内部复制到 {external_config}")
    
    return external_config

def load_config():
    """加载配置文件（始终读取外部配置）"""
    config_file = init_config()  # 确保配置已初始化
    with open(config_file, 'r') as f:
        return f.read()

# 使用示例
if __name__ == "__main__":
    config_path = init_config()
    print("配置文件路径:", config_path)
    
    # 读取配置
    config_content = load_config()
    print("配置内容:", config_content)
    
    # 修改配置（会写入外部文件）
    with open(config_path, 'w') as f:
        f.write("new_value=123")