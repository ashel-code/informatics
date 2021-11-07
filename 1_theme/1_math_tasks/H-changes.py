x, x2, y, y2 = map(int, input().split())

if x > x2:
    max1 = x 
    min1 = x2
else:
    max1 = x2 
    min1 = x

if y > y2:
    max2 = y
    min2 = y2
else:
    max2 = y2 
    min2 = y

c = 0
for i in range(101):
    if i >= min1 and i <= max1:
        if i >= min2 and i <= max2:
            c += 1

print(c)