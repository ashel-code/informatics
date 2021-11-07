n, m, k = map(int, input().split())

red = m // k
white = k - 1
if (m > k):
    print(n * (white + red))
else:
    print(n * m)

