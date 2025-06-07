def A_Ex3(fileName):
    diz={}
    f=open(fileName)
    riga=f.readline()
    righe=f.readlines()
    for i in range(len(righe)):
        parola=righe[i].strip().split(',')
        if int(parola[1])>17:
            matricola=parola[0]
            materia=parola[2]
            if not materia in diz:
                insieme=[]
                insieme.append(int(matricola))
                diz[materia]=insieme
            else:
                n=diz.get(materia)
                n.append( int(matricola))
                n.sort()
                diz[materia]=n
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
