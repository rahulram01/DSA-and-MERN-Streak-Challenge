def replaceX(strings,"x",""):
    l=len(strings)
    if l==0:
        return strings
    replace_ele= replaceX(strings[1:],a,b)
    if strings[0]==a:
        return b+ replace_ele
    else:
        return strings[0]+replace_ele
strings=input()
a=input()
b=input()
print(replaceX(strings,a,b))
