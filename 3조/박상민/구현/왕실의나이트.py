combination = input()
row = int(combination[1])
col = int(ord(combination[0])) - int(ord('a')) + 1

ways = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
count = 0
for block in ways:
    next_row = row + block[1]
    next_col = col + block[0]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)
