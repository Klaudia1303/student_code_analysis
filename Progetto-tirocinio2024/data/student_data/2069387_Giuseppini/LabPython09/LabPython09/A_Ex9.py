def A_Ex9(fileName,squadra):
    f=open(fileName, encoding='utf-8')
    s=f.read()
    l=s.strip().split('\n')
    punti=0
    pos=0
    res=[]
    for riga in l:
        ll=riga.strip().split(',')
        if squadra in ll:
            pos=ll.index(squadra)
            if pos==0:
                if int(ll[2])>int(ll[3]):
                    punti=punti+3
                if int(ll[2])==int(ll[3]):
                    punti=punti+1
            if pos==1:
                if int(ll[3])>int(ll[2]):
                    punti=punti+3
                if int(ll[3])==int(ll[2]):
                    punti=punti+1
    
    return punti
        
    
    
           
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
