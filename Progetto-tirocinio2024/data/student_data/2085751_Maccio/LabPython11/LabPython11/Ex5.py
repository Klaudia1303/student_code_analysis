def Ex5(file):
    fil=open(file,'r',encoding='UTF-8')
    file=fil.readlines()
    d={}
    auto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
    moto=r'\b[A-Z]{2}[0-9]{5}\b'
    ciclomotore1=r'\b[A-Z0-9]{5}\b'
    ciclomotore2=r'\b[A-Z0-9]{6}\b'
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    for targa in file:
        if re.search(auto,targa):
            d['auto']+=1
        elif re.search(moto,targa):
            d['moto']+=1
        elif re.search(ciclomotore1,targa):
            d['ciclomotore1']+=1
        elif re.search(ciclomotore2,targa):
            d['ciclomotore2']+=1
        else:
            d['errata']+=1
    return d

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
