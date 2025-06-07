def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding='UTF-8')
    a=f.readline().strip().split(',')
    M=0
    I=1
    for line in f:
        s=line.strip().split(',')
        if oggetto in s:
            l=s
    for i in range(2,len(l)):
        if int(l[i])-int(l[i-1])>=M:
            M=int(l[i])-int(l[i-1])
            I=i
    f.close()
    res=int(a[I])
    return res
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
