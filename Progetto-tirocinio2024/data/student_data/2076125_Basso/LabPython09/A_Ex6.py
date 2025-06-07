def A_Ex6(filename):
    f=open(filename)
    riga=f.readline()
    anni=riga.strip().split(',')
    m=0

    for i in range(1,len(anni)):
        s=0
        riga=f.readline()
        dati=riga.strip().split(',')
        while len(riga)>0:
            s=s+int(dati[i])
            print(dati[i])
            riga=f.readline()
            dati=riga.strip().split(',')
        f.close()
        print(s)
            
        if s>=m:
            m=s
            anno=anni[i]

        f=open(filename)
        riga=f.readline()    
    f.close()
    return int(anno)
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
