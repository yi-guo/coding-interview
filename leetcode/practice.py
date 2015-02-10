def isMatch(s, p, i=0, j=0):
    while i < len(s) and j < len(p):
        if j == len(p) - 1 or p[j + 1] != '*':
            if s[i] != p[j] and p[j] != '.':
                return False
        else:
            if isMatch(s, p, i, j + 2):
                return True
            while i < len(s) and (s[i] == p[j] or p[j] == '.'):
                if isMatch(s, p, i + 1, j + 2):
                    return True
                i = i + 1
            return False
        i = i + 1
        j = j + 1
    return True if i == len(s) and j == len(p) else False

def main():
    print isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")

main()
