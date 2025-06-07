def A_Ex3(fileName):

    materie = set()

    AlmenoUno = set()
    
    with open(fileName, "r", encoding="UTF-8") as file:
        titoli = file.readline().strip().split(",")

        riga = file.readline()

        while len(riga) > 0:
            dati = riga.strip().split(",")
            print(dati)

            voto = int(dati[1])
            
            if voto >= 29 and dati[2] in AlmenoUno:
                materie.add(dati[2])
            else:
                AlmenoUno.add(dati[2])
                
            riga = file.readline()

    return materie
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
