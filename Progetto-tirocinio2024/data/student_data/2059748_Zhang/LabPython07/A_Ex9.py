def A_Ex9(l):
    l1=[]
    a=0
    b=str()
    for i in l:
        for j in range (len(i)):
            if j==len(i)-1:
                if i.count(i[j])>a:
                    a=i.count(i[j])
                    b=i[j]
                if i.count(i[j])==a:
                    if ord(i[j])<ord(b):
                        a=i.count(i[j])
                        b=i[j]
                l1.append(b)
                b=str()
                a=0
            else:
                if i.count(i[j])>a:
                    a=i.count(i[j])
                    b=i[j]
                if i.count(i[j])==a:
                    if ord(i[j])<ord(b):
                        a=i.count(i[j])
                        b=i[j]
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
