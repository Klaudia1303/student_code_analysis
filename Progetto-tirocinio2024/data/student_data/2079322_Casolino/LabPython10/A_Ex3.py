def A_Ex3(fileName):
    fin=open(fileName, 'r', encoding="UTF-8")
    materie=set()
    d={}
    campi=fin.readline() #consuma la prima riga
    campi=campi.strip().split(',')
    riga=fin.readline()
    while len(riga)>0:
        riga=riga.strip().split(',')
        if len(riga)==len(campi):
            materie.add(riga[2])
            for i in materie:
                l=[]
                if i==riga[2] and int(riga[1])>17:
                    d[riga[2]]=d.get(riga[2],[])+[int(riga[0])]
                    d[riga[2]]=sorted(d[riga[2]])
        riga=fin.readline()
    return d

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
