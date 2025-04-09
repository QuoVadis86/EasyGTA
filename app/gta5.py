from conf.config import PROCESS, GTA5
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
        suspend_process(self.pids[GTA5])


    def resume(self):
        resume_process(self.pids[GTA5])
       

    def kill(self):
        for name in PROCESS:
            kill_process(self.pids[name])
        