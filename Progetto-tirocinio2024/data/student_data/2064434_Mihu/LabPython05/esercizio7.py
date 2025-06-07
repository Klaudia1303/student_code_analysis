s=input("inserisci una stringa: ")
i=0
controllo=False
while i<len(s) and controllo==False:
    x=s.rfind(s[i])
    if x>-1 and x!=i:
        controllo=True
    else:
        i=i+1
if controllo==True:
    print("True")
else:
    print("False")
