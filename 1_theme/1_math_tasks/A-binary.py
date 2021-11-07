n = int(input())

maxNum = 2 ** n 

result = ""
for i in range(maxNum):
    tmp = i
    result = ""
    for j in range(n):
        if tmp >= 2 ** (n - j - 1):
            tmp -= 2 ** (n - j - 1)
            result += "1"
        else:
            result += "0"
    print(result)