latoA=int(input('lato a: '))
latoB=int(input('lato B: '))
latoC=int(input('lato C: '))
if(latoA>latoB):
    latoA,latoB=latoB,latoA
if(latoA>latoC):
    latoA,latoC=latoC,latoA
if(latoB>latoC):
    latoB,latoC=latoC,latoB
if((latoA+latoB)>=latoC):
    if(latoA==latoB==latoC):
        print('equilatero')
    elif(latoA==latoB!=latoC):
        print('isoscele')
    elif(latoA!=latoB!=latoC):
        print('scaleno')
else:
    print('input non valido')