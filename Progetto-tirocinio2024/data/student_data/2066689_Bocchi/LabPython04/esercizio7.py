s= input('inserisci stringa: ')
x=0
mas=1

while x < len(s):  
    n = s.count(s[x])
    if n>mas:
        print(s[-x])
        mas = n
    else:
        x= x+1
