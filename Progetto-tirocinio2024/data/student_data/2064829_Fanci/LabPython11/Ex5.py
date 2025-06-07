def Ex5(file):
    f=open(file,encoding="UTF-8")
    l=f.readlines()
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    pauto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
    pmoto=r'\b[A-Z]{2}[0-9]{5}\b'
    pcm1=r'\b[A-Z0-9]{5}\b'
    pcm2=r'\b[A-Z0-9]{6}\b'
    for i in l:
        if re.match(pauto,i):
            d['auto']+=1
        elif re.match(pmoto,i):
            d['moto']+=1
        elif re.match(pcm1,i):
            d['ciclomotore1']+=1
        elif re.match(pcm2,i):
            d['ciclomotore2']+=1
        else:
            d['errata']+=1
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
