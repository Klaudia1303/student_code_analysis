def A_Ex4(filename,anno):
    c=open(filename, encoding='UTF-8')
    F=c.readline()
    F2=c.readlines()
    F1=F.strip().split(',')
    v=0
    f=0
    t=''
    h=[]
    m=''
    for j in range (1,len(F1)):
        if int(F1[j])==anno:
            v=j
    for i in range(len(F2)):
        File=F2[i].strip().split(',')
        if int(File[v])>f:
            f=int(File[v])
            t=File[0]
            m=ord(File[0][0])
        if (File[v])==f:
            h.append(m)
            h.append(ord(File[0][0]))
            H=min(h)
            t=str(H)
    c.close()   
            
        
        
    
            
    
            
            
   
        

    

        
        
        
    
        
            
        



    
    return t




    
    
    
   

        
                
            
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
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
