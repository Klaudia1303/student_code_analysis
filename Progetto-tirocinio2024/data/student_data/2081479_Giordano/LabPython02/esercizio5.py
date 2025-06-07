anno=int(input('anno'))
if(anno%4==0):
    if(anno%100!=0):
        print('anno bisestile')
    elif(anno%400==0):
        print('anno bisestile')
    else:
        print('anno non bisestile')

else:
    print('anno non bisestil')