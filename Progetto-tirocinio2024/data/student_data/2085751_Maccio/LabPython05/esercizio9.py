lato=int(input("Inserire un numero dispari intero maggiore di 3:  "))
a=int(lato-2)
for i in range(lato):
    if i==0 or i==lato-1:
        print("*"*lato)
    else:
        print("*"+" "*a+"*")
