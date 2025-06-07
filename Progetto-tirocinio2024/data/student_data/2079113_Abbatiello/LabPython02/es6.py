n = input('numeratore :')
d = input('denomitaore :')
n = int(n)
d = int(d)
if n < d :
    print('propria')
elif n > d and n % d !=0 :
    print('impropria')
elif n % d == 0:
    print('apparente')
