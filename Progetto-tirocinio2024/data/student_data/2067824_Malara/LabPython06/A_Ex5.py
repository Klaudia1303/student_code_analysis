s=input('inserire una stringa: ')
valore=0
for i in range(len(s)-2):
    c=s[i]
    acc=1    
    while s[i]==s[i+1]:
        i+=1
        acc+=1
        if i==len(s)-1:
            break
    if valore<=acc:
            valore=acc
            carattere=c
if valore==1:
    carattere=s[len(s)-1]
                

print(carattere,valore)






