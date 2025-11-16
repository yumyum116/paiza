"""
NOTE:
 This program calculates the number of bingo.
 The length of each row, the number of lottery, pairs of integer in a bingo card, and won numbers are given through a standard input.
"""

size, count = list(map(int, input().split()))
card_numbers = [list(map(int, input().split())) for _ in range(size)]
winning_numbers = list(map(int, input().split()))

for i in range(size):
    for j in range(size):
        if card_numbers[i][j]  in winning_numbers or card_numbers[i][j] == 0:   # Card number 0 is equivalent to 'free' cell in a bingo card
            # Change a won number to '#', not another integer not to confuse whether the number is original or won
            card_numbers[i][j] = '#'

bingo = 0
count = 0
# Count a number of horizontal bingo
for i in range(size):
    bingo += 1 if card_numbers[i].count('#') == size else 0
    count = 0

# Create an array based on index of each row to count vertical bingo
vertical_card = [[0] for _ in range(size)]
for i in range(size):
    for j in range(size):
        vertical_card[j].append(card_numbers[i][j])

# Count a number of vertical bingo
for i in range(size):
    for j in range(1, size + 1):
        if vertical_card[i][j] == '#':
            count += 1
    bingo+= 1 if count == size else 0
    count = 0

# Create an one-axis array to count crossed bingo
pressed_card = []
for i in range(size):
    for j in range(size):
        pressed_card.append(card_numbers[i][j])

# Check a right crossed bingo
for n in range(1, size):
    count += 1 if pressed_card[0] == pressed_card[0 + n * (size + 1)] == '#' else 0
bingo += 1 if count == size - 1 else 0
count = 0

# Check a left crossed bingo
for n in range(1, size):
    count += 1 if pressed_card[size - 1] == pressed_card[(size - 1) + n * (size - 1)] == '#' else 0
bingo += 1 if count == size - 1 else 0

print(bingo)
