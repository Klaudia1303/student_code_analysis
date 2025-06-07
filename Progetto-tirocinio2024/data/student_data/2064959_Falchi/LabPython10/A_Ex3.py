def A_Ex3(fileName):
    votoMinimo = 18
    d = dict()

    with open(fileName, "r", encoding="UTF-8") as file:
        riga = file.readline().strip().split(",") #Titoli della tabella
        print(riga, len(riga))

        riga = file.readline().strip().split(",")
        
        while len(riga) > 1:
            matricola = riga[0]
            voto = riga[1]
            materia = riga[2]
            
            if not materia in d:
                d[materia] = list()

            if int(voto) >= votoMinimo:
                d[materia].append(int(matricola))

            riga = file.readline().strip().split(",")
            print(riga, len(riga))

        filtro = list()
        
        for chiave in d: #Riordina i valori nel dizionario
            if d[chiave] == []: #aggiunge ad una blacklist le chiavi con valore vuoto
                filtro.append(chiave)
                continue
            d[chiave].sort()

        for elem in filtro: #rimuove dal dizionario le chiavi con valore vuoto
            d.pop(elem)
            
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
