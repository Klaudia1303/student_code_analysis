c=input('inserire carattere: ')
a=True
while a:
    s=input('inserire stringa: ')
    if s.count(c)>2:
        print(s.count(c))
        a=False
