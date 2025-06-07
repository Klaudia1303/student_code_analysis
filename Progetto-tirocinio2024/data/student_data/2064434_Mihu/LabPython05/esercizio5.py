s=input("inserisci stringa con almeno 2 caratteri: ")
n=int(input("inserisci un numero: "))
i=0
corretto=False
while i<len(s)-n and corretto==False:
    if s[i]==s[i+n]:
        corretto=True
    i=i+1
if corretto==True:
    print("True")
else:
    print("False")
