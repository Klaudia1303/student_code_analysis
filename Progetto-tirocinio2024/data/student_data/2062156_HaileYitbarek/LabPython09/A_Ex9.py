def A_Ex9(fileName,squadra):
    f=open(fileName,encoding='UTF-8')
    s=f.readline()
    punti=0
    for riga in f:
        riga=riga.strip().split(',')
        if squadra in riga:
            if riga[0]==squadra:
                a=int(riga[2])
                b=int(riga[3])
                if a>b:
                    punti+=3
                if a==b:
                    punti+=1
            else:
                a=int(riga[2])
                b=int(riga[3])
                if a<b:
                    punti+=3
                if a==b:
                    punti+=1
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
