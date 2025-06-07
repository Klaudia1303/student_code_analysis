def Ex5(file):
    import re
    f=open(file)
    testo=f.readlines()
    d={}
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    pa=r'[A-Z]{2}[0-9]{3}[A-Z]{2}'
    pm=r'[A-Z]{2}[0-9]{5}'
    p1=r'[A-Z0-9]{5}'
    p2=r'[A-Z0-9]{6}'
    for el in testo:
        el=el.strip()
        if len(el)==7 and re.search(pa,el,flags=0):
            d['auto']+=1
        elif len(el)==7 and re.search(pm,el,flags=0):
            d['moto']+=1
        elif len(el)==5 and re.search(p1,el,flags=0):
            d['ciclomotore1']+=1
        elif len(el)==6 and re.search(p2,el,flags=0):
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
