def A_Ex4(filename,anno):
    f=open(filename, encoding="UTF-8")
    s=f.readline()
    s1=f.readlines()
    ogg_pv=""
    max1=0
    s=s.strip().split(",")
    for i in range(len(s)):
        if(str(anno)==s[i]):
            ind=i
    for j in range(len(s1)):
        s2=s1[j].strip().split(",")
        if(int(s2[ind])>max1):
            max1=int(s2[ind])
            ogg_pv=s2[0]
    return(ogg_pv)
        
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
