import run
from app.ui import init
from app.gta5 import GTA5
from app.input import Listener
from app.input import Controller

if __name__ == "__main__":
    run.controller = Controller()
    run.gta5 = GTA5()
    run.listener = Listener()
    init()
    run.listener.start()
