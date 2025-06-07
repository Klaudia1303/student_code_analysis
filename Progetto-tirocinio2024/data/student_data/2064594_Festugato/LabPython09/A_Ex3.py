def A_Ex3(fileName):
    materie = list()
    risultato = set()
    file = open(fileName,'r',encoding='UTF-8')

    intestazione = file.readline().strip().split(',')

    for riga in file:#loop sul file dalla riga 1
        riga = riga.strip().split(',')
        voto = int(riga[1])
        
        if voto >= 29 : #voto maggiore di 29
            materie.append(riga[2])#salvo le materie voto > di 29   

    #print(materie)
    
    for materia in materie: #loop su lista di materie con voto>29
        if materie.count(materia)>=2:#cerca la materia che compare 2 volte perche ha due 29
            risultato.add(materia)

    return risultato
            
            
            
            
            
    
















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
