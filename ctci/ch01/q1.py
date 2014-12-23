def hasUniqueChar1(str):
    if len(str) > 128:
        return False
    lst = list(sorted(str))
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True 

def hasUniqueChar2(str):
    if len(str) > 128:
        return False
    lst = [False for i in range(128)]
    for c in str:
        if lst[ord(c)]:
            return False
        else:
            lst[ord(c)] = True
    return True

def main():
    str1 = 'This is a test!'
    str2 = ''
    str3 = 'No!'
    print hasUniqueChar1(str1)
    print hasUniqueChar2(str1)
    print hasUniqueChar1(str2)
    print hasUniqueChar2(str2)
    print hasUniqueChar1(str3)
    print hasUniqueChar2(str3)

main()
