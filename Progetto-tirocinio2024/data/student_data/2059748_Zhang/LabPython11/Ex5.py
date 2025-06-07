def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    f=open(file,encoding='UTF-8')
    p_a=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
    p_m=r'\b[A-Z]{2}[0-9]{5}\b'
    p_cm1=r'\b[A-Z0-9]{5}\b'
    p_cm2=r'\b[A-Z0-9]{6}\b'
    for l in f:
        r=l.strip()
        if re.match(p_a,r):
            x['auto']+=1
        elif re.match(p_m,r):
            x['moto']+=1
        elif re.match(p_cm1,r):
            x['ciclomotore1']+=1
        elif re.match(p_cm2,r):
            x['ciclomotore2']+=1
        else:
            x['errata']+=1

    return x
    
      
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
