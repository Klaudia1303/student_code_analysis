s = input('stringa alfanumerica: ')
same_char = 1
char = ''
max_char = 1

for i in range(len(s)-1):
    if s.find(s[i]) != s.find(s[i+1]):
        same_char = 1
    else:   
        same_char += 1
        char = s[i]
        if same_char >= max_char:
            max_char = same_char
print(char, max_char)
