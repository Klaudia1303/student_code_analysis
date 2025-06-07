def A_Ex9(l):
    l1=[]
    z=0
    y=200
    for i in range(len(l)):
        l2=l.copy()
        x=str(l2[i])
        for j in range(len(x)):
            a=x[j]
            b=x.count(a)
            if x.count(a)>z:
                y=ord(a)
                z=b
                c=a
            elif x.count(a)==z and ord(a)<y:
                y=ord(a)
                z=b
                c=a
        z=0
        y=200
        l1.append(c)
        c=''
    return l1



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
