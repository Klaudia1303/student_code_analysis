s=input("Inserisci una stringa: ")
cont=0
for i in range(len(s)):
    if s.rfind(s[i])!= i:
       cont=1
if cont==0:
   print("False")
else:
   print("True")
