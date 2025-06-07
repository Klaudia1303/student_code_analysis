print("questo programma restituisce tutti i numeri compresi tra 1 e 10, esclusi quelli che verranno inseriti in input\n")
x=int(input("inserire primo numero compreso tra 1 e 10:"))
y=int(input("inserire secondo numero compreso tra 1 e 10:"))
i=1
while i<=10:
    if i!=x and i!=y:
        print(i)
    i+=1
    
