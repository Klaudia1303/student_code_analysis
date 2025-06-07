s=input('inserire una stringa: ')
r=input('inserire una stringa: ')
t=input('inserire una stringa: ')

while len(s)+len(r)!=len(t):
    s=r
    r=t
    t=input('inserire una stringa: ')
print(s,r,t)
