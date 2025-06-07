s=input('Inserire stringa: ')
for i in s:
    if s.count(i)>1:
        k='True'
    else:
        k='False'
print(k)
