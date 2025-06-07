s=input("Inserisci una stringa: ")
cont=0
for i in range(int(len(s)/2)):
    if s[i]==s[(len(s)-1)-i]:
       cont+=1
    else:
       break
if cont == int(len(s)/2):
   print("Livello della palindromia: ",len(s))
else:
    print("Livello della palindromia: ",cont)
