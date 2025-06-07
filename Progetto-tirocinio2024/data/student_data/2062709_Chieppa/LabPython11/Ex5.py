def Ex5(file):
    f=open(file,encoding='UTF-8')
    s=f.readlines()
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}

    pattern_a=r'\b[A-Z]{2}\d{3}[A-Z]{2}\b'
    pattern_m=r'\b[A-Z]{2}\d{5}\b'
    pattern_c1=r'\b\w{5}\b'
    pattern_c2=r'\b\w{6}\b'
    
    for riga in s:
        auto=re.search(pattern_a,riga)
        moto=re.search(pattern_m,riga)
        ciclomotore1=re.search(pattern_c1,riga)
        ciclomotore2=re.search(pattern_c2,riga)
        if auto:
            d['auto']=d.get('auto')+1
        elif moto:
            d['moto']=d.get('moto')+1
        elif ciclomotore1:
            d['ciclomotore1']=d.get('ciclomotore1')+1
        elif ciclomotore2:
            d['ciclomotore2']=d.get('ciclomotore2')+1
        else:
            d['errata']=d.get('errata')+1

    f.close()
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
