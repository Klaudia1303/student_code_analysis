a=int(input('inserici un numero '))
if a%5==0:
    print(a//5)
else:
    while a%5!=0:
        a=int(input('inserici un numero '))
        if a%5==0:
            print(a//5)
   
