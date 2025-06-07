def Ex5(file):
    import re
    f=open(file, encoding='UTF-8')
    t=f.read()
    d=dict()
    pauto=r'[A-Z]{2} ?[0-9]{3} ?[A-Z]{2}'
    pmoto=r'[A-Z]{2} ?[0-9]{5}'
    pcicl1=r'[A-Z0-9]{5}'
    pcicl2=r'[A-z0-9]{6}'
    auto=re.findall(pauto, t)
    moto=re.findall(pmoto, t)
    cicl1=re.findall(pcicl1, t)
    cicl2=re.findall(pcicl2,t)
    nauto= len(auto)
    d['auto']= nauto
    d['moto']= len(moto)
    d['ciclomotore1']= len(cicl1)
    d['ciclomotore2']= len(cicl2)
    tt=len(t.split('\n'))
    if (tt-(len(auto)+len(moto)+len(cicl1)+len(cicl2)))>0:
        d['errata']=tt-(len(auto)+len(moto)+len(cicl1)+len(cicl2))
    else:
        d['errata']=0
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
