idata = input()

row = int(idata[1:2])
col = ord(idata[0:1]) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0

for step in steps:
  nxt_row = row + step[0]
  nxt_col = col + step[1]

  if nxt_row >= 1 and nxt_row <= 8 and nxt_col >= 1 and nxt_col <= 8:
    result = result + 1

print(result)
