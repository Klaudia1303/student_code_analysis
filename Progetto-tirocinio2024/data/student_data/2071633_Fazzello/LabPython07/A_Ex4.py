##Scrivere una funzione che prende in ingresso una lista l di interi e restituisce la stringa
##composta da soli caratteri ‘P’ e ‘D’ che indicano se l’intero nella lista è pari o dispari. Più precisamente,
##se il numero in posizione i in l è pari, la stringa restituita dalla funzione contiene ‘P’ in posizione i, ‘D’
##altrimenti. Se la lista è vuota la funzione deve restituire la stringa vuota. Ad esempio, se l vale [3,7,8,9]
##la funzione deve restituire la stringa ‘DDPD’.

def A_Ex4(l):
    s=''
    for i in range(len(l)):
        if l[i]%2==0:
            s=s+'P'
        else:
            s=s+'D'
    return s



###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [[3,7,8,9]], 'DDPD')
    counter_test_positivi += tester_fun(A_Ex4, [[3]], 'D')
    counter_test_positivi += tester_fun(A_Ex4, [[8]], 'P')
    counter_test_positivi += tester_fun(A_Ex4, [[]], '')
    counter_test_positivi += tester_fun(A_Ex4, [[7,7,7,7,8]], 'DDDDP')

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
