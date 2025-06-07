corretto=False
c=input('Inserire carattere: ')
while not corretto:
    s=input('Inserire stringa: ')
    if s.count(c)>2:
        print(s.count(c))
        corretto=True
