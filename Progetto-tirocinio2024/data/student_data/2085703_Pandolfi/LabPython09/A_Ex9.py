def A_Ex9(fileName,squadra):
    f = open(fileName, "r")

    riga = f.readline()

    dati = []
    punteggio = 0

    while len(riga) > 0:
        riga = f.readline()
        dati = riga.strip().split(",")

        if len(riga) < 4:
            break

        i_squadra = 0
        i_avversario = 0

        if dati[0] == squadra:
            i_squadra = 2
            i_avversario = 3
        elif dati[1] == squadra:
            i_squadra = 3
            i_avversario = 2
        else:
            continue

        if int(dati[i_squadra]) > int(dati[i_avversario]):
            punteggio += 3
        elif int(dati[i_squadra]) == int(dati[i_avversario]):
            punteggio += 1         

    f.close()

    return punteggio



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
