import socket
import threading

# 创建一个锁对象
print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        # 创建TCP套接字对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置连接超时时间为1秒
        s.settimeout(1)
        # 尝试连接到目标IP的端口
        result = s.connect_ex((ip, port))
        # 如果连接成功，则端口是开放的
        if result == 0:
            # 使用锁来确保输出的顺序性
            with print_lock:
                print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(ip):
    threads = []
    for port in range(1, 65536):  # 扫描所有端口
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print("Scan completed.")

def main():
    ip = input("Enter the IP address to scan: ")
    print(f"Scanning all ports on {ip}...")
    scan_ports(ip)
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
