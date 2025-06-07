x=int(input('inserire primo numero: '))
y=int(input('inserire secondo numero: '))
i=int(x)
while i>0:
    if x%i==0 and y%i!=0:
        print(i)
    i -= 1
