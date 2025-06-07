c=0
s=input('inserire una stringa: ')
n=int(input('inserire una numero: '))
i=0
l=len(s)
st=s[0]*n
st=str(st)
for c in range(l):
    st=str(st)+str(s[i])*n
    i+=1
    c+=1
print(st)
    
