c=input("Inserire un carattere: ")
b=True
while b:
    s=input("Inserire una stringa: ")
    if s.count(c)>2:
        print (s.count(c))
        b=False
    
