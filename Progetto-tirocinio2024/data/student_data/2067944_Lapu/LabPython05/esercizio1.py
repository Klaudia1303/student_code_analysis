a=input("inserire una stringa ")
b=input("inserire una stringa di lunghezza uguale alla prima ")
if len(a)==len(b):
    x=0
    for i in range (x,len(a)):
        print(a[x]+b[x],end='')
        x+=1
else:
    print("la lunghezza delle stringhe è diversa")
