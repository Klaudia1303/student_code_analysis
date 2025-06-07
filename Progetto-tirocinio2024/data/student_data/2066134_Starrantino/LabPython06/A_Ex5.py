s: str = input('> ')
countOut: int = 0
char: str = ''
for i in range(len(s)):
    index: int = i
    count: int = 0
    while index < len(s) and s[i] == s[index]:
        count += 1        
        index += 1
    if count >= countOut:
        char = s[i]
        countOut = count  
print(char, countOut)
