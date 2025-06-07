x=0
y=0
z=0
for i in range (1,8) :
    for j in range (1,8) :
        z=i*j
        x=str(z//8)+str(z%8)
        print (str (i)+ '*' + str(j) + '=' + x)
print()
