s1=input('insereire una stringa (non vuota) ')
s2=input('insereire una stringa (non vuota) ')
strMax=''
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        slicing=s1[i:j]
        if slicing in s2:
            if len(strMax)<len(slicing):
                strMax=slicing
        else:
            break 
print(strMax)
    
         
