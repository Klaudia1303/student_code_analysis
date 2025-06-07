s=input('inserire una stringa:')
n=int(input('inserire un intero:'))
i=0
finito=False
while not finito and (i+n)<len(s):
    if s[i]==s[i+n]:
        print('True')
        finito=True
    i+=1
if finito==False:
    print('False')
    
    
