number=int(input('insert number: '))
counter=number-1
factors=0
while counter>=2:
    if number%counter==0:
        counter-=1
        factors+=1
    elif number%counter!=0:
        counter-=1    
if factors==0:
    print('numero primo')
elif factors>0:
    print('numero non primo')
