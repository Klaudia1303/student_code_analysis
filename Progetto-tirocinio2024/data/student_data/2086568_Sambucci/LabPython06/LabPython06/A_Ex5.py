s=input('Inserire stringa: ')
while len(s)==0:
    print('Hai inserito una stringa vuota!')
    s=input('Inserire stringa: ')
occmax=0
for i in range(len(s)):
    k=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            k+=1
        else:
            break
    if k>=occmax:
        occmax=k
        maxc=s[i]
print(maxc,occmax)
        
            
    
