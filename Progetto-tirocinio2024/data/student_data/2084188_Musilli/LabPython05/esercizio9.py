b=True
while b:
    lato=int(input("Inserire la misura del lato del \
quadrato (dispari e >=3): "))
    if lato%2!=0 and lato>=3: b=False
    else:   print("\n\tValore inserito non valido! Deve essere dispari e >=3\n")
j=lato-2
for i in range(lato):
    if i==0 or i==(lato-1): print("*"*lato)
    else: print("*"+" "*j+"*")
