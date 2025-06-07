base=int(input('inserire numero dispari >=3: '))
b=1
d=int((base-1)/2)
for a in range(0,base,2):
    print(' '*d+'*'*b)
    b+=2
    d-=1
         
