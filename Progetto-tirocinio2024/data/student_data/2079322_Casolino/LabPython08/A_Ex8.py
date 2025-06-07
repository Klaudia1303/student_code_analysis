#Scrivere una funzione che prende in ingresso una lista l di insiemi di numeri interi e
#restituisce un altro insieme contenente tutti e soli gli
#elementi che appaiono in uno ed uno solo degli insiemi in l.
#Ad esempio, se x=[{3,2,90},{2,87,23},{2,23,3}], allora
#l'insieme da restituire sarà {90,87}. Se la lista in ingresso è vuota,
#la funzione deve restituire un insieme vuoto.

def A_Ex8(l):

    insieme=set()
    if len(l)==0:
        return insieme

    insiemeA=set()
    l1=[]
    for i in l:
        i=list(i)               #converto l'insieme in una lista
        for j in i:             #prendo i singoli elementi della lista che sono quelli dell'insieme
            l1.append(j)        #...e li aggiungo alla lista l1 inizializzata prima

    l2=l1.copy()                #creo una copia della lista l1 per modificarla
    for elem in l1:             #prendo ciascun elemento della lista l1
        if l1.count(elem)>1:    #controllo quante volte quell'elemento è presente nella lista, se più di una volta lo tolgo dalla lista "copia"
            l2.remove(elem)
    insiemeA=set(l2)            #converto la lista con gli elementi rimossi in un insieme
    return insiemeA
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{-10},{2}]] , {-10,2})
    counter_test_positivi += tester_fun(A_Ex8, [[set()]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-2},{10},{-2}]] , set())
    counter_test_positivi += tester_fun(A_Ex8, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})


    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
