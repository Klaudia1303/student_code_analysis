s=str(input('Inserisci carattere '))
a=1
b=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        a+=1
        if a>=b:
            b=a
            c=s[i]
    else:
        a=1
print(c,b)
