x, y = map(int, input().split())
c = 0
for i in range(1605, 2001, 10):
    if i > x and i <= y:
        c+=1

print(c)