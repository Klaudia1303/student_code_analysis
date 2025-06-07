def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(fileName,'r',encoding='utf-8')
    d = {}
    f.readline()
    for partita in f:
        ris = partita.strip().split(',')
        team1 = ris[0].strip()
        team2 = ris[1].strip()
        gol1 = int(ris[2])
        gol2 = int(ris[3])
        if gol1 > gol2:
            d[team1] = d.get(team1,0) + 3
            d[team2] = d.get(team2,0) + 0
        elif gol1 == gol2:
            d[team1] = d.get(team1,0) + 1
            d[team2] = d.get(team2,0) + 1
        else:
            d[team2] = d.get(team2,0) + 3
            d[team1] = d.get(team1,0) + 0
    f.close()
    if squadra not in d:
        return 0
    else:
        return d.get(squadra)
 
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
