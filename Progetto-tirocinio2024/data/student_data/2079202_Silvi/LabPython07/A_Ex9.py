def A_Ex9(l):
    risultato=[]
    char=""
    for i in range(0, len(l)):
        
        for z in range(0, len(l[i])):
            if char=="":
                char=(l[i][z])
            else:
                if char!=l[i][z]:
                    if l[i].count(char)<=l[i].count((l[i][z])):
                        if l[i].count(char)==l[i].count((l[i][z])):
                            if ord(char)>ord((l[i][z])):
                                char=(l[i][z])
                        else:
                            char=(l[i][z])
        risultato.append(char)
        char=""
    return risultato
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
