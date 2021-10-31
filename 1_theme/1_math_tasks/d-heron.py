x, y = map(int, input().split())
max = 0
min = 0
if x > y:
    max = x
    min = y
else:
    min = x
    max = y

minH = 0
maxH = 0

if(max % 2 == 0):
    minH = max // 2
else: 
    minH = max // 2 + 1

maxH = min

print(minH, maxH, end=' ')