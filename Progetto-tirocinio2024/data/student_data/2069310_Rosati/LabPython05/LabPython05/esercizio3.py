s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
lung=0
if len(s1)>=len(s2):
   lung=len(s2)
else:
   lung=len(s1)
finale=""
for i in range(lung):
    if s1[i] not in s2:
       finale+=s1[i] 
print(finale)
