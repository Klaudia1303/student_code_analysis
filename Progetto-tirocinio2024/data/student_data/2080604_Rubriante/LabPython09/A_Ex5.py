def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    cre=1
    ind=1
    anno=1
    for i in f:
        i=i.strip().split(",")
        if i[0]==oggetto:
            for j in range(len(i)):
                if i[j].isalpha()==False:
                    if j==len(i)-1:
                        break
                    else:
                        if int(i[j+1])-int(i[j])>=cre:
                            cre=int(i[j+1])-int(i[j])
                            ind=j+1
        else:
            continue
    f.close()
    f=open(filename,encoding="UTF-8")
    for i in f:
        i=i.strip().split(",")
        anno=int(i[ind])
        break
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
