s=input('inserire stringa (almeno 2 caratteri): ')
n=int(input('inserire numero >0: '))
a=False
for b in range(len(s)):
    for c in range(1,len(s)):
        if s[b]==s[c] and c-b==n:
            a=True
print(a)
