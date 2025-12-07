#!/usr/bin/env python3
import subprocess
import statistics
import json
import csv
import time
import os

N = 10  # 実行回数

# ----- 測定対象プログラム -----
PYTHON_CMDS = [
    ["python3", "is_prime_n.py"],
    ["python3", "is_prime_sqrt.py"],
    ["python3", "is_prime_even.py"]
]

C_CMDS = [
    ["./is_prime"],
    ["./is_prime_org"]
]

# C# DLL を自動探索
def find_csharp_dll():
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(".dll"):
                return os.path.join(root, f)
    return None

CSHARP_DLL = find_csharp_dll()
if not CSHARP_DLL:
    raise RuntimeError("C# DLL が見つかりません。dotnet build -c Release 済みですか？")

CSHARP_CMDS = [
    ["dotnet", CSHARP_DLL]
]

# ----- 計測関数 -----
def measure_commands(commands, lang_prefix):
    result = {}
    for cmd in commands:
        name = lang_prefix + "_" + os.path.basename(cmd[-1]).split(".")[0]
        times = []
        for _ in range(N):
            start = time.perf_counter()
            try:
                subprocess.run(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=3      # ←これ！安全のため追加
                )
            except subprocess.TimeoutExpired:
                print(f"Timeout: {name} took too long!")
                times.append(float('inf'))
                continue
            end = time.perf_counter()
            times.append(end - start)
        result[name] = times
    return result

results = {}
results.update(measure_commands(PYTHON_CMDS, "python"))
results.update(measure_commands(C_CMDS, "c"))
results.update(measure_commands(CSHARP_CMDS, "csharp"))

# ----- 平均 & 標準偏差 -----
summary = {}
for lang, data in results.items():
    # 無限大（timeout）のデータを除外
    filtered = [t for t in data if t != float('inf')]

    if len(filtered) == 0:
        # 全部 timeout → 計測不能として扱う
        summary[lang] = {"avg": float('inf'), "std": float('nan')}
        continue

    if len(filtered) == 1:
        # 標準偏差は計算できないので 0
        summary[lang] = {"avg": filtered[0], "std": 0}
        continue

    avg = statistics.mean(filtered)
    sd  = statistics.stdev(filtered)
    summary[lang] = {"avg": avg, "std": sd}

# ----- CSV 出力 -----
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["program", "run", "time"])
    for program, data in results.items():
        for i, t in enumerate(data):
            writer.writerow([program, i+1, t])

# ----- JSON 出力 -----
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("CSV → results.csv")
print("JSON → summary.json")
print("VSCodeで results.csv を開けば Plot ボタンが出ます！")
