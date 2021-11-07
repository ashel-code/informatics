numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]
for i in range(1, 5):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]
print(min)
print(max)