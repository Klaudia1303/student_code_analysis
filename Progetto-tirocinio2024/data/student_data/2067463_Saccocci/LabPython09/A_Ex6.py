def A_Ex6(filename):
    f=open(filename,'r',encoding='UTF-8')
    primariga=f.readline().strip().split(',')
    (_,anni)=(primariga[0],primariga[1:])
    maxvendite=0
    maxvenditeanno=0
    righe=f.readlines()
    for i in range(len(anni)):
        venditeanno=0
        for riga in righe:
            riga=riga.strip().split(',')
            venditeanno+=int(riga[i+1])
        if venditeanno>maxvendite:
            maxvendite=venditeanno
            maxvenditeanno=int(anni[i])
        elif venditeanno==maxvendite:
            maxvenditeanno=max(maxvenditeanno,int(anni[i]))
    return maxvenditeanno
            
    
        
        
        
    
    
     
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
