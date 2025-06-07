def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding='UTF-8')
    anni=f.readline().strip().split(',')
    maxi=0
    maxanni=0
    for line in f.readlines():
        line=line.strip().split(',')
        (ogg,vendite)=(line[0],line[1:])
        crescita=False
        if ogg==oggetto:
            for i in range(len(vendite)-1):
                differenza=int(vendite[i+1])-int(vendite[i])
                if differenza>maxi:
                    maxanni=int(anni[i+2])
                    maxi=differenza
                    crescita=True
                elif differenza==maxi:
                    maxanni=max(maxanni,int(anni[i+2]))
                    crescita=True
                elif differenza<maxi and not crescita:
                    maxanni=int(anni[1])
    return maxanni
        
            
        
    
        
        
    
        
        
        
        
        
    
    
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
