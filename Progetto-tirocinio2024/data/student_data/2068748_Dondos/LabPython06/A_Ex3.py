for i in range(1, 9):
    for j in range(1, 9):
        n = i*j
        quoziente1 = n//8
        resto = n%8
        resti = str(resto)

        if quoziente1 == 0:
            ottale = resto
        else:
            while quoziente1 != 0:
                quoziente = quoziente1//8
                resto = quoziente1%8
                resti += str(resto)
                valore = resti[::-1]
                quoziente1 = quoziente
                ottale = int(valore)
        if(ottale < 10):
            print("0", i, "x", "0", j, "=", "0", ottale, sep='')
        else:
            print("0", i, "x", "0", j, "=", ottale, sep='')
