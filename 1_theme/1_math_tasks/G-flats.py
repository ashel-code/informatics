x, y = map(int, input().split())

dif = y - x + 1

if (x - 1) % dif == 0:
    print("YES")
else:
    print("NO")