def A_Ex9(l):
    lt=[]
    lf=[]
    for i in l:
        i=sorted(i)
        mx=0
        for j in i:
            if(i.count(j)>mx):
                mx=i.count(j)
        c=1
        z=1
        if(len(i)==1):
            lf.append(i[0])
        while(z<len(i)):
            if(c==mx):
                lf.append(i[z-1])
                z=len(i)
                continue
            if (i[z]==i[z-1]):
                c+=1
            else:
                c=1
            z+=1
    return(lf)
                
    
    
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
