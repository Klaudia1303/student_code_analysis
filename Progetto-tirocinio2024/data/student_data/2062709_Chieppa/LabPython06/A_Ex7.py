s1=input('inserire stringa: ')
s2=input('inserire stringa: ')
risultato=''
len_max=0
for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            s=s1[i:j]
            l=j-i
            if s in s2:
                l=j-i
                if l>=len_max:
                    len_max=l
                    risultato=s
            else:
                break
print(risultato)
