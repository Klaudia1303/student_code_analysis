def A_Ex5(filename,oggetto):
    f=open(filename, encoding="UTF-8")
    riga1=f.readline()
    riga1=riga1.strip().split(',')
    righe=f.readlines()
    crescitaMax=0
    annoMax=int(riga1[1])
    for i in righe:
        i=i.strip().split(',')
        if i[0]==oggetto:
            for j in range(2, len(i)):
                if i[j]>i[j-1]:
                    crescita=(int(i[j])-int(i[j-1]))
                    if crescita>=crescitaMax:
                        crescitaMax=crescita
                        annoMax=int(riga1[j])
    f.close()
    return annoMax
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
