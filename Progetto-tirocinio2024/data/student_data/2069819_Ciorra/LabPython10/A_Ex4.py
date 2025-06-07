def A_Ex4(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    d={}
    votoM = 18
    with open(fileName, "r", encoding="utf-8") as f:
        riga = f.readline().strip().split(",")
        riga = f.readline().strip().split(",")
        while len(riga) > 1:
            matricola = int(riga[0])
            voto = riga[1]
            materia = riga[2]
            if matricola not in d:
                d[matricola] = 0
            if int(voto) >= votoM:
                d[matricola] += 1
            riga = f.readline().strip().split(",")
        fnull = list()
        for c in d:
            if d[c] == 0:
                fnull.append(c)
        for elem in fnull:
            d.pop(elem)
    return d

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
