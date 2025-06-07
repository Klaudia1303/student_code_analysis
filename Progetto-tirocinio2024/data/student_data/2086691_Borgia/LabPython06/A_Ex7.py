s1=input('Inserire una stringa: ')
s2=input('Inserire una stringa: ')
v=0
stot1=''
stot2=''
for i in range(len(s2)):
    for j in range(len(s1)):
        if s1[j]==s2[i]:
            stot=(stot+s1[j])
            break
print(stot)
