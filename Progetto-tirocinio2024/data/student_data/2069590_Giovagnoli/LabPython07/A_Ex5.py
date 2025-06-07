def A_Ex5(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso una lista l di stringhe e restituisce una lista di
    #interi, tale che ciascun intero x nella lista restituita è ottenuto dalla somma dei codici Unicode dei
    #caratteri della stringa che in l occupa la stessa posizione che occupa x nella lista restituita. Ad esempio,
    #se l è [‘ama’, ‘ma’, ‘amaca’] la funzione dovrebbe restituire la lista [303,206,499], in quanto il codice
    #Unicode di ‘a’ è 97, quello di ‘m’è 109 e quello di ‘c’è 99 (e quindi ad esempio ad ‘ama’ corrisponde
    #l’intero 303). Se la lista in input è vuota, la funzione deve restituire una lista vuota

    lista=[]
    for i in l:
        somma=0
        for j in i:
            somma=somma+ord(j)
        lista.append(somma)
    return lista

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
