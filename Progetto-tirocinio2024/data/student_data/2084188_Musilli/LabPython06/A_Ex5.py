b=True
while b:
    s=input("Inserire una stringa: ")
    if s!="": b=False
    else: print("\nValore iserito non valido. Inserire una stringa non vuota\n")
conta=c=1; carattere=a=s[0]
for i in range(len(s)):
    if b:  a=s[i]; c=1; 
    if (i+1)<len(s) and s[i]==s[i+1]:    c+=1; b=False
    elif (i-1)>0 and s[i]==s[i-1]: conta=c; carattere=a; b=True
if conta==1: carattere=s[len(s)-1]
print("Carattere con più occorrenze consecutive:",carattere,\
      "\nNumero occorrenze:",conta)
