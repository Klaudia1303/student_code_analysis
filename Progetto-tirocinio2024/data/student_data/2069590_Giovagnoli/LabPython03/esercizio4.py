n = int(input("Inserire un primo numero intero compreso tra 0 e 10: "))
n1 = int(input("Inserire un secondo numero intero compreso tra 0 e 10: "))
i = 0
while i<=10:
    if i==n or i==n1:
        i+=1
    else:
        print(i,"\n")
        i+=1