def A_Ex5(filename,oggetto):

    f=open(filename, encoding='UTF_8')
    for riga in f:
        l=f.readline() .strip() .split(',')
        if oggetto in l:
            break
    l1=[]
    for i in range (l,len(l)):
        l1.append(l[i])

    nmax=max(l1)
    pos=l1.index(nmax)
    f.close()
    l=readline() .strip() .split(',')
    f.close()

    return int(l[pos+1])







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
