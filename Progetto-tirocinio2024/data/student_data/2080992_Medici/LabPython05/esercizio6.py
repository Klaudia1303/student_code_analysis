s=str(input('inserire una stringa: '))
massimo=0
carattere=''
for i in range(len(s)):
    conto=s.count(s[i])
    if conto>=massimo:
        massimo=conto
        carattere=s[i]
i1=s.find(carattere)
i2=s.rfind(carattere)
print(i2-i1)
      
