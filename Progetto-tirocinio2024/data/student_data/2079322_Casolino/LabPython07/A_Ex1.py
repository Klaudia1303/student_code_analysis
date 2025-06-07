#Scrivere una funzione che, ricevendo in ingresso due liste l1 e l2 contenenti
#numeri interi, e tali che len(l2)>= len(l1), restituisca una nuova lista
#composta dalla somma degli interi che si trovano nella stessa posizione in l1
#e l2. Se l1 è più corta si assuma che gli interi mancanti siano uguali a 0.
#Ad esempio, se l1 vale [3,6] e l2 vale [3,4,9] la funzione deve restituire
#[6, 10, 9]. Se l1 ed l2 sono entrambe vuote (cioè pari a []),
#la funzione deve restituire una lista vuota.

def A_Ex1(l1, l2):
    l3=[]
    if len(l1)==len(l2) and len(l1)==0:
        return l3
    for position in range (len(l2)):
        if position>=len(l1):
            somma=int(l2[position])
            l3.append(somma)
        else:
            somma=int(l1[position])+int(l2[position])
            l3.append(somma)
    return l3


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
