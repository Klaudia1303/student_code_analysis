s = (input("Inserisci la prima stringa: "))
n=int(input("Inserisci un numero: "))
lun=len(s)
for i in range (lun):
    if s[0]==s[n]:
        print("True")
        break
    else:
        print("False")
        break