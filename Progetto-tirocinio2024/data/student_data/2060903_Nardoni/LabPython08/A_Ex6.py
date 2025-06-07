from tester import tester_fun

def A_Ex8(l,c,n):
        conta=0
        lista=l.copy()
        for i in range (len(l)):
                parola=l[i]
                for j in range (len(parola)):
                        if parola[j]==c:
                                conta+=1
                if conta>=n:
                        lista.remove(l[i])
                conta=0
        return lista

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, [['palla','casse','palo'],'a',2] ,['casse','palo'])
    counter_test_positivi += tester_fun(A_Ex8, [['palla','casse','palo'],'p',1] ,['casse'])
    counter_test_positivi += tester_fun(A_Ex8, [['pallone','casse','palla','pappa'],'p',2] ,['pallone','casse','palla'])
    counter_test_positivi += tester_fun(A_Ex8, [['pallone','casse','palla','pappa'],'a',1], [])
    counter_test_positivi += tester_fun(A_Ex8, [[],'a',1] , [])


    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
