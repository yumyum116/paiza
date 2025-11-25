rows, columns, number = map(int, input().split())
stamp = []
for _ in range(number):
    stamp.append([input() for _ in range(rows)])

res_row, res_col = map(int, input().split())
result = [list(map(int, input().split())) for _ in range(res_row)]

cache = [[stamp[i][k] for i in range(number)] for k in range(rows)]

for l in range(res_row):
    for k in range(rows):
        print("".join(cache[k][result[l][n] - 1] for n in range(res_col)))
