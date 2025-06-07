s=input('inserisci una stringa ' )
l=input('inserisci una seconda stringa ')
g=''
f=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j] in l:
            n=j-i
            if n>=f:
                f=n
                g=s[i:j]
            else:
                break
print(g)
        
