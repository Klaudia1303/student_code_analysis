b=True
while b:
    x=int(input("Inserire il primo numero: "))
    if x<11 and x>-1:   b=False
    else:   print("\nValore non compreso tra 0 e 10. Reinserire\n")
b=True
while b:
    y=int(input("Inserire il secondo numero: "))
    if y<11 and y>-1:   b=False
    else:   print("\nValore non compreso tra 0 e 10. Reinserire\n")
i=0
while i<11:
    if i!=x and i!=y:    print("\n",i)
    i+=1
