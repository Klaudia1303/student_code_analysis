def Ex5(file):
    f=open(file)
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    p_a=r'[A-Z][A-Z][0-9][0-9][0-9][A-Z][A-Z]\b'
    p_m=r'[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]\b'
    p_c1=r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
    p_c2=r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
    for riga in f:
        if len(re.findall(p_a,riga))==1:
            d['auto']+=1
            
        elif len(re.findall(p_m,riga))==1:
            d['moto']+=1
            
        elif len(re.findall(p_c2,riga))==1:
            d['ciclomotore2']+=1
            
        elif len(re.findall(p_c1,riga))==1:
            d['ciclomotore1']+=1
            
        else:
            d['errata']+=1
        print(d)
    f.close()
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
