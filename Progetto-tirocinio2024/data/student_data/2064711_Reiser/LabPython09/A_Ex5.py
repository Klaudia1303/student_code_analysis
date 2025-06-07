def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTf-8")
    l1=[]
    for riga in f:
        riga=riga.strip().split(',')
        l1.append(riga)
    a=0
    anno=0
    riga1=l1[0]
    for i in l1:
        if oggetto in i:
            for j in range(1,len(i)-1):
                if int(i[j])-int(i[j+1])<0 and int(i[j])-int(i[j+1])<=a:
                    a=int(i[j])-int(i[j+1])
                    anno=int(riga1[j+1])
                else:
                    continue
            if a==0:
                anno=int(riga1[1])
    return anno
    f.close()
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
