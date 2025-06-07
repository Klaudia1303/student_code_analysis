s=input('Inserire stringa: ')
i=0
n=0
p='0'
while i<len(s):
    if s.count(s[i])>n:
        n=s.count(s[i])
        p=s[i]
    elif  s.count(s[i])==n:
        p=s[max(s.rfind(s[i]),s.rfind(p))]
    i+=1
print(p)
