base = int(input("Inserire un numero dispari >= a 3:"))
z = base//2
c = 1
for i in range(z+1):
        print(" "*z+"*"*c)
        z-=1
        c+=2
