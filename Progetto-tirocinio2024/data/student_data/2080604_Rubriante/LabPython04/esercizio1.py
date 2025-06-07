s=input("Inserisci una stringa: ")
count=1
while s.find("a")==-1 or s.find("c")==-1:
    count+=1
    s=input("Inserisci una stringa: ")
print(count)
