def A_Ex9(fileName,squadra):
        f=open(fileName, encoding='UTF-8')
        punti = 0

        for i in f.readlines():
            (squad1, squad2, punti1, punti2) = i.strip().split(',')
            
            if squad1 == squadra or squad2 == squadra:
                if punti1 > punti2:
                    punti += 3
                elif punti1 == punti2:
                    punti += 1

        f.close()
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
