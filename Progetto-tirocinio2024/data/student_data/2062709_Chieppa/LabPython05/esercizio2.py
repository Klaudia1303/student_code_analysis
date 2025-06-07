s=str(input('inserire stringa: '))
n=int(input('inserire intero: '))
t=''
for i in range(len(s)):
    t=t+s[i]*n
print(t)
