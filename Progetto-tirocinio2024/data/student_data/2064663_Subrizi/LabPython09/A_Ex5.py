def A_Ex5(filename,oggetto):
    f=open(filename, 'r', encoding='UTF-8')
    s=f.readline()
    s1=s.strip().split(',')

    massimo=-1
    anno=1
    for riga in f:
        riga=riga.strip().split(',')
        if riga[0]==oggetto:
            print(riga)
            for i in range(1,len(riga)-1):
                if int(riga[i+1])-int(riga[i])>=massimo:
                    massimo=int(riga[i+1])-int(riga[i])
                    anno=i+1
                else:
                    continue
    f.close()
    return int(s1[anno])
                    
        
            
        


    
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
