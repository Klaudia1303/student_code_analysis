s=input('inserisci una stringa di almeno 2 caratteri ')
n=int(input('Inserisci un intero positivo (distanza tra le lettere)' ))
fine=False
for i in range(len(s)):
    while i+n<len(s):
        if s[i]==s[i+n]:
            fine=True
        i=len(s)
print(fine)
