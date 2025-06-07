n=int(input('numeratore '))
d=int(input('denominatore '))
if n<d :
    print('frazione propria')
if n%d==0 :
    print('frazione apparente')
if n>d and n%d!=0 :
    print('impropria')

