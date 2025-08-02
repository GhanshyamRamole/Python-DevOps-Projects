import psutil
import socket

def get_system_health():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    print(get_system_health())

