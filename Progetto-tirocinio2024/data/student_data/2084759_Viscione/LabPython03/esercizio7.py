c=input("immetti un carattere: ")
termina=False
while not termina:
    s=input("immetti una stringa: ")
    if s.count(c)>2:
        termina=True
        print(s.count(c))
