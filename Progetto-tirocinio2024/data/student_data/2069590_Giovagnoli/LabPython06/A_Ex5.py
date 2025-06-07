s=input("Inserire una stringa alfanumerica: ")
carattere=""
contatore=0
massimo=0
carattere_max=""
if s.isalnum() and s!="":
    for pos in range(len(s)):
        carattere=s[pos]
        i=pos
        while i<len(s) and carattere==s[i]:
            contatore+=1
            i+=1
        if contatore>=massimo:
            massimo=contatore
            contatore=0
            carattere_max=carattere
        else:
            contatore=0
        #carattere=s[pos]
    print(carattere_max,"",massimo)
else:
    print("Inserisci un input valido!")    