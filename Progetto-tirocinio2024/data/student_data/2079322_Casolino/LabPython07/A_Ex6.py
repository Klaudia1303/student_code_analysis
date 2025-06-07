#Scrivere una funzione che prende in ingresso due liste l1 e l2 contenenti numeri interi e restituisce una lista contenente gli elementi di l1 che NON compaiono in l2.
#Nella lista restituita gli elementi devono comparire in ordine crescente.
#Si noti che eventuali ripetizioni di un elemento x in l1 sono tutte non presenti nel risultato se x compare anche solo una volta in l2,
#mentre sono tutte presenti nel risultato se x non compare in l2. Ovviamente, se la lista l1 è vuota la funzione deve restituire la lista vuota,
#invece se l2 è vuota, la funzione deve restituire una lista uguale a l1.
#Ad esempio, se l1 = [1, 3, 7, 2, 1,-5, 7] e l2 = [1, 3], la funzione deve restituire la lista [-5, 2,7,7]

def A_Ex6(l1, l2):
    l3=[]
    if len(l1)==0:
        return l3
    for i in l1:
        if i not in l2:
            l3.append(i)
    l3.sort()
    return l3


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 3]],[-5, 2])
    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 1, 1]],[-5, 2, 3])
    counter_test_positivi += tester_fun(A_Ex6, [[10, 1, 10, 1, 2],[10, 1, 2]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[],[1, 1, 1]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[100, 12, -2, -1, -2],[]],[-2, -2, -1, 12, 100])

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
