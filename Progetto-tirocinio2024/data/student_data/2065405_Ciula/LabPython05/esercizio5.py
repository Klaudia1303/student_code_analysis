s=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero: "))
b=False
for i in range(len(s)-n):
    if(s[i]==s[i+n]):
        b=True
print(b)
