import os
import subprocess
import time
from datetime import datetime
import keyboard

def terminate_display_processes():
    # 获取当前影响显示的进程列表
    result = subprocess.run(['powercfg', '-requests'], capture_output=True, text=True)
    output = result.stdout

    # 查找DISPLAY相关的进程
    for line in output.splitlines():
        if 'DISPLAY:' in line:
            continue
        if '[PROCESS]' in line:
            # 提取进程路径
            process_path = line.split('] ')[1]
            # 强制终止进程
            try:
                os.system(f'taskkill /F /IM {os.path.basename(process_path)}')
                print(f"已终止进程: {process_path}")
            except Exception as e:
                print(f"无法终止进程: {process_path}, 错误: {e}")

def lock_computer():
    # 锁定计算机
    os.system('rundll32.exe user32.dll, LockWorkStation')
    print("计算机已锁定")

def pause_all_streaming():
    # 使用Windows媒体键暂停播放
    keyboard.send('play/pause media')
    print("已发送媒体暂停命令")

# 执行终止、锁定和暂停操作
terminate_display_processes()
pause_all_streaming()  # 先暂停媒体，再锁定电脑
lock_computer()