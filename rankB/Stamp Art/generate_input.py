import random

rows = 2
columns = 3
number = 5      # patterns of stamp
res_row = 10000 # number of rows to be printed
res_col = 10    # number of columns to be printed

# make stamp strings randomly
stamp_list = []
for i in range(number):
    stamp = []
    for r in range(rows):
        s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=columns))
        stamp.append(s)
    stamp_list.append(stamp)

# print results on standard output
print(rows, columns, number)
for stamp in stamp_list:
    for line in stamp:
        print(line)

# print layout
print(res_row, res_col)
for _ in range(res_row):
    print(' '.join(str(random.randint(1, number)) for _ in range(res_col)))
