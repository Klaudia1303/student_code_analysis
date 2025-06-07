def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    l=[]
    cmax=0
    anno=''
    for elem in f:
        l.append(elem.strip().split(","))
    for i in range(1,len(l)):
        if l[i][0]==oggetto:
            primo=int(l[i][1])
            for j in range(2,len(l[i])):
                if int(l[i][j])-primo>cmax or (int(l[i][j])-primo==cmax and l[0][j]>anno):
                    cmax=int(l[i][j])-primo
                    anno=l[0][j]
    if anno=='':
        return int(l[0][1])
    return int(anno)
                    
                
    

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
