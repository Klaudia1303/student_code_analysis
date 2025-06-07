n= int(input('Inserire un numeratore: '))
d= int(input('Inserire un denominatore: '))
if n<d:
    print ('n/d è una frazione propria')
elif n>=d:
    if n%d==0:
        print ('n/d è una frazione apparente')
    else:
        print ('n/d è una frazione impropria')
