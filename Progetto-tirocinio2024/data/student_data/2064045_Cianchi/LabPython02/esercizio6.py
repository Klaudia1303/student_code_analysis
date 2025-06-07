n=input('inserire un numeratore:')
n=int(n)
d=input('inserire un denominatore:')
d=int(d)
if n<d:
    print('frazione propria')
elif n%d==0:
    print('frazione apparente')
elif n>d and n%d!=0:
    print('frazione impropria')

