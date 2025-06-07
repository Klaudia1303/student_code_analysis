def A_Ex3(fileName):
    file = open(fileName, encoding= 'UTF-8')
    l = []
    for elem in file :
        elem = elem.strip().split(',')
        l.append(elem)
    l.remove(l[0])
    d = {}
    for riga in l :
        matricola = int(riga[0])
        voto = int(riga[1])
        materia = riga[2]
        if materia not in d and voto>= 18:
            d[materia] = [matricola]
        elif materia in d and voto>=18:
            lista = d[materia]
            lista.append(matricola)
            lista.sort()
            d[materia]= lista
    return(d)
        

        

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
