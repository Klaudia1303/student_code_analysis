c=input("inserire un carattere: ")
s=chr(int(ord(c))+1)
while s.count(c)<=2:
    s=input("inserire una stringa: ")
    if s.count(c)>2:
        print(s.count(c))
