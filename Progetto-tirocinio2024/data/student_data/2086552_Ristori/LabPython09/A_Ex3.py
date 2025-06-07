def A_Ex3(fileName):
    fin=open(fileName,"r",encoding="UTF-8")
    riga=fin.readline()
    riga=fin.readline()
    lista=[]
    ris=set()
    while len(riga)>0:
        dati=riga.strip().split(",")
        matricola=dati[0]
        voto=int(dati[1])
        materia=dati[2]
        if voto>=29:
            lista.append(materia)
        riga=fin.readline()
    for i in range(len(lista)):
        voce=lista[i]
        if lista.count(voce)>=2 and voce not in ris:
            ris.add(voce)
    return ris


    
        
        
        

    


    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
