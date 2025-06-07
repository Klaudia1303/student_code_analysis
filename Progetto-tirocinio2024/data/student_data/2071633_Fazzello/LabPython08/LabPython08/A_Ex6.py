## Scrivere una funzione che prende in ingresso una lista l di stringhe, un carattere c ed un 
##numero intero n e restituisce una lista ottenuta da l eliminando tutte le stringhe che contengono almeno 
##n volte il carattere c. Ad esempio, se l = ['palla','casse','palo'], c = ‘a’ ed n = 2 allora la funzione deve 
##restituire la lista ['casse','palo']. Si noti che le stringhe non eliminate compaiono nel risultato nello 
##stesso ordine in cui compaiono in l. Ovviamente se la lista l in ingresso è vuota, la funzione deve 
##restituire una lista vuota.

def A_Ex6(l,c,n):
    l1=list()
    for i in range(len(l)):
        if l[i].count(c)<n:
            l1.append(l[i])
    return l1
    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [['palla','casse','palo'],'a',2] ,['casse','palo'])
    counter_test_positivi += tester_fun(A_Ex6, [['palla','casse','palo'],'p',1] ,['casse'])
    counter_test_positivi += tester_fun(A_Ex6, [['pallone','casse','palla','pappa'],'p',2] ,['pallone','casse','palla'])
    counter_test_positivi += tester_fun(A_Ex6, [['pallone','casse','palla','pappa'],'a',1], [])
    counter_test_positivi += tester_fun(A_Ex6, [[],'a',1] , [])


    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
