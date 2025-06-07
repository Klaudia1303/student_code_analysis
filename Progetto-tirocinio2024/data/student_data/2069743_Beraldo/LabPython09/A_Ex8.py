def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

    file = open(fileName,'r', encoding='UTF-8')
    somma = 0
    index = 0
    indexRiga = 0
    for riga in file:
        sommaAct = 0
        index += 1
        #print('Controllo pwer :' + str(index))
        for i in range(len(riga)):
                if(riga[i].isupper() and riga[i].isalpha()):
                    sommaAct += 1
        if(somma < sommaAct):
            somma = sommaAct
            indexRiga = index
            sommaAct = 0
        elif(somma == sommaAct):
            if(index > indexRiga):
                indexRiga = index
                
            sommaAct = 0
    return indexRiga
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
