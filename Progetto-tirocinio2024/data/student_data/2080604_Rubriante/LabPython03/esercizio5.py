x=input("Inserire una stringa: ")
while not x.isalpha() or not x.islower():
    print(x[0],x[len(x)-1])
    x=input("Inserire una stringa: ")
print(x[0],x[len(x)-1])
