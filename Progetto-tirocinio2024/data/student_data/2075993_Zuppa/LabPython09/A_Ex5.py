def A_Ex5(filename,oggetto):
    fin=open(filename,encoding='UTF-8')
    anni=fin.readline().strip().split(',')
    l=[]
    for i in fin:
        l.append(i.strip().split(','))
    fin.close()
    for i in range(len(l)):
        if oggetto in l[i]:
            ro=l[i]
    sM=int(ro[2])-int(ro[1])
    a=anni[2]
    for i in range(2,len(ro)-1):
        if sM<=int(ro[i+1])-int(ro[i]):
            sM=int(ro[i+1])-int(ro[i])
            a=anni[i+1]
    if sM<=0:
        return int(anni[1])
    else:
        return int(a)

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
