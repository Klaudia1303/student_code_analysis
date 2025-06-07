n=float(input('inserire numeratore:'))
d=float(input('inserire denominatore:'))
if n<d:
        print('propria')
elif n%d==0:
        print('apparente')
elif n>d and n%d!=0:
        print('impropria')
      
