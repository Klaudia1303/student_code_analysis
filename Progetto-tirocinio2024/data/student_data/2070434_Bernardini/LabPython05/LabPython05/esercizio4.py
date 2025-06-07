n1=int(input('inserire primo numero: '))
n2=int(input('inserire secondo numero: '))
for i in range (1, n2):
    f=n1*i
    if f<n2:
        print(f)
    
