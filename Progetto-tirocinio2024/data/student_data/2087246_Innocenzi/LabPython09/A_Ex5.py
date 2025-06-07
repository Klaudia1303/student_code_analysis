def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8") 
    s=f.readline() 
    l=s.strip().split(',') 
    anni=[]
    ris=0
    for i in range(1,len(l)): 
        anni.append(l[i]) 
    vendite = [0 for i in range(len(l))] 
    for i in f: 
        l=i.strip().split(',') 
        for j in range(1,len(l)): 
            vendite[j-1] += int(l[j]) 
    f.close()
    ris=int(anni[vendite.index(max(vendite))]) 
    return ris





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
