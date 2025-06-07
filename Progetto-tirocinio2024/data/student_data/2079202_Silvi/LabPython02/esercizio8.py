print("questo programma verifica se, inseriti i lati, un tringolo possa essere costruito e il suo tipo\n")
a=int(input("inserire primo lato:"))
b=int(input("inserire secondo lato:"))
c=int(input("inserire terzo lato:"))
if a>0 and b>0 and c>0:
    
    if a<b+c and b<c+a and c<b+a:
        
        if a==b and b==c:
            print("triangolo equilatero")

        else:
            if a==b or a==c or b==c:
                print("triangolo isoscele")

            else:
                print("triangolo scaleno")
        
    else:
        print("input non valido")
        
else:
    print("input non valido")
