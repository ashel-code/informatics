n, k = map(int, input().split())

squares = 1 
fact = 1

for i in range(0, k):
    squares *= (n - i) ** 2 # сколько вариантов в оставшемся "квадрате"
    fact *= i + 1           # контроль кол-ва вариантов, убирает повторы

print(squares // fact)
