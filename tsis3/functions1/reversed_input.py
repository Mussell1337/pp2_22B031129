def reversed(s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

def reverseString(str):
    str = list(str + " ")
    n = len(str)
    j = 0
    for i in range(n):
        if str[i] == " ":
            reversed(str, j, i - 1)
            j = i + 1
    str.pop()
    reversed(str, 0, len(str) - 1)
    return "".join(str)

str = input("type words: ")
rev = reverseString(str)
print(rev)