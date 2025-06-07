def A_Ex9(l):
    l1=[]
    max1=0
    max_p=""
    parola=""
    for i in range(len(l)):
        parola=l[i]
        for j in range(len(parola)):
            if (parola.count(parola[j])>max1):
                max1=parola.count(parola[j])
                max_p=parola[j]
            elif(parola.count(parola[j])==max1 and ord(parola[j])<ord(max_p)):
                max1=parola.count(parola[j])
                max_p=parola[j]
        l1.append(max_p)
        max1=0
        max_p=""
    return(l1)
                
        
  

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
