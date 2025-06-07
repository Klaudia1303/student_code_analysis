def Ex5(file):
    import re
    d={}
    f=open(file,encoding="UTF-8")
    
    pauto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
    pmoto=r'\b[A-Z]{2}[0-9]{5}\b'
    pciclo1=r'\b[A-Z0-9]{5}\b'
    pciclo2=r'\b[A-Z0-9]{6}\b'
    targaauto=0
    targamoto=0
    targaciclo1=0
    targaciclo2=0
    targaerrata=0
    
    for riga in f:
        auto=re.search(pauto,riga)
        moto=re.search(pmoto,riga)
        ciclo1=re.search(pciclo1,riga)
        ciclo2=re.search(pciclo2,riga)
        if auto:
            targaauto+=1
            d['auto']=targaauto
        elif moto:
            targamoto+=1
            d['moto']=targamoto
        elif ciclo1:
            targaciclo1+=1
            d['ciclomotore1']=targaciclo1
        elif ciclo2:
            targaciclo2+=1
            d['ciclomotore2']=targaciclo2
        else:
            targaerrata+=1
            d['errata']=targaerrata

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
