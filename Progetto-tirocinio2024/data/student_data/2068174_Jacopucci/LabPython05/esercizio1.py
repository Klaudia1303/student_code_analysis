c=0
s1=input('inserire una stringa: ')
s2=input('inserire una stringa della stessa lunghezza: ')
n=len(s1)
st=0
for c in range(n+1):
    st=st+str(s1[c])+str(s2[c])
print(st)
