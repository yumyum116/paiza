rows, columns, number = map(int, input().split())
stamp = []
for _ in range(number):
    stamp.append([input() for _ in range(rows)])

res_row, res_col = map(int, input().split())
result = [list(map(int, input().split())) for _ in range(res_row)]

for l in range(res_row):
    for k in range(rows):
        print("".join(stamp[result[l][n] - 1][k] for n in range(res_col)))
