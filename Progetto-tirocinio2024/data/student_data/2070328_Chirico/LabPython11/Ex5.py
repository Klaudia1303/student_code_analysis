def Ex5(file):
    x = open(file,'r',encoding = 'UTF-8')
    d = {}
    d['auto'] = 0
    d['moto'] = 0
    d['ciclomotore1'] = 0
    d['ciclomotore2'] = 0
    d['errata'] = 0

    auto = '[A-Z]{2}[0-9]{3}[A-Z]{2}'
    moto = '[A-Z]{2}[0-9]{5}'
    ciclomotore1 = '[A-Z0-9]'
    ciclomotore2 = '[A-Z0-9]'

    for i in x:
        i = i.strip()
        if re.findall(auto, i):
            d['auto'] = d['auto']+1
            
        elif re.findall(moto, i):
            d['moto'] = d['moto']+1
        
        elif len(re.findall(ciclomotore1, i)) == 5:
            if len(i) == 5:
                d['ciclomotore1'] = d['ciclomotore1']+1
            else:
                d['errata'] = d['errata']+1
            
        elif len(re.findall(ciclomotore2, i)) == 6:
            if len(i) == 6:
                d['ciclomotore2'] = d['ciclomotore2']+1
            else:
                d['errata'] = d['errata']+1

        else:
            d['errata'] = d['errata']+1
            

        

    x.close()   
    return d
        



    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
      
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
