s1=input('inserisci stringa: ')
s2=input('inserisci stringa: ')

i=0
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        if s1[1:j]in s2:
            
