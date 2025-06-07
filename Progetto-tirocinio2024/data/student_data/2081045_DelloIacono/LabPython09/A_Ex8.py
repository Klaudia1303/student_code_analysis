def A_Ex8(fileName):
    f = open(fileName, encoding = "UTF-8")
    s = f.readlines()
    cont = 0
    maxCont = 0
    pos = 1
    maxPos = 1
    for riga in s:
        for parola in riga.split():
            for i in range(len(parola)):
                if(parola.isalpha() and parola[i].isupper()):
                    cont += 1
        if(cont >= maxCont):
            maxCont = cont
            maxPos = pos
        pos += 1
        cont = 0
    f.close()
    return(maxPos)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
