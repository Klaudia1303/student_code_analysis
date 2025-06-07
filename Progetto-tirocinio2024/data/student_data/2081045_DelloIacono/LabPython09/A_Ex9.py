def A_Ex9(fileName,squadra):
    f = open(fileName, encoding = "UTF-8")
    n = 0
    for riga in f:
        riga = riga.split(",")
        if(riga[0] != "Nome_Squadra1"):
            for i in range(len(riga)):
                if(riga[i] != "Anno" and riga[i]==squadra):
                    p = i + 2
                    if(p == 2):
                        if(int(riga[p]) > int(riga[i+3])):
                            n += 3
                        elif(int(riga[p]) == int(riga[i+3])):
                            n += 1
                    else:
                        if(int(riga[p]) > int(riga[i+1])):
                            n += 3
                        elif(int(riga[p]) == int(riga[i+1])):
                            n += 1
    f.close()
    return(n)
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
