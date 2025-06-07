s=input('inserisci una stringa ')
i=0
n=0
while i<len(s):
    c=s.count(s[i])
    if c>=n:
        n=c
        l=s[i]
    i+=1
print(l)
