c=input("Inserire un carattere: ")
s=input("Inserire una stringa: ")
while s.count(c)<=2:
    s=input("Inserire una stringa: ")
print(s.count(c))
