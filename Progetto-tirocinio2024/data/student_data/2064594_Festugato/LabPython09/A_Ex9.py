def A_Ex9(fileName,squadra):
    punti = 0

    file = open(fileName,'r',encoding='UTF-8')

    intestazione = file.readline().strip().split(',') #intestazione listata

    for riga in file:
        riga = riga.strip().split(',')
        if squadra == riga[0]:
            if riga[2] > riga[3]:
                punti += 3
            elif riga[2] == riga[3]:
                punti += 1
            

        elif squadra == riga[1]:
            if riga[3] > riga[2]:
                punti += 3
            elif riga[3] == riga[2]:
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
