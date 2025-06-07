n=int(input("Inserisi la base del triangolo isoscele (num. dispari > di 3)"))
while n<3 or n%2==0:
    print("ERRORE")
    n=int(input("Inserisi la base del triangolo isoscele (num. dispari > di 3)"))
for i in range (n+1):
    if i%2!=0:
        print(((n-i)//2)*" ","*"*i)
