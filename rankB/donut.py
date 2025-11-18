row, column = map(int, input().split())
symbol_art = [input() for _ in range(row)]
donut = ['###', '#.#', '###']

result = 0
for i in range(row - 2):  
    for j in range(column - 2):
        match = True
        for k in range(3):
            for l in range(3):
                if symbol_art[i + k][j + l] != donut[k][l]:
                    match = False
                    break
            if not match:
                break
        if match:
            result += 1

print(result)
