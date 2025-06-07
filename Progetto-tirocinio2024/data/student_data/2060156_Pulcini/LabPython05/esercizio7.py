s=input('inserire una stringa:')
finito=False
for i in s:
    if s.count(i)>1 and not finito:
        print('True')
        finito=True
if not finito:
    print('False')
