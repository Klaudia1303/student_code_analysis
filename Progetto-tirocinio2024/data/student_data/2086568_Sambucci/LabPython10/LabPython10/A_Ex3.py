def A_Ex3(fileName):
    fin=open(fileName,encoding="UTF-8")
    diz={}
    campi=fin.readline()
    campi=campi.strip().split(",")
    for dati in fin:
        dati=dati.strip().split(",")
        if len(dati)==len(campi):
            if int(dati[1])>=18:
                if dati[2] not in diz:
                    diz[dati[2]]=[int(dati[0])]
                else:
                    diz[dati[2]].append(int(dati[0]))

    fin.close()
    for k in diz:
        diz[k].sort()

    return diz
                                     
                                    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
