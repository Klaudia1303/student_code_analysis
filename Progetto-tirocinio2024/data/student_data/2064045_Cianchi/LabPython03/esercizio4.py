x=int(input('inserire un numero compreso fra 0 e 10:'))
y=int(input('inserire un numero compreso fra 0 e 10:'))
if not 0<=x<=10 or not 0<=y<=10:
    print('numeri errati')
i=0
while i<=10:
    if not i==x and not i==y:
        print(i)
    i+=1
    
