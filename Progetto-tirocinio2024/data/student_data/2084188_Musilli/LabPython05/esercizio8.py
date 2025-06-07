b=True
while b:
    base=int(input("Inserire la misura della base del \
triangolo (dispari e >=3): "))
    if base%2!=0 and base>=3: b=False
    else:   print("\n\tValore inserito non valido! Deve essere dispari e >=3\n")
c=base//2; k=0
for i in range(base-c):
    print(" "*c+"*"*k+"*"+"*"*k+" "*c)
    k+=1; c-=1
