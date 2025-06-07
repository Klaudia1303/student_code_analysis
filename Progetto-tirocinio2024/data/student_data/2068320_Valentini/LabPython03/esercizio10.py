n=int(input("Inserire un numero: "))
for loop in range(2,n+1):
   if loop > 1:
       for i in range(2, loop):
           if (loop % i) == 0:
               break
       else:
           print(loop)
