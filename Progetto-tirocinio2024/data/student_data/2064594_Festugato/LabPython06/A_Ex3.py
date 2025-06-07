for i in range(8):
    for j in range(8):
        n = i*j
        quoz = n//8
        resto = n%8
        numOttale = str(resto)
        while(quoz > 0):
            resto = quoz%8
            quoz = quoz//8
            numOttale += str(resto)
        print("0"+str(i)+" x 0"+str(j)+" = "+numOttale[::-1], end=" | ")
    print()

