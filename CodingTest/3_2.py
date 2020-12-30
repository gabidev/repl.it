# n:두번째 줄 입력 개수, m:더할 수 있는 수, k:반복 가능 수
print("n m k 순으로 입력 하세요")
n, m, k = map(int, input().split())
print("위에 입력한 n에 해당하는 갯수 만큼 입력 하세요")
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

print(m // (k + 1) * (first * k + second) + first * (m % (k + 1)))
