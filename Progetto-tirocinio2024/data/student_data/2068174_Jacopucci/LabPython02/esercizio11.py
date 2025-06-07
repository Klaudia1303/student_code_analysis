temp=input('inserire unvalore intero: ')
temp=int(temp)
if(temp<=10):
    print ('freddo')
else:
    if (temp>10 and temp<=20):
        print('sgradevole')
    else:
        if (temp>20 and temp<=30):
            print('caldo')
        else:
            print('molto caldo')
