s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
maxi=0
st=''
for i in range (len(s1)):
    for j in range (i+1, len(s1)+1):
        s=s1[i:j]
        if s in s2:
            l=j-i
            if l>=maxi:
                maxi=l
                st=s
        else:
            break
print(st)
                
