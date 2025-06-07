def A_Ex3(fileName):
    f = open(fileName)
    r = f.readlines()
    dizionario = {}
    found_lista = []
    for l in range(1, len(r)):
        r[l] = r[l].strip().split(",")
        esame = r[l][2]
        if esame not in dizionario.keys() and int(r[l][1]) >= 18:
            matricola = []
            matricola.append(int(r[l][0]))
            dizionario.update({esame:matricola})
        elif int(r[l][1]) >= 18:
            matricola2 = int(r[l][0])
            dizionario[r[l][2]].append(int(r[l][0]))
            dizionario[r[l][2]].sort() 
        voti = []
    return dizionario
    
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
