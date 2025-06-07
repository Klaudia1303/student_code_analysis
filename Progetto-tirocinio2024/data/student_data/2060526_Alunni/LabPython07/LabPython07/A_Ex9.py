def A_Ex9(l):
    v=[]
    a=0
    b=0
    k=0
    for i in range(len(l)):
        k=l[i]
        a=0
        b=0
        for j in range(len(k)):
            if k.count(k[j])==a:
                if ord(k[j])<ord(b):
                    b=k[j]
            if k.count(k[j])>a:
                a=k.count(k[j])
                b=k[j]
        v.append(b)
    return (v)

           
         


        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [['amaca','amaranto','rosso']], ['a','a','o'])
    counter_test_positivi += tester_fun(A_Ex9, [['osso','assolato','alto']], ['o','a','a'])
    counter_test_positivi += tester_fun(A_Ex9, [['stringa','a','bbbbcccc','dado']], ['a','a','b','d'])
    counter_test_positivi += tester_fun(A_Ex9, [['fosso','dosso','rosso','fosso']], ['o', 'o', 'o', 'o'])
    counter_test_positivi += tester_fun(A_Ex9, [['ciao mamma','ciao ']], ['a', ' '])

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
