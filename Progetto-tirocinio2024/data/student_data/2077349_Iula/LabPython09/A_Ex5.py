def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding="UTF-8")
    lfile=[]
    anno="nessun anno"
    for el in f:
        l=el.split(',')
        for c in range(len(l)):
            l[c]=l[c].strip()
        lfile.append(l)
    for i in range(len(lfile)):
        for j in range(len(lfile[i])):
            if lfile[i][j]==oggetto:
                diff=0
                anno=int(lfile[0][1])
                for k in range(2,len(lfile[i])):
                    if int(lfile[i][k])-int(lfile[i][k-1])>=diff:
                            diff=int(lfile[i][k])-int(lfile[i][k-1])
                            anno=int(lfile[0][k])
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
