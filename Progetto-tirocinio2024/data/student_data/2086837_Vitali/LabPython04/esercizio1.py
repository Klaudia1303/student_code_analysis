s=input("Inserisci stringa: ")
count=1
while s.find('a')==-1 or s.find('c')==-1:
    s=input("Inserisci stringa: ")
    count +=1
print(count)
