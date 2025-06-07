def A_Ex5(filename,oggetto):
    fin=open(filename,'r',encoding='UTF-8')
    l=[]
    for i in fin:
        i=i.strip().split(',')
        l.append(i)
    anno=int(l[0][1])
    k=0
    l2=[]
    for i in l:
        if oggetto in i:
            l2=i
    for j in range(2,len(l2)):
        if int(l2[j])-int(l2[j-1])>=k:
            anno=int(l[0][j])
            k=int(l2[j])-int(l2[j-1])
    fin.close
    return anno
    

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
