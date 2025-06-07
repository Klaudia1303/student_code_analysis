def A_Ex9(l):
    rep=[]
    c=0
    d=''
    for i in range(len(l)):
        for j in range(len(l[i])):
            r=l[i]
            b=r.count(r[j])
            a=r[j]
            if b>c:
                c==b
                d==a
            if b==c:
                if ord(a)<ord(d):
                    c==b
                    d==a
                elif ord(a)<ord(d):
                    c==c
                    d==a
        rep.append(d)
    return rep    

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
