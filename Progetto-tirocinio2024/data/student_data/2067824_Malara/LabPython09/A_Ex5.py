def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding='UTF-8')
    
    strAnni=f.readline()              #lista anni
    strAnni=strAnni.strip().split(',')

    for riga in f:
        riga=riga.strip().split(',')
        if riga[0]==oggetto:    #sono nella riga dell'oggetto
            incrementomax=0
            indiceAnno=1
            i=1
            while i<len(riga)-1:
                incremento=int(riga[i+1])-int(riga[i])
                if incremento>=incrementomax:
                    incrementomax=incremento
                    indiceAnno=i+1        
                i+=1
    annomax=strAnni[indiceAnno]
    return int(annomax)

                                                     
            
            
      
    

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
