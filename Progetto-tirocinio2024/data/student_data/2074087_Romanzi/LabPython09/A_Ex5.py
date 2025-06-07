def A_Ex5(fileName,oggetto):

    f=open(fileName,encoding="UTF-8")
    ls=[]
    d=0
    s=0
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls)):
        if ls[j][0]==oggetto:
            d=j
    h=int(ls[0][1])
    for z in range(1,len(ls[d])):
        if z!=len(ls[d])-1:
            if int(ls[d][z])<=int(ls[d][z+1]):
                s=int(ls[d][z+1])-int(ls[d][z])
                h=int(ls[0][z+1])
    f.close()
    return h

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
