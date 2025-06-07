def Ex5(file):
    import re
    
    f = open(file,'r',encoding= 'UTF-8')

    regex = {'auto': r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b','moto' : r'\b[A-Z]{2}[0-9]{5}\b',

    'ciclomotore1':r'\b[A-Z0-9]{5}\b','ciclomotore2': r'\b[A-Z0-9]{6}\b'}
    #print(regex,type(regex))

   
    i = 0
    risultato = dict()
    for targa in f:
        targa = targa.strip()
        #print(targa)

        for veicolo in regex:
            m = re.search(regex[veicolo],targa)
            if m:
                i = 1
                risultato[veicolo] = risultato.get(veicolo,0) + 1
                break

        if i == 0:
            risultato['errata'] = risultato.get('errata',0) + 1

        i = 0
    
        

    return risultato

        

        
        

    












      
      
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
