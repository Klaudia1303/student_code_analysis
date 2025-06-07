def A_Ex5(filename,oggetto):
    f=open(filename, encoding='UTF-8')
    pRiga=f.readline()
    anno=pRiga.strip().split(',')
    riga=f.readlines()
    for x in riga:
        if oggetto in x.strip().split(','):
            i=x.strip().split(',')
    massimo=0
    for k in range(1, len(i)-1):
        if int(i[k+1])-int(i[k])>=massimo:
            massimo=int(i[k+1])-int(i[k])
            anno1=int(anno[k+1])
    if massimo==0 and anno!=[]:
        anno1=int(anno[1])
    f.close()
    return anno1
        
    
    
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
