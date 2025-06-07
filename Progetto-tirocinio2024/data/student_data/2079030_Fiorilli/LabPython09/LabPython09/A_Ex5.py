def A_Ex5(filename,oggetto):
    file=open(filename, encoding="UTF-8")
    anni=file.readline()
    anni=anni.strip().split(',')
    riga=file.readline()
    anno=0
    while len(riga)>0:
        riga=riga.strip().split(',')
        if riga[0]==oggetto:
            deltamax=0
            pos=0
            for i in range (1,len(riga)-1):
                if int(riga[i+1])-int(riga[i])>=deltamax:
                    deltamax=int(riga[i+1])-int(riga[i])
                    pos=i
            anno=int(anni[pos+1])
            break       
        riga=file.readline()
    file.close()
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
