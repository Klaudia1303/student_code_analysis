s=str(input("Inserire una stringa alfanumerica non vuota:"))
inizio=0
conteggioTot=0
for i in range(0,len(s)):
    index=s[i]
    if s.count(s[i])>=inizio:
        j=1
        z=1
        conteggio1=1
        conteggio2=0
        while i+j<=len(s)-1:
            indexSucc=s[i+j]
            if indexSucc!=index:
                break
            else:
                conteggio1=conteggio1+1
                j=j+1
        while i>0:
            indexPrec=s[i-z]
            if indexPrec!=index:
                break
            else:
                conteggio2=conteggio2+1
                z=z+1
        if conteggio1+conteggio2>=conteggioTot:
            lettera=s[i]
            conteggioTot=conteggio1+conteggio2
            inizio=s.count(s[i])
print(lettera,s.count(lettera))
        

    
        

    
        
        
        

    


