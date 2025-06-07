def A_Ex7(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso una lista l di numeri interi positivi e restituisce
    #una lista ottenuta modificando l nel seguente modo: ogni volta che un numero all'interno di l è più
    #piccolo del successivo, alla lista viene aggiunta in fondo la differenza tra il secondo ed il primo dei
    #due numeri. Ad esempio, se l=[10,1,11,31,251], allora la lista da restituire sarà
    #[10,1,11,31,251,10,20,220,10,200,190]. Si noti che il confronto fra un numero ed il successivo deve
    #essere fatto anche per i nuovi elementi inseriti, come mostrato dall’esempio. Ovviamente, se la lista in
    #ingresso è vuota, la funzione deve restituire una lista vuota.
    l2=l.copy()
    n=0
    while n<len(l)-1:
        if l[n]<l[n+1]:
            differenza=l[n+1]-l[n]
            l.append(differenza)
        n+=1
    return l





###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, [[10,1,11,31,251]] , [10,1,11,31,251,10,20,220,10,200,190])
    counter_test_positivi += tester_fun(A_Ex7, [[]] , [])
    counter_test_positivi += tester_fun(A_Ex7, [[2,7,3]] , [2,7,3,5,2])
    counter_test_positivi += tester_fun(A_Ex7, [[200,501,300]] , [200,501,300,301,1])
    counter_test_positivi += tester_fun(A_Ex7, [[3,2,0]] , [3,2,0])


    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
