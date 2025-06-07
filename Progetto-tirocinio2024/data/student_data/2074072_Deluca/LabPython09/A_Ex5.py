def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    s=f.read()
    ogg=oggetto
    sclear=s.replace("\n",";")
    l=s.strip().split("\n")
    l1=[]
    for elem in l:
        elem1=elem.split(";")
        l1.append(elem1)
    l2=[]
    for elem in l1:
        elem2=elem[0].split(",")
        l2.append(elem2)
    obj=""
    i=1
    n=1
    stesso=False
    while not stesso:
        if l2[i][0]==oggetto:
            obj=l2[i][0]
            n=i
            stesso=True
        i+=1
    nanni=len(l2[0])-1
    i1=1
    incr=0
    n1=1
    while i1<nanni:
        if int(l2[n][i1+1])-int(l2[n][i1])>incr:
                    incr=int(l2[n][i1+1])-int(l2[n][i1])
                    n1=i1+1
        elif int(l2[n][i1+1])-int(l2[n][i1])==incr:
            if l[0][i1+1]>l[0][i1]:
                n1=i1+1
        i1+=1
    anno=int(l2[0][n1])
    f.close()
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
