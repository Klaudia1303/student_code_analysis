s=input('stringa: ')
isBool= False
for i in s:
    if s.count(i)>1:
        isBool=True
if isBool:
    print('true')
else:
    print('False')
