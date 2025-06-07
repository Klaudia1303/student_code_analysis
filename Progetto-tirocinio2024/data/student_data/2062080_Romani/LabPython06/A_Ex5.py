s=input('Inserire stringa: ')
x=0
x_correnti=0
ch=''
for c in range(0, len(s)-1):
    if s[c]!=s[c+1]:
        x_correnti=0
    else:
        ch=s[c]
        x_correnti+=1
        x=max(x,x_correnti+1)
        c+=1
print(ch,x)
