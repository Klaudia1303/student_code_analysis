def A_Ex5(filename,oggetto):
    valore=0
    f=open(filename,encoding="UTF-8")
    for line in f:
        element=line.strip().split(",")
        if oggetto in element:
            for i in range (1,len(element)):
                vendite=element[i]
                vendite=int(vendite)
                if vendite>valore:
                    valore=vendite
            valore=str(valore)
            pos=element.index(valore)
            f.close()
            f=open(filename,encoding="UTF-8")
            riga=f.readline()
            lis=riga.strip().split(",")
            anno = lis[pos]
            anno=int(anno)
            return anno
            
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
