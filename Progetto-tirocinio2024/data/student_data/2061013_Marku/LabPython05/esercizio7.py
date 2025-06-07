s=input('inserire una stringa: ')
count=0
for c in s:
    if s.count(c)>=2:
        count+=1
if count==0:
    print('False')
else:
    print('True')
