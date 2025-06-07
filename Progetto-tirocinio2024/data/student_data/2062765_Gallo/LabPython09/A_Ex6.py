def A_Ex6(filename):
    f=open(filename,"r",encoding="UTF-8")
    riga=f.readline()
    anni=riga.strip().split(",")
    a=0
    massimo=0
    acc=0
    while len(riga)>0:
        riga=f.readline()
        if len(riga)>0:
            a+=1
    f.close()
    f2=open(filename,"r",encoding="UTF-8")
    riga2=f2.readline()
    sos=riga2.strip().split(",")
    for i in range(1,len(sos)):
        for j in range(a):
            riga2=f2.readline()
            dati=riga2.strip().split(",")
            acc+=int(dati[i])
        if acc>massimo:
            massimo=acc
            x=i
        acc=0
        f2=open(filename,"r",encoding="UTF-8")
        riga2=f2.readline()
    return int(anni[x])
                
            
        
        
            
 
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
