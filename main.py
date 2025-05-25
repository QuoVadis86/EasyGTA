import run
from app import ui
from app.gta5 import GTA5
from app.input import Listener
from app.input import Controller

if __name__ == "__main__":
    run.controller = Controller()
    run.gta5 = GTA5()
    run.listener = Listener()
    run.listener.start()
    ui.create_ui()
    # demo.create_ui()
