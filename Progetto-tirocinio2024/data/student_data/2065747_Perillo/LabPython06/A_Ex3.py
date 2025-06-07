valore=""
x=""
u=""
v=""
for i in range(0,8):
    for j in range(1,8):
        n=i*j
        if n%8!=0:
            valore=n%8
            x=(n-valore)//8
            u="0"+str(i)
            v="0"+str(j)
            print(str(u),"X",str(v),"=",str(x)+str(valore))
    
