def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding="UTF-8")
    p=[]
    s=f.readlines()
    for j in range(len(s)):
        x=s[j].strip().split(',')
        for i in range(1):
            if x[0]==oggetto:
                p=x.copy()
    b=0
    for k in range(1,len(p)):
        if int(str(p[k]))>=b:
            b=int(str(p[k]))
            m=k
    g=s[0].strip().split(',')
    z=int(g[m])
    f.close()
    return z



    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
