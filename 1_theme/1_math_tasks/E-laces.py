a, b, i, n = map(int, input().split())

res = a * (n * 2 - 1) + b * (2 * (n - 1)) + i * 2
print(res)