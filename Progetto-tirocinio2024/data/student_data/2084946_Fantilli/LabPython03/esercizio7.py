c = input("carattere: ")
s = input("stringa: ")
while s.count(c)<=2:
    s = input("stringa: ")
    if s.count(c)>2:
        print(s.count(c))
