def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    s=open(filename,encoding='UTF-8').readlines()
    for elem in s:
        if elem[:elem.find(',')]==oggetto:
            t=elem.strip().split(',')
            break
        
    d=s[0].strip().split(',')     
    imax=0
    anno=d[1]
    for i in range(1,len(t)-1):
        if int(t[i+1])-int(t[i])>=imax:
            imax=int(t[i+1])-int(t[i])
            anno=d[i+1]
    return int(anno)
    
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
