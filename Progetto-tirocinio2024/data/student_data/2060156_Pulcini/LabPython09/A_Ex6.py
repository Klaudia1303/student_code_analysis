def A_Ex6(filename):
    file=open(filename,'r',encoding='UTF-8')
    anni=file.readline().strip().split(',')
    lista=[0 for i in range(len(anni))]
    for riga in file:
        riga=riga.strip().split(',')
        for i in range(len(lista)):
            if riga[i].isdecimal():
                lista[i]+=int(riga[i])
    lista.reverse()
    anni.reverse()
    return int(anni[lista.index(max(lista))])
            
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
