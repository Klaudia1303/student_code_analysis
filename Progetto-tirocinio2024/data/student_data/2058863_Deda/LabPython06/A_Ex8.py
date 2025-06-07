s1=str(input('Inserisci stringa 1 '))
s2=str(input('Inserisci stringa 2 '))
n=int(input('Inserisci intero '))
w=''
precedente=''
for i in range(len(s1)-n+1):
    a=s2.count(s1[i])
    c=len(s1[:i+1])
    for j in range(n):
        d=len(s1[:i+j])
        b=s2.count(s1[i:i+1+j])
        if a>=1 and b>=1 and d-c<=n:
            w=precedente+s1[i]
            precedente=w
print(w)
