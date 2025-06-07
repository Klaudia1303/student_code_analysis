def A_Ex9(l):
    l2=[]
    s=''
    for i in range(len(l)):
        s=l[i]
        mas=0
        char=''
        for j in range(len(s)):
            if s.count(s[j])>mas:
                mas=s.count(s[j])
                char=s[j]
            elif mas==s.count(s[j]):
                if ord(char)<ord(s[j]):
                    mas=s.count(char)
                    char=char
                else:
                    mas=s.count(s[j])
                    char=s[j]
        l2.append(char)
    return l2
                
        

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
