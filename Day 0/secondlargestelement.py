def secondlargest(li):

    if all(x == li[0] for x in li):
        return -1

    li = list(set(li))  
    li.sort()

    if len(li) < 2:
        return -1

    return li[-2]

def takeInput():
    n = int(input())
    li = [int(x) for x in input().split()]
    return li, n

t = int(input())
while t:
    li, n = takeInput()
    print(secondlargest(li))
    t = t - 1
