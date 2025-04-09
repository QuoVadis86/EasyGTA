import logging
from psutil import process_iter, Process, STATUS_STOPPED

def suspend_process(pid: int):
    try:
        Process(pid).suspend()
        logging.info(f"进程{pid}已挂起")
    except Exception as e:
        logging.error(f"无法挂起进程: {e}")

def is_suspended(pid: int)->bool:
    try:
        status = Process(pid).status()
        return status == STATUS_STOPPED
    except Exception as e:
        logging.error(f"No process found with PID: {e}")
        return False

def resume_process(pid: int):
    try:
        Process(pid).resume()
        logging.info(f"进程{pid}已恢复")
    except Exception as e:
        logging.error(f"无法恢复进程: {e}")

def kill_process(pid: int):
    try:
        Process(pid).terminate()
        logging.info(f"进程{pid}已结束")
    except Exception as ex:
        logging.error(f"无法结束进程: {ex}")

def get_pid_by_name(name: str):
    for process in process_iter(["pid", "name"]):
        if process.info["name"] == name:
            logging.info(f"进程{name}的pid为: {process.info['pid']}")
            return process.info["pid"]
    logging.warning("没有找到该进程")