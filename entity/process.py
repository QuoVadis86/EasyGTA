from psutil import process_iter, Process, STATUS_STOPPED

from conf.config import *


class GTA():
    def __init__(self):
        self.init_process()

    def suspend_process(self, pid: int):
        try:
            Process(pid).suspend()
            print(f"进程已挂起")
        except Exception as e:
            print(f"无法挂起进程: {e}")

    def is_suspended(self, pid: int):
        try:
            status = Process(pid).status()
            return status == STATUS_STOPPED
        except Exception as e:
            print("No process found with PID:", e)
            return False

    def resume_process(self, pid: int):
        try:
            Process(pid).resume()
            print(f"进程已恢复")
        except Exception as e:
            print(f"无法恢复进程: {e}")

    def kill_process(self, pid: int):
        try:
            Process(pid).terminate()
            print(f"进程已结束")
        except Exception as ex:
            print(f"无法结束进程{ex}")

    def get_pid_by_name(self, name: str):
        for process in process_iter(["pid", "name"]):
            if process.info["name"] == name:
                print(f"进程{name}的pid为: {process.info["pid"]}")
                return process.info["pid"]
        print("没有找到该进程")
        return None

    def init_process(self):
        # pass
        self.gta5 = self.get_pid_by_name(GTA5)
        self.be = self.get_pid_by_name(BE)
        self.launcher = self.get_pid_by_name(LAUNCHER)
        self.play_gta5 = self.get_pid_by_name(PLAY_GTA5)
        self.rockstar_service = self.get_pid_by_name(ROCKSTAR_SERVICE)
        self.error_handler = self.get_pid_by_name(ERROR_HANDLER)
        self.sc_helper = self.get_pid_by_name(SC_HELPER)

    def is_suspended(self,pid):
        try:
            status = Process(pid).status()
            return status == STATUS_STOPPED
        except Exception as e:
            print("No process found with PID:", e)
            return False
