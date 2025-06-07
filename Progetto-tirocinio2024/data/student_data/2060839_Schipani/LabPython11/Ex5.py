def Ex5(file):
    import re
    nA=0
    nM=0
    nCm1=0
    nCm2=0
    errata=0
    nTarghe=0
    d={}
    f=open(file,encoding='UTF-8')
    for riga in f:
        nTarghe+=1
        auto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
        a=re.search(auto,riga)
        if a:
            nA+=1
            d['auto']=nA
        moto=r'\b[A-Z]{2}[0-9]{5}\b'
        m=re.search(moto,riga)
        if m:
            nM+=1
            d['moto']=nM
        ciclomotore1=r'\b[A-Z0-9]{5}\b'
        ecm1=re.search(ciclomotore1,riga)
        if ecm1:
            nCm1+=1
            d['ciclomotore1']=nCm1
        ciclomotore2=r'\b[A-Z0-9]{6}\b'
        ecm2=re.search(ciclomotore2,riga)
        if ecm2:
            nCm2+=1
            d['ciclomotore2']=nCm2
    nTarghe+=1
    errata=(nTarghe-(nA+nM+nCm1+nCm2))-1
    d['errata']=errata
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
