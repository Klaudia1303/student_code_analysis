s=input('inserire una stringa: ')
y=-1
livello=0
for i in s:
    if i==s[y]:
        livello+=1
        y-=1
    else:
        break
print(livello)
