def A_Ex5(fileName,oggetto):
    f=open(fileName,encoding='UTF-8')
    riga1=f.readline().strip().split(',')
    mas=0
    anno=riga1[1]
    for riga in f:
        riga=riga.strip().split(",")
        if oggetto in riga:
            for i in range(2,len(riga)):
                if (int(riga[i])-int(riga[i-1]))>=mas and (int(riga[i])-int(riga[i-1]))!=0:
                    mas=int(riga[i])-int(riga[i-1])
                    anno=riga1[i]
    f.close()
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
