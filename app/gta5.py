from time import sleep
from config.config import PROCESS, GTA, GTA_ENHANCED
from .tools.process import *


class GTA5:
    def __init__(self):
        self.init_process()

    def init_process(self):
        self.pids: dict = {}
        for name in PROCESS:
            pid = get_pid_by_name(name)
            self.pids[name] = pid

    def suspend(self):
        print(self.pids)
        gta5_pid = self.pids[GTA_ENHANCED] or self.pids[GTA]
        if not is_suspended(gta5_pid):
            suspend_process(gta5_pid)
            sleep(8)
            resume_process(gta5_pid)
        resume_process(gta5_pid)

    def resume(self):
        gta5_pid = self.pids[GTA_ENHANCED] or self.pids[GTA]
        resume_process(gta5_pid)

    def kill(self):
        for name in PROCESS:
            kill_process(self.pids[name])
