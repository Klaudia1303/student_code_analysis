s = str(input('Insert string: '))
n = int(input('Insert number: '))
if len(s)>=2:
    for i in range(len(s)-n):
        x = i+n
        y = i-n
    if s[i]==s[x] or s[i]==s[y]:
        print('True')
    else:
        print('False')
else:
    print('String too short, restart')
