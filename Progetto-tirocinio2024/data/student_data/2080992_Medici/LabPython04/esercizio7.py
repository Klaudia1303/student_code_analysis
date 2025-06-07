s=str(input('inserire una stringa: '))
i=0
conto=0
massimo=0
carattere=''
while i<len(s):
    conto=s.count(s[i])
    if conto>=massimo:
        massimo=conto
        carattere=s[i]
    i+=1
print(carattere)
        
