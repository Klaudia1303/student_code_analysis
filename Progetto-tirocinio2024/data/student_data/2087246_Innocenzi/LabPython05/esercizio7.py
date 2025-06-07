s=input("Inserisci una stringa: ")
for i in range(0, len(s)):
    conta=s.count(s[i])
    
if(conta>=2):
    print("True")
else:
    print("False")