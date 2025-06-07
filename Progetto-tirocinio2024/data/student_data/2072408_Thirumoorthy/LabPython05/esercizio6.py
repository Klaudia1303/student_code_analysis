s=input('inserire una stringa: ')
c=0
massimadistanza=0
for c in s:
    if s.rfind(c)-s.find(c)>massimadistanza:
        massimadistanza=s.rfind(c)-s.find(c)
print(massimadistanza)
  

