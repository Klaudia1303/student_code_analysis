def A_Ex6(filename):
    l=[]
    smx=0
    somma=0
    j=0
    mx=0
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.split(',')
    for i in s:
        l.append(i)
    for j in range(len(l)-1):      
        for i in f:
            i=i.split(',')
            somma=somma+int(i[j+1])
        if somma>smx or somma==smx and int(l[j+1])>int(l[mx]):
            smx=somma
            mx=j+1
        somma=0
        f.close()
        f=open(filename,encoding='UTF-8')
        f.readline()
    return int(l[mx])
        
        
        
    
        
    
    
        
        
    
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
