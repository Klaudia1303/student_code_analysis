s=input('inserisci una stringa: ')
Max=0
for i in range(len(s)): 
    b=s[i]
    c=s.rfind(b)
    e=s.find(b)
    k=abs(c-e)
    if k>Max:
        Max=k
print(Max)
