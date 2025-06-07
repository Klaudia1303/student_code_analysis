s1=input('inserire stringa principale:\t')
s2=input('inserire stringa contente caratteri da eliminare in stringa precedente:\t')
for i in s1:
    if not i in s2:
        print(i,end='')
    
