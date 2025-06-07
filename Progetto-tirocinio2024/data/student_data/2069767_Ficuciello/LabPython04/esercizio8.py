s1=input('Inserire una stringa:')
s2=input('Inserire una stringa:')
c=0
while s1!='' and s2!='':
    c+=1
    s1=input('Inserire una stringa:')
    s2=input('Inserire una stringa:')
    if s1[:1]==s2[:1]:
        print(s1,s2)
    
