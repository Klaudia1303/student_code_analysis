def A_Ex9(fileName,squadra):
    f = open (fileName, "r", encoding = "UTF-8")
    punti = 0
    for riga in f:
        riga = riga.strip().split(",")
        if squadra in riga:
            index = riga.index(squadra)
            if index%2 == 0:
                if int(riga[index+2]) > int(riga[index+3]):
                    punti = punti + 3
                elif riga[index+2] == riga[index+3]:
                    punti = punti + 1
            if index%2 == 1:
                if int(riga[index+1]) < int(riga[index+2]):
                    punti = punti + 3
                elif riga[index+1] == riga[index+2]:
                    punti = punti + 1
    f.close()
    return punti
                
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
