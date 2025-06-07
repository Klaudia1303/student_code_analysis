def Ex5(file):
    f=open(file, encoding='UTF-8')
    testo=f.read()
    elementi=testo.strip().split('\n')
    f.close()
    d={}
    aut=r'\b[A-Z]{2}\d{3}[A-Z]{2}\b'
    mot=r'\b[A-Z]{2}\d{5}\b'
    ciclomotor1=r'\b[A-Z0-9]{5}\b'
    ciclomotor2=r'\b[A-Z0-9]{6}\b'
    d['auto']=len(re.findall(aut, testo))
    d['moto']=len(re.findall(mot, testo))
    d['ciclomotore1']=len(re.findall(ciclomotor1, testo))
    d['ciclomotore2']=len(re.findall(ciclomotor2, testo))
    d['errata']=len(elementi)-d['auto']-d['moto']-d['ciclomotore1']-d['ciclomotore2']
    return d
        
      
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
