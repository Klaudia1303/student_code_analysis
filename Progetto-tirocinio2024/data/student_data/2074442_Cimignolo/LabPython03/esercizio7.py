s=input('inserisci un carattere: ')
boo=True

while boo:
    t=input('inserisci una stringa: ')
    u=t.count(s)
    v=int(u)
    if v>2:
        print(v)
        boo=False
        
