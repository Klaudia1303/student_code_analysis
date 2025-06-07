def A_Ex9(l):
    lfinale=[]
    for i in range(len(l)):
        counter=l[i].count(l[i][0])
        lettera=l[i][0]
        lfinale.append(lettera)
        for j in range(1,len(l[i])):
            if l[i].count(l[i][j])>counter:
                counter=l[i].count(l[i][j])
                lfinale.remove(lfinale[i])
                lettera=l[i][j]
                lfinale.append(lettera)
            if l[i].count(l[i][j])==counter:
                n=min(ord(l[i][j]),ord(lettera))
                x=chr(n)
                lfinale.remove(lfinale[i])
                lfinale.append(x)
    return lfinale
                
            
    
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
