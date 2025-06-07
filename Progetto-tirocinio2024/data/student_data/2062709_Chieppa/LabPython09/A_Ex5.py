def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    sv=[]
    colonna=0
    diff=0

    for elem in f:
        elem=elem.strip().split(",")
        sv.append(elem)
    

    for i in range(1,len(sv)):
        if sv[i][0]==oggetto:
            break
    riga=i
    anno=sv[0][riga]


    for j in range(1,len(sv[riga])-1):
        n1=int(sv[riga][j])
        n2=int(sv[riga][j+1])

        if int(n2-n1)>diff:
            diff=int(n2-n1)
            anno=sv[0][j+1]

        if int(n2-n1)==diff:
            anno=max(int(anno),int(sv[0][j+1]))






    f.close()        
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
