s=input('inserire una stringa:')
finito=False
for i in s:
    if s.count(i)>=2 and not finito:
        print(s.rfind(i))
        finito=True
if finito==False:
    print('0')
        
