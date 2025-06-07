def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(filename,encoding="UTF-8")
    s_tot=[]
    s_0=[]

    max_elem='0'
    max_index=0

    for elem in fin:
        elem=elem.strip().split(',')
        s_tot.append(elem)

    fin.close()
    s_0=s_tot[0]
    anno_s=str(anno)
    indice=s_0.index(anno_s)

    for i in range (1,len(s_tot)):
        if int(s_tot[i][indice])>int(max_elem):
            max_elem=s_tot[i][indice]
            max_index=i
        elif int(s_tot[i][indice])==int(max_elem):
            if ord(s_tot[i][0][0])>ord(s_tot[max_index][0][0]):
                max_elem=s_tot[i][indice]
                max_index=i
            
    res=s_tot[max_index][0]
    
    return(res)    
     
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
