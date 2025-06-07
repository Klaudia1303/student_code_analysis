s1=input('Inserire prima stringa: ')
s2=input('Inserire seconda stringa: ')
lenmax=0
smax=''
for i in range (len(s1)):
    sq=''
    if s1[i] in s2:
        sq=sq+s1[i]
        t=s1.find(s1[i])+1
        z=s2.find(s1[i])+1
        for j in range(t,len(s1)):
            if z<len(s2):
                if s1[j]==s2[z]:
                    sq=sq+s1[j]
                else:
                    break
            else:
                break
            z+=1
        if len(sq)>lenmax:
            lenmax=len(sq)
            smax=sq
print('Sequenza di caratteri più lunga:',smax)
            
    
