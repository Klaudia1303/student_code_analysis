s=""
c=0
while len(s)<2:
      s=input("Inserisci una stringa di almeno 2 caratteri: ")
n=int(input("Inserisci un intero positivo: "))
for i in range(len(s)-n):
    if s[i]==s[i+n]:
       c+=1
if c>=1:
   print("True")
else:
   print("False")
