from pythonping import ping

def ping_port(ip, port):
    try:
        result = ping(ip, count=1, timeout=1, verbose=False)
        if result.success():
            print(f"Port {port} is reachable")
        else:
            print(f"Port {port} is unreachable")
    except Exception as e:
        print(f"Error pinging port {port}: {e}")

def ping_ports(ip):
    for port in range(1, 65536):  # 扫描所有端口
        ping_port(ip, port)

def main():
    ip = input("Enter the IP address to ping: ")
    print(f"Pinging all ports on {ip}...")
    ping_ports(ip)

if __name__ == "__main__":
    main()
