s=input("Inserire una stringa: ")
c=1
while s.find('a')==-1 or s.find('c')==-1:
    c+=1
    s=input("Inserire una stringa: ")
print(c)
