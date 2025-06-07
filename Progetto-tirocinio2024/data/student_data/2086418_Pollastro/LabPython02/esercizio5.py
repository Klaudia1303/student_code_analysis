a=int(input('inserire un anno'))
x=a%4 
if x==0 and a%100!=0 or a%400==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
    
