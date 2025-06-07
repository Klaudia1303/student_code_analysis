s=input("Inserisci una stringa: ")
s1=''
while s!='':
      s1=input("Inserisci una stringa : ")
      while s[len(s)-1]!=s1[0]:
            s=s1
            s1=input("Inserisci una stringa : ")
      break
print(s,s1)
