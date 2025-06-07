s=input('inserire stringa: ')
t=input('inserire stringa: ')
for a in range(len(s)):
    if s[a] not in t:
        print(s[a],end='')
