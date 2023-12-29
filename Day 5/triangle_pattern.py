def triangle_pattern(num):
    i=1
    while(i<=num):
        j=1
        while(j<=i):
            print("*",end="")
            j=j+1
        print()
        i=i+1
num=int(input())
triangle_pattern(num)
