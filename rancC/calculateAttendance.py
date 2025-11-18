import datetime

day = int(input())
records = [list(input().split()) for _ in range(day)]
working_hours = []
time_format = '%H:%M'
for i in range(day):
    start_time = datetime.datetime.strptime(records[i][0], time_format)
    end_time = datetime.datetime.strptime(records[i][1], time_format)
    working_hours.append(end_time - start_time)

total = 0
for i in range(day):
    total += working_hours[i].seconds

hour = int(total / (60 * 60))
mins = int((total - 60 * 60 * hour) / 60)
print(hour, mins)
