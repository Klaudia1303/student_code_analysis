b=int(input("Inserire la base del triangolo isoscele(dispari>=3):"))
while(b%2==2 or b<3):
    b=int(input("Inserire la base del triangolo isoscele(dispari>=3):"))
star="*"
while (len(star)<=b):
    print(star)
    star+="**"
    
