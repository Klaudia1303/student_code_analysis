def A_Ex4(filename,anno):
    fin=open(filename,encoding='UTF-8')
    totalList=[]
    firstRow=fin.readline().strip().split(',')
    index=firstRow.index(str(anno))
    maxSold=0
    for line in fin:
        line=line.strip().split(',')
        sold=int(line[index])
        if sold>maxSold or sold==maxSold and ord(line[0][0])>ord(item[0]):
            maxSold=sold
            item=line[0]
    return item
            
    
        
    
        
    
        
        
        
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
