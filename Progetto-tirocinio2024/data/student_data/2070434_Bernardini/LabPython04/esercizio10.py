a = input("Inserire prima stringa: ")
b = input("Inserire seconda stringa: ")
c = input("Inserire terza stringa: ")
while len(a)+len(b)!=len(c):
    a = b
    b = c
    c = input("Inserire una stringa: ")
print(a,b,c)
