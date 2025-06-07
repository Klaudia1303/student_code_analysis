s=input('inserire una stringa: ')
x=0
for i in range(0,len(s)):
    if s[i]==s[-(i+1)]:
        x+=1
    else:
        break
print('palindorma di livello:',x)
