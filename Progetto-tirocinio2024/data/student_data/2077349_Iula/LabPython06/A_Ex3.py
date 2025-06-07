for i in range(1,11):
    for j in range(1,11):
           n=i*j
           q1=n//8
           r1=n%8
           if q1>=8:
            q2=q1//8
            r2=q1%8
            numero=str(q2)+str(r2)+str(r1)
           else:
            numero=str(q1)+str(r1)
           print(numero,end=" ")
    print()
        
