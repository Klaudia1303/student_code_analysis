x=int(input('numeratore'))
y=int(input('denominatore'))
if x<y:
    print('propria')
if x%y==0:
    print('apparente')
if x>y and x%y!=0:
    print('impropria')
    
    
