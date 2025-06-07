def A_Ex3(fileName):
    d = dict()
    f = open(fileName,'r',encoding = 'UTF-8')

    intestazione = f.readline().strip().split(',')

    for riga in f:
        riga= riga.strip().split(',')
       
        print(riga)
        matricola = int(riga[0])
        voto = int(riga[1])
        materia = riga[2]

        if voto >=18:
            if materia not in d:
                d[materia] = [matricola]

            else:
                d[materia].append(matricola)

            d[materia].sort()
    
          

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
