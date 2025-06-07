s=input("Inserisci stringa: ")
while s.islower()!= True or s.isalpha()!= True:
    print("\n",s[0]+s[-1])
    s=input("Inserisci stringa: ")
print("\n",s[0]+s[-1])

