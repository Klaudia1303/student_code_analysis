def A_Ex5(filename,oggetto):
    f=open(filename, encoding='UTF-8')
    anno=f.readline()
    anno=anno.strip().split(',')
    f1=f.readlines()
    ind=[]
    c=0
    for i in range(len(f1)):
        f2=f1[i].strip().split(',')
        if(oggetto == f2[0]):
            f3=f2
    for i in range(1, len(f3)):
        if(int(f3[i])>=c):
            c=int(f3[i])
            ind=i
    f.close()
    return int(anno[ind])
        

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
