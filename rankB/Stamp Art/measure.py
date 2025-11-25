#!/usr/bin/env python3
import psutil
import subprocess
import time
import resource

def run_and_measure(script, input_file):
    start_real = time.time()
    # 実行前にリソース使用量をリセット
    start_usage = resource.getrusage(resource.RUSAGE_CHILDREN)

    proc = subprocess.Popen(
        ["python3", script],
        stdin=open(input_file),
        stdout=subprocess.DEVNULL
    )
    p = psutil.Process(proc.pid)
    max_rss = 0  # 最大メモリ（bytes）
    
    while True:
        try:
            mem = p.memory_info().rss
            max_rss = max(max_rss, mem)
        except psutil.NoSuchProcess:
            break
        
        if proc.poll() is not None:
            break
        time.sleep(0.01)
    
    # 最終確認
    try:
        mem = p.memory_info().rss
        max_rss = max(max_rss, mem)
    except psutil.NoSuchProcess:
        pass
    
    end_real = time.time()
    end_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    
    real = end_real - start_real
    user = end_usage.ru_utime - start_usage.ru_utime
    sys_time = end_usage.ru_stime - start_usage.ru_stime
    
    print(f"{script}: real = {real:.3f}s, user = {user:.3f}s, sys = {sys_time:.3f}s, max memory = {max_rss / 1024:.0f} KB")

if __name__ == "__main__":
    input_file = "input_large.txt"
    scripts = ["submit.py", "fast_approach.py", "cache.py"]
    
    for script in scripts:
        run_and_measure(script, input_file)
