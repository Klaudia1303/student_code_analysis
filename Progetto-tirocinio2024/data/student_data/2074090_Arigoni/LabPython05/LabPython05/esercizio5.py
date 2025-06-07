s=str(input("Inserisci una stringa con almeno due caratteri>> "))
n=int(input("Inserisci un intero positivo>> "))
d=False
for i in range(len(s)//2):
    if s[i]==s[i+n]:
        d=True
if d:
    print("True")
else:
    print("False")
        
