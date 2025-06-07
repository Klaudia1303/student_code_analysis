s=input('Inserire una stringa: ')
d=1
while s.find('a')==-1 or s.find('c')==-1:
    s=input('Inserire una stringa: ')
    d+=1
print(d)