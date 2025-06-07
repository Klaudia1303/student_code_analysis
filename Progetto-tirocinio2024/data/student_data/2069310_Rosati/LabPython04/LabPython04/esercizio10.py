s=input("Inserisci una stringa: ")
s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")     
while len(s)+len(s1)!=len(s2):
      s=s1
      s1=s2
      s2=input("Inserisci una stringa: ")
print(s,s1,s2)
