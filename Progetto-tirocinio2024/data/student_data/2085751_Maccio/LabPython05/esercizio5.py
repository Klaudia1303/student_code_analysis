s=input("Inserire una stringa composta da almeno 2 caratteri:  ")
n=int(input("Inserire un numero intero:  "))
i=0
cond=False
while i<(len(s)-n) and cond!=True:
    if s[i]==s[n+i]:
        cond=True
    i=i+1
print(cond)
