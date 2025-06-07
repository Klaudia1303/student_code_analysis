def A_Ex6(filename):
    f=open(filename, 'r', encoding='UTF-8')
    s=f.readline()
    l=s.strip().split(',')
    s1=f.readlines()
    l1=[]

    
    for riga in s1:
        riga=riga.strip().split(',')
        l1.append(riga)
    massimo=0
    for i in range(1,len(l)):
        somma=0
        for elem in l1:
            somma+=int(elem[i])
        if somma>=massimo:
            massimo=somma
            anno=int(l[i])
    f.close()
    return anno
            
        
            
        
                
            



    
 
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
