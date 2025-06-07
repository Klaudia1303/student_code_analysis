c=input('inserire un carattere   ')
while len(c)!=1:
    c=input('inserire il carattere   ')
s=input('inserire una stringa   ')
print(s.count(c))
while s.count(c)<3:
    s=input('inserire una stringa   ')
    print(s.count(c))
