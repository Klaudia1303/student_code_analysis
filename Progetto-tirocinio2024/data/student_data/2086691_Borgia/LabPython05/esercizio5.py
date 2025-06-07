s=input("Inserire una stringa di minimo 2 caratteri:")
n=int(input("Inserire un numero intero positivo: "))
run=False
for i in range(len(s)):
    if run==False:
        if s[i]==s[i+n]:
            run=True
print(run)
