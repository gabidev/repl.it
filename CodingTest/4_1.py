size = int(input())
plans = input().split()

x, y = 1, 1

for plan in plans:
  if plan == "U" and x >= 2:
    x = x - 1
  elif plan == "D" and x <= size - 1:
    x = x + 1
  elif plan == "L" and y >= 2:
    y = y - 1
  elif plan == "R" and y <= size - 1:
    y = y + 1

print(x, y)
