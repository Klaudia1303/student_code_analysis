n=int(input('inserire numero dispari: '))
x=1
spazi=(n//2)
for i in range((n//2)+1):
    print((' '*spazi),('*'*x))
    x=x+2
    spazi=spazi-1
