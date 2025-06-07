carattere=input('digitare carattere: ')
s=str(input('digitare stringa: '))
while s.count(carattere)<=2:
    s=str(input('digitare stringa: '))
print(s.count(carattere))
