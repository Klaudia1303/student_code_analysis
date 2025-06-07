temp=input('iserisci una temperatura: ')
temp=float(temp)
if (temp<=10):
    print('con questa temperatura fa freddo')
else:
    if (10<temp<=20):
        print('la temperatura è gradevole')
    else:
        if (20<temp<=30):
            print('con questa temperatura fa caldo')
        else:
            print('con questa temperatura fa molto caldo')
