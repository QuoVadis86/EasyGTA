import os
import sys
import shutil
import logging
from pathlib import Path
import json
from .binding import App

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

GAME_NAME = "Grand Theft Auto V"
GTA = "GTA5.exe"
BE = "GTA5_BE.exe"
GTA_ENHANCED = "GTA5_Enhanced.exe"
BE_ENHANCED = "GTA5_Enhanced_BE.exe"
LAUNCHER = "Launcher.exe"
PLAY_GTA5 = "PlayGTAV.exe"
ROCKSTAR_SERVICE = "RockstarService.exe"
ERROR_HANDLER = "RockstarErrorHandler.exe"
SC_HELPER = "SocialClubHelper.exe"

PROCESS = [
    GTA,
    BE,
    GTA_ENHANCED,
    BE_ENHANCED,
    LAUNCHER,
    PLAY_GTA5,
    ROCKSTAR_SERVICE,
    ERROR_HANDLER,
    SC_HELPER,
]


def get_external_config_path():
    """返回外部配置文件的绝对路径（用户可修改的位置）"""

    if getattr(sys, "frozen", False):
        # 打包后，使用 sys.executable 的目录
        base_dir = Path(sys.executable).parent
    else:
        # 开发时，使用当前脚本的目录
        base_dir = Path(__file__).parent
    base_dir.mkdir(parents=True, exist_ok=True)  # 确保目录存在
    return base_dir / "default.json"  # 配置文件路径


def init_config():
    """初始化配置：如果外部配置不存在，则从内部默认配置复制"""
    external_config = get_external_config_path()
    logging.info(f"External config path: {external_config}")

    if not external_config.exists():
        logging.info("External config does not exist. Creating default config.")
        default_config = {}
        for key, value in vars(App).items():
            if key.startswith("__"):
                continue
            default_config[key] = str(value)
        with open(external_config, "w", encoding="utf-8") as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
        logging.info(f"Default config created at {external_config}")
    else:
        logging.info("External config already exists.")

    return external_config


def load_config() -> dict:
    """加载配置文件（始终读取外部配置）"""
    config_file = init_config()  # 确保配置已初始化
    logging.info(f"Loading config from {config_file}")
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f)


# 使用示例
if __name__ == "__main__":
    config_path = init_config()
    print("配置文件路径:", config_path)

    # 读取配置
    config_content = load_config()
    print("配置内容:", config_content)
    print("配置内容类型:", type(config_content))

    # # 修改配置（会写入外部文件）
    # with open(config_path, 'w', encoding='utf-8') as f:
    #     json.dump(config_content, f, ensure_ascii=False, indent=4)
