def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding='UTF-8')
    anno=f.readline().strip().split(',')
    sommavenditemax=0
    annomax=''
    for i in range(1,len(anno)):
        f=open(filename,encoding='UTF-8')
        anno=f.readline().strip().split(',')
        sommavendite=0
        for elem in f:
            elem=elem.strip().split(',')
            sommavendite+=int(elem[i])
        if sommavendite>=sommavenditemax:
            sommavenditemax=sommavendite
            annomax=int(anno[i])
        f.close()
    return annomax
        
            
        
        
 
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
