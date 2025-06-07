def Ex5(file):

    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    auto = open(file,'r', encoding = 'UTF-8')

    targhe = {'auto': 0,'moto' : 0,'ciclomotore1' : 0,'ciclomotore2' : 0,'errata' : 0}

    for riga in auto:
          if(sum(1 for c in riga if c.isupper()) == 4
             and sum(1 for c in riga if c.isnumeric()) == 3):
              targhe['auto'] = targhe['auto'] + 1
          elif(sum(1 for c in riga if c.isupper()) == 2 and
               sum(1 for c in riga if c.isnumeric()) == 5):
              targhe['moto'] = targhe['moto'] + 1
          elif(sum(1 for c in riga if c.isalnum()) == 5):
                targhe['ciclomotore1'] = targhe['ciclomotore1'] + 1
          elif(sum(1 for c in riga if c.isalnum()) == 6):
               print(riga + ' è ciclomotore2 ')
               targhe['ciclomotore2'] = targhe['ciclomotore2'] + 1
          else:
              print(riga + ' è errata ')
              targhe['errata'] = targhe['errata'] + 1

    return targhe
               
        
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["targhe1.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 1})
    counter_test_positivi += tester_fun(Ex5, ["targhe2.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 2})
    counter_test_positivi += tester_fun(Ex5, ["targhe3.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 3})
    counter_test_positivi += tester_fun(Ex5, ["targhe4.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 4})
    counter_test_positivi += tester_fun(Ex5, ["targhe5.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 5})
    
    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
