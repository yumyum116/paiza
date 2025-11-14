# B131: 運賃計算
# アプローチ：線形走査

lines, stations = list(map(int, input().split()))
fares = [list(map(int, input().split())) for _ in range(lines)]
condition = int(input())
destinations = [list(map(int, input().split())) for _ in range(condition)]

total_fares = 0
line = 0
station = 0

for destination in destinations:
    current_line = destination[0] - 1
    current_station = destination[1] - 1
    if current_station == station:
        continue
    elif station > current_station:
        total_fares += fares[current_line][station] - fares[current_line][current_station]
    elif current_station > station:
        total_fares += fares[current_line][current_station] - fares[current_line][station]
    line = current_line
    station = current_station
    
print(total_fares)
