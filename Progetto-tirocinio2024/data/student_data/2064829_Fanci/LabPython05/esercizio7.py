s = input("inserisci stringa: ")
sen=False
for i in s:
    if s.count(i)>1:
        sen=True
if sen==True:
    print("True")
else: print("False")
