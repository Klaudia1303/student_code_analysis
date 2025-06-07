s=input('inserisci stringa s:')
i=0
numero=0
while i<len(s):
    conta=s.count(s[i])
    if conta>=numero:
        numero=conta
        lettera=s[i]
    i+=1
print(lettera)
    
    
