s=input('inserire una stringa: ')
contatore=1
while s.count('c')==0 or s.count('a')==0:
      contatore+=1
      s=input('inserire una stringa: ')

print(contatore)

