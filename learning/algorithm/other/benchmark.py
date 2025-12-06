#!/usr/bin/env python3
import subprocess
import time
import psutil
import resource
import os

# -----------------------------
# 実行 & 計測関数
# -----------------------------
def run_and_measure(script):
    """script を実行し、real/user/sys/max_rss を返す"""

    start_real = time.time()
    start_usage = resource.getrusage(resource.RUSAGE_CHILDREN)

    proc = subprocess.Popen(
        ["python3", script],
        stdout=subprocess.DEVNULL,
    )

    p = psutil.Process(proc.pid)
    max_rss = 0

    # 子プロセスが終了するまで、メモリを監視
    while True:
        if proc.poll() is not None:
            break
        try:
            mem = p.memory_info().rss
            max_rss = max(max_rss, mem)
        except psutil.NoSuchProcess:
            break
        time.sleep(0.01)

    end_real = time.time()
    end_usage = resource.getrusage(resource.RUSAGE_CHILDREN)

    real = end_real - start_real
    user = end_usage.ru_utime - start_usage.ru_utime
    sys = end_usage.ru_stime - start_usage.ru_stime

    return real, user, sys, max_rss


# -----------------------------
# メイン処理
# -----------------------------
def main():
    # 比較したいスクリプト名を並べる
    programs = [
        "is_prime_n.py",
        "is_prime_sqrt.py",
        "is_prime_even.py"
    ]

    print(f"{'Program':30} | {'real(s)':>8} | {'user(s)':>8} | {'sys(s)':>8} | {'max_rss(KB)':>12}")
    print("-" * 80)

    for prog in programs:
        if not os.path.exists(prog):
            print(f"{prog:30} | NOT FOUND")
            continue

        real, user, sys, max_rss = run_and_measure(prog)
        print(
            f"{prog:30} | {real:8.3f} | {user:8.3f} | {sys:8.3f} | {max_rss // 1024:12d}"
        )


if __name__ == "__main__":
    main()
