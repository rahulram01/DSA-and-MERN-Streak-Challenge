def rotatearray(li, k):
    n = len(li)
    k = k % n  # Ensure k is within the range of the array length

    for i in range(k):
        temp = li[0]
        for j in range(n - 1):
            li[j] = li[j + 1]
        li[n - 1] = temp

    return li

n = int(input())
li = [int(x) for x in input().split()]
k = int(input())

result = rotatearray(li, k)
print(result)
