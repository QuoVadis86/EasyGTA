from time import sleep
from conf.config import PROCESS, GTA
from .tools.process import *

class GTA5():
    def __init__(self):
       self.init_process()
    
    def init_process(self):
        self.pids:dict={}
        for name in PROCESS:
            pid = get_pid_by_name(name)
            self.pids[name]=pid

    def suspend(self):
        print(self.pids)
        if not is_suspended(self.pids[GTA]):
            suspend_process(self.pids[GTA])
            sleep(8)
            resume_process(self.pids[GTA])
        resume_process(self.pids[GTA])


    def resume(self):
        resume_process(self.pids[GTA])
       

    def kill(self):
        for name in PROCESS:
            kill_process(self.pids[name])
        