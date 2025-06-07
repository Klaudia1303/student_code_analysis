c=input('inserire un carattere: ')
i=1
while 1!=0:
    s=input('inserire stringa: ')
    if s.count(c)>3:
        print(s.count(c))
        break
