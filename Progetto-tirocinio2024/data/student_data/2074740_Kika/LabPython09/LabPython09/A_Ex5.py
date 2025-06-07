def A_Ex5(filename,oggetto):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding='UTF-8')
    for riga in f:
        riga=riga.strip().split(',')
        riga=list(riga)
        if riga.count(oggetto)==1:
            Max=0
            pos=1
            for i in range(1,len(riga)):
                if i+1<len(riga) and int(riga[i+1])-int(riga[i])>=Max:
                    Max=int(riga[i+1])-int(riga[i])
                    pos=i+1
    f.close()
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip().split(',')
    s=list(s)
    anno=s[pos]
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
