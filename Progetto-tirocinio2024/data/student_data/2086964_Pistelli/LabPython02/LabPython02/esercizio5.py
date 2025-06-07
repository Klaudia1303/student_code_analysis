a=int(input('inserire un anno '))
if (a%4==0 and a%100!=0):
    print('anno bisestile')
elif a%2==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
