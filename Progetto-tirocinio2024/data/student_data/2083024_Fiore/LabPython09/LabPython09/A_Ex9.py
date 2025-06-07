def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(fileName, "r", encoding="UTF-8")
    punti = 0
    for riga in f:
        lista = riga.strip().split(",")
        for i in range(len(lista)):
            if lista[i] == squadra:
                if i == 0:
                    if int(lista[i+2]) > int(lista[i+3]):
                        punti += 3
                    elif int(lista[i+2]) == int(lista[i+3]):
                        punti += 1
                elif i == 1:
                    if int(lista[i+1]) < int(lista[i+2]):
                        punti += 3
                    elif int(lista[i+1]) == int(lista[i+2]):
                        punti += 1
                        
                        
    return punti
                
 
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
