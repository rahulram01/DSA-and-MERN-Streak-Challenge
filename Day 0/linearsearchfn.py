def linear_search(li,ele):
    for i in range(n):
        if li[i]==ele:
            return i
    else:
        return -1
n=int(input())   
li=[int(x) for x in input().split()]
ele=int(input())
index=linear_search(li,ele)
print(index)
