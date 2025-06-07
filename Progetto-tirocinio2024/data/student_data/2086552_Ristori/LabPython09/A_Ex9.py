def A_Ex9(fileName,squadra):
    fin=open(fileName,"r",encoding="UTF-8")
    riga=fin.readline()
    riga=fin.readline()
    punti=0
    while len(riga)>0:
        dati=riga.strip().split(",")
        if squadra in dati:
            if dati[0]==squadra:
                if dati[2]>dati[3]:
                    punti+=3
                elif dati[2]==dati[3]:
                    punti+=1
                else:
                    punti=punti
            if dati[1]==squadra:
                if dati[3]>dati[2]:
                    punti+=3
                elif dati[3]==dati[2]:
                    punti+=1
                else:
                    punti=punti
        riga=fin.readline()
    return punti
        
    
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
