from psutil import process_iter, Process
import Config

def suspend_process():
    try:
        Process(Config.Process.ProcessPids.Process_GTA).suspend()
    except Exception as e:
        print(f"Error suspending process: {e}")


def resume_process():
    try:
        Process(Config.Process.ProcessPids.Process_GTA).resume()
    except Exception as e:
        print(f"Error resumeing process: {e}")


def kill_process():
    try:
        for name, pid in vars(Config.Process.ProcessPids).items():
            if name == "Process_Rockstar_Service" or name.startswith("__"):
                continue
            Process(pid).terminate()
            print(f"进程已结束")
    except Exception as ex:
        print(f"无法结束进程{ex}")
        
def get_process_id_by_name(process_name):
    for process in process_iter(["pid", "name"]):
        if process.info["name"] == process_name:
            return process.info["pid"]
    return None

def pid_init():
    for key, name in vars(Config.Process.ProcessNames).items():
        if key.startswith("__"):
            continue
        pid = get_process_id_by_name(name)
        setattr(Config.Process.ProcessPids, key, pid)