def Ex5(file):
    import re
    d={}
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    f=open(file,'r',encoding='UTF-8')
    for riga in f:
        Auto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
        Moto=r'\b[A-Z]{2}[0-9]{5}\b'
        Ciclo1=r'\b[A-Z0-9]{5}\b'
        Ciclo2=r'\b[A-Z0-9]{6}\b'
        a=re.search(Auto,riga)
        m=re.search(Moto,riga)
        c1=re.search(Ciclo1,riga)
        c2=re.search(Ciclo2,riga)
        if a:
            d['auto']+=1
        elif m:
            d['moto']+=1
        elif c1:
            d['ciclomotore1']+=1
        elif c2:
            d['ciclomotore2']+=1
        else:
            d['errata']+=1
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
