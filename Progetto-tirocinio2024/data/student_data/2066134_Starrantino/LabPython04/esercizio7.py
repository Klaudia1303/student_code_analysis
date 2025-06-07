s: str = input('> ')
char: str = ''
count: int = 0
index: int = 0
while index < len(s):
    c: str = s[index]
    num: int = s.count(c)

    if (num == count) and (s.rfind(c) > s.rfind(char)):
        count = num
        char = c

    elif num > count:
        count = num
        char = c

    index += 1

print(char)
