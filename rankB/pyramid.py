# Approach  : 与えられた外周の長さに対するピラミッドの配列を求め（理想ピラミッド）、理想ピラミッドから標準入力で渡された配列ピラミッドの各要素の差分を足し合わせる

N = int(input())
stones = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 現在位置 (i, j) から外周までの距離の最小値がレベルになる
        level = min(i, j, N-1-i, N-1-j)
        answer[i][j] = level + 1

count = 0
for i in range(N):
    for j in range(N):
        count += stones[i][j] - answer[i][j]

print(count)
