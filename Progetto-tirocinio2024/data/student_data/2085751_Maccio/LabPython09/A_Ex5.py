def A_Ex5(filename,oggetto):
    file=open(filename, 'r', encoding='UTF-8')
    a=file.readline().strip().split(',')
    l=[]
    for riga in file:
        riga=riga.strip().split(',')
        if oggetto in riga:
            rig=riga
    for i in range(1, len(rig)):
        l.append(int(rig[i]) )
        mas=max(l)
    ind=l.index (mas)
    file.close ()
    return int(a[ind+1])
        
            
    
    

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
