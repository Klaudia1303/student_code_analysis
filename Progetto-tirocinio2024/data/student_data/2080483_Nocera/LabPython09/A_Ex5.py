def A_Ex5(filename,oggetto):
    strn=[]
    crescitaeff=0
    fin=open(filename,encoding="UTF-8")
    f1=fin.readline()
    f1=f1.strip().split(",")
    print(f1)
    annoatt=int(f1[1])
    for riga in fin:
        r=riga.strip().split(",")
        strn.append(r)
    for elem in strn:
        if oggetto in elem:
            for i in range(2,len(elem)):
                crescita=int(elem[i])-int(elem[i-1])
                if crescita>=crescitaeff:
                    crescitaeff=crescita
                    annoatt=int(f1[i])
    fin.close()
    return annoatt
                    
            
    
        
        
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
