u=int(input('inserire primo intero:'))
n=int(input('inserire secondo intero:'))
i=0
x=0
u1= abs(u)
n1= abs(n)

while i<n1:
    x= x+u
    i+=1

if (u<0 and n>=0) or (u>=0 and n<0):
    x=-x

print(x)
