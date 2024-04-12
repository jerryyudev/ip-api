import subprocess
import tkinter as tk
from tkinter import scrolledtext

def scan_wifi():
    # 清空文本框
    text_area.delete(1.0, tk.END)
    
    # 执行系统命令来扫描Wi-Fi网络
    result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=bssid'], capture_output=True, text=True)
    
    # 将扫描结果显示在文本框中
    text_area.insert(tk.END, result.stdout)

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
