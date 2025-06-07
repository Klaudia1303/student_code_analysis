def A_Ex8(fileName):
    
    contoMaiuscole = list()

    contoRiga = 0
    lunghezzaRiga = list()

    with open(fileName, "r", encoding="UTF-8") as file:
        for riga in file.readlines():
            #print(riga)
            lunghezzaRiga.append(len(riga))

            localCount = 0

            for lettera in riga:
                #print(lettera)
                if lettera.isupper():
                    localCount += 1

            contoMaiuscole.append(localCount)

    massimo = [0, 0]

    for i in range(len(contoMaiuscole)):
        if contoMaiuscole[i] >= massimo[1]:
            massimo = [i+1, contoMaiuscole[i]]
        '''elif contoMaiuscole[i] == massimo[1]:
            if lunghezzaRiga[massimo[0] - 1] < lunghezzaRiga[i]:
                massimo = [i+1, contoMaiuscole[i]]'''

    contoRiga = massimo[0]

    print(massimo)

    return contoRiga    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
