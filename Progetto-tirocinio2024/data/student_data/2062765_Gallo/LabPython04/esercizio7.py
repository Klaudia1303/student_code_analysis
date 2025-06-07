s=input("Inserisci stringa")
i=0
massimo=0
lettera='0'
if s=='':
    print("Non hai inserito nessuna stringa")
else:
    while i<len(s):
        if s.count(s[i])>=massimo:
            massimo=s.count(s[i])
            lettera=i    
        i+=1
    print(s[lettera])
        
