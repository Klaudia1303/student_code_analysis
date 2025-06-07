s=input('inserisci una stringa:')
i=0
n=0
while i<len(s):
    x=s.count(s[i])
    if x>=n:
        n=x
        lettera=s[i]
    i+=1
print(lettera)
