def A_Ex5(filename,oggetto):
      f=open(filename,'r',encoding='UTF-8')
      rigadeglianni=f.readline().strip().split(',')
      increase=0
      maxann=0
      for riga in f.readlines():
            riga=riga.strip().split(',')
            ogg=riga[0]
            vendite=riga[1:]
            iincreased=False
            if ogg==oggetto:
                  for j in range(len(vendite)-1):
                        differ=int(vendite[j+1])-int(vendite[j])
                        if differ>increase:
                              maxann=int(rigadeglianni[j+2])
                              increase=differ
                              iincreased=True
                        elif differ==increase:
                              maxann = max(maxann,int(rigadeglianni[j+2]))
                              iincreased=True
                        elif differ<increase and not iincreased:
                              maxann=int(rigadeglianni[1])
      f.close()

      return maxann
                        
                        
    
    
    
    
"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
