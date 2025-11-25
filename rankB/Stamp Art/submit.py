# 提出したコード
rows, columns, number = map(int, input().split())
stamp = []
for _ in range(number):
    stamp.append([input() for _ in range(rows)])

res_row, res_col = map(int, input().split())
result = [list(map(int, input().split())) for _ in range(res_row)]

art = [["" for _ in range(res_col)] for _ in range(res_row * rows)]

for l in range(res_row):
    for k in range(rows):
        m = l * rows + k
        for n in range(res_col):
            stamp_index = result[l][n] - 1
            art[m][n] = stamp[stamp_index][k]

for row in art:
    print("".join(row))
