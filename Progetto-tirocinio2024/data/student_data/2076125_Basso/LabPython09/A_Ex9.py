def A_Ex9(fileName,squadra):
    f=open(fileName)
    riga=f.readline()
    riga=f.readline()
    dati=riga.strip().split(',')
    punti=0
    while len(riga)>0:
        if squadra in dati:
            x=dati.index(squadra)
            if x==0:
                if int(dati[2])>int(dati[3]):
                    punti=punti+3
                elif int(dati[2])==int(dati[3]):
                    punti=punti+1

            elif x==1:
                if int(dati[2])<int(dati[3]):
                    punti=punti+3
                elif int(dati[2])==int(dati[3]):
                    punti=punti+1
        riga=f.readline()
        dati=riga.strip().split(',')
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
