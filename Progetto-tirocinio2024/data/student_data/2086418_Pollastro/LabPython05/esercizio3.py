s1=str(input('inserire stringa: '))
s2=str(input('inserire stringa: '))
nuova_stringa=''
d=0
for i in range(len(s1)):
    if not s1[i] in s2:
        print(s1[i], end='')
    
    
