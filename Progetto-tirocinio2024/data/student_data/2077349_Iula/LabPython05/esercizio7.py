s=input("Inserisci una stringa: ")
temp=0
for i in range(len(s)):
    if s.count(s[i])>1:
        print("True")
        break
    else:
        temp+=1
if temp==len(s):
    print("False")

