import subprocess
import tkinter as tk
from tkinter import scrolledtext
import locale

def scan_wifi():
    # 清空文本框
    text_area.delete(1.0, tk.END)
    
    try:
        # 执行系统命令来扫描Wi-Fi网络
        result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=bssid'], capture_output=True)
        
        # 获取默认的系统编码
        system_encoding = locale.getpreferredencoding()
        
        # 将扫描结果显示在文本框中
        text_area.insert(tk.END, result.stdout.decode(system_encoding, errors='ignore'))
    except Exception as e:
        # 如果出现错误，打印错误信息并在文本框中显示错误信息
        print("Error:", e)
        text_area.insert(tk.END, "Error: Unable to scan Wi-Fi networks.")

# 创建主窗口
root = tk.Tk()
root.title("Wi-Fi Scanner")

# 创建扫描按钮
scan_button = tk.Button(root, text="Scan Wi-Fi", command=scan_wifi)
scan_button.pack()

# 创建文本框用于显示扫描结果
text_area = scrolledtext.ScrolledText(root, width=80, height=20)
text_area.pack()

# 运行主循环
root.mainloop()
