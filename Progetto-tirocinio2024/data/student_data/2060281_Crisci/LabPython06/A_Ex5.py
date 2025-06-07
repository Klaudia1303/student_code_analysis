s=input("Inserire una stringa alfanumerica: ")
carattere=''
ricorrenza=1
Massimo_ricorrenza=0
for i in range(1, len(s)):
    if(s[i]==s[i-1]):
        ricorrenza=ricorrenza+1
        if(ricorrenza>=Massimo_ricorrenza):
            Massimo_ricorrenza=ricorrenza
            carattere=s[i]
    else:
        ricorrenza=1
print(carattere, Massimo_ricorrenza)
