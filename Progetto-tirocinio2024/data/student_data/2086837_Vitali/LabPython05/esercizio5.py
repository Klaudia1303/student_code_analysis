s=input("Inserisci una stringa di almeno 2 caratteri :")
n=int(input("Inserisci un intero positivo n :"))
while len(s)<2 or n<0:
    print("Dati non validi")
    s=input("Inserisci una stringa di almeno 2 caratteri :")
    n=int(input("Inserisci un intero positivo n :"))
ver=False
for i in range(len(s)):
    if i+n<len(s):
        if s[i]==s[i+n]:
            print("True")
            ver=True
            break
if ver==False:
    print("False")
