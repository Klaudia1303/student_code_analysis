l=int(input("Inserire la base del quadrato(dispari>=3):"))
while(l%2==2 or l<3):
    l=int(input("Inserire la base del quadrato(dispari>=3):"))
star="*"*l
for i in range (l):
    if(i!=0 and i!=(l-1)):
        print(star[0]," "*(len(star)-2),star[l-1],sep="")
    else:
        print(star)
    
    
    
    
