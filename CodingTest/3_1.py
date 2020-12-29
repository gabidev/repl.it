money = [500, 100, 50, 10]
N = 1260

for m in money:
  print(m, N // m)
  N = N % m
