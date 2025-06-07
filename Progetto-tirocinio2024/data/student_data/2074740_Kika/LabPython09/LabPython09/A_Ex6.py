def A_Ex6(filename):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    l=[]
    for t in f:
        t=t.strip().split(',')
        l.append(t)
    #l=lista con tutti gli oggetti venduti
    Max=0
    AnnoProfiquo=0
    pos=0
    for anno in range(len(l[1])-1):
        count=0
        pos+=1
        for listina in l:
            count+=int(listina[pos])
        if count>=Max:
            Max=count
            AnnoProfiquo=pos
    f.close()
    s=s.strip().split(',')
    return int(s[AnnoProfiquo])
        
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
