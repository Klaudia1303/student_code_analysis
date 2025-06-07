s=''
while not s.islower() or s.isalpha()==False:
      s=input("Inserisci stringa(stringa tutta minuscola per terminare: ")
      if s!='':
          print(s[0],s[len(s)-1])
       

