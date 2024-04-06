import requests

def get_ip_info():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    ip_info = get_ip_info()
    print("IP 地址信息:")
    print("--------------")
    print(f"IP 地址: {ip_info['query']}")
    print(f"国家: {ip_info['country']}")
    print(f"国家代码: {ip_info['countryCode']}")
    print(f"州/省: {ip_info['regionName']}")
    print(f"城市: {ip_info['city']}")
    print(f"邮政编码: {ip_info['zip']}")
    print(f"经度: {ip_info['lon']}")
    print(f"纬度: {ip_info['lat']}")
    print(f"时区: {ip_info['timezone']}")
    print(f"ISP: {ip_info['isp']}")
    print(f"组织: {ip_info['org']}")
    print(f"自动系统编号 (AS): {ip_info['as']}")
    input("按 Enter 键退出...")
