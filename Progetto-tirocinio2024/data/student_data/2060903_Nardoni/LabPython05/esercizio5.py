s=""
while len(s)<2:
    s=input("Inserisci una stringa con almeno 2 caratteri")
n=int(input("Inserisci un numero intero"))
for i in range (len(s)-n):
    if s[i]==s[i+n]:
        cond = True
    else:
        cond = False
print(cond)
