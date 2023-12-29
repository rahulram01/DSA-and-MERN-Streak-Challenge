def print_num(chars):
    
    if (chars==chars.upper()):
        return 1
    elif (chars==chars.lower()):
        return 0
    elif(chars==chars.int()):
        return -1
chars=input()
print(print_num(chars))