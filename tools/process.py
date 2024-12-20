from psutil import iter, Process,STATUS_STOPPED

from ..conf.config import Names

class GTA5:
    def __init__(self):
        self.game_name = Names.GAME_NAME
        self.gta5 = self.get_pid_by_name(Names.GTA5)
        self.be = self.get_pid_by_name(Names.BE)
        self.launcher = self.get_pid_by_name(Names.LAUNCHER)
        self.play_gta5 = self.get_pid_by_name(Names.PLAY_GTA5)
        self.rockstar_service = self.get_pid_by_name(Names.ROCKSTAR_SERVICE)
        self.error_handler = self.get_pid_by_name(Names.ERROR_HANDLER)
        self.sc_helper = self.get_pid_by_name(Names.SC_HELPER)

    def suspend_process(self,pid:int):
        try:
            Process(pid).suspend()
            print(f"进程已挂起")
        except Exception as e:
            print(f"无法挂起进程: {e}")


    def resume_process(self,pid:int):
        try:
            Process(pid).resume()
            print(f"进程已恢复")
        except Exception as e:
            print(f"无法恢复进程: {e}")


    def kill_process(self,pid:int):
        try:
            Process(pid).terminate()
            print(f"进程已结束")
        except Exception as ex:
            print(f"无法结束进程{ex}")
            
    def get_pid_by_name(self,name:str):
        for process in iter(["pid", "name"]):
            if process.info["name"] == name:
                print(f"进程{name}的pid为: {process.info["pid"]}")
                return process.info["pid"]
        print("没有找到该进程")
        return None

# def pid_init():
#     for key, name in vars(Config.Process.ProcessNames).items():
#         if key.startswith("__"):
#             continue
#         pid = get_id_by_name(name)
#         setattr(Config.Process.ProcessPids, key, pid)



def is_suspended(pid):
    try:
        p = Process(pid)
        status = p.status()
        return status == STATUS_STOPPED or status == 'stopped'
    except Exception as e:
        print("No process found with PID:", e)
        return False

# def kill_process(pid:int):
#     try:
#         for name, pid in vars(Config.Process.ProcessPids).items():
#             if name == "Rockstar_Service" or name.startswith("__"):
#                 continue
#             Process(pid).terminate()
#             print(f"进程已结束")
#     except Exception as ex:
#         print(f"无法结束进程{ex}")