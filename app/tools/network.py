import subprocess
import json

def get_network_connections(pid):
    """根据PID获取进程的TCP和UDP网络连接"""
    def run_ps_command(command):
        """执行PowerShell命令并返回解析后的JSON数据"""
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        if result.returncode != 0:
            print("执行命令时出错:", result.stderr.strip())
            return []
        output = result.stdout.strip()
        if not output:
            return []
        try:
            data = json.loads(output)
            return data if isinstance(data, list) else [data]
        except json.JSONDecodeError:
            print("解析JSON输出失败")
            return []

    # 获取TCP连接
    tcp_cmd = f"Get-NetTCPConnection | Where OwningProcess -eq {pid} | Select Protocol, LocalAddress, LocalPort, RemoteAddress, RemotePort, State | ConvertTo-Json"
    tcp_conns = run_ps_command(tcp_cmd)
    
    # 获取UDP连接
    udp_cmd = f"Get-NetUDPConnection | Where OwningProcess -eq {pid} | Select Protocol, LocalAddress, LocalPort, RemoteAddress, RemotePort | ConvertTo-Json"
    udp_conns = run_ps_command(udp_cmd)
    
    return tcp_conns + udp_conns

def main():
    pid = int(input("请输入要查询的进程PID: "))
    connections = get_network_connections(pid)
    
    if not connections:
        print(f"进程 {pid} 没有网络连接或PID不存在。")
        return
    
    print(f"\n进程 {pid} 的网络连接信息：")
    print("-" * 60)
    for conn in connections:
        print(f"协议: {conn.get('Protocol', 'N/A')}")
        print(f"本地地址: {conn.get('LocalAddress', 'N/A')}:{conn.get('LocalPort', 'N/A')}")
        print(f"远程地址: {conn.get('RemoteAddress', 'N/A')}:{conn.get('RemotePort', 'N/A')}")
        if conn.get('Protocol') == 'TCP':
            print(f"状态: {conn.get('State', 'N/A')}")
        print("-" * 60)

if __name__ == "__main__":
    main()