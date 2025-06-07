s1=input('Inserire stringa: ')
s2=input('Inserire stringa: ')
while s1[-1]!=s2[0]:
    s1=s2
    s2=input('Inserire stringa: ')
print(s1,s2)    
