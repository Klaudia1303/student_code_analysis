s=str(input("Inserisci una stringa>> "))
finito=False
for i in range(len(s)):
    if s.find(s[i])!=s.rfind(s[i]):
        finito=True
if finito:
    print("True")
      
if s.find(s[i])==s.rfind(s[i]):
          print("False")
