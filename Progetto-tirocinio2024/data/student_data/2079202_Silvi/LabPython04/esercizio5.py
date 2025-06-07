n=int(input("inserire un numero intero maggiore o uguale di 0:"))
nF=1
for i in range (0,n):
    if n==0 or n==1:
        nF=1
    else:
        nF*=n-i
    
print(nF)
