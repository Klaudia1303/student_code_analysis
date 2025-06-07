s = input("inserisci stringa: ")
n = int(input("inserisci intero: "))
sen=False
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        sen=True
if sen==True:
    print("True")
else:
    print("False")
        
