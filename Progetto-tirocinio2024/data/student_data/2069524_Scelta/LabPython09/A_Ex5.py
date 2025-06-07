def A_Ex5(filename,oggetto):
    file=open(filename,'r',encoding='UTF-8')
    anni=file.readline().strip().split(',')
    
    incr_max=0
    incr_annuo=0
    
    for line in file.readlines():
        line=line.strip().split(',')
        (ogg,vendite)=(line[0],line[1:])
        
        incremento=False
        
        if ogg==oggetto:
            for i in range(len(vendite)-1):
                differenza=int(vendite[i+1])-int(vendite[i])
                
                if differenza>incr_max:
                    incr_annuo=int(anni[i+2])
                    incr_max=differenza
                    incremento=True
                elif differenza==incr_max:
                    incr_annuo=max(incr_annuo,int(anni[i+2]))
                    incremento=True
                elif differenza<incr_max and not incremento:
                    incr_annuo=int(anni[1])
                
    return incr_annuo
        
    
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
