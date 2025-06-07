def Ex5(file):
    file = open(file,encoding='UTF-8')
    l = []
    for elem in file:
        elem = elem.strip()
        l.append(elem)
    d = {}
    d['auto'] = 0
    d['moto'] = 0
    d['ciclomotore1'] = 0
    d['ciclomotore2'] = 0
    d['errata'] = 0
    for elem in l :
        if re.match(r'[A-Z]{2}\d{3}[A-Z]{2}',elem, flags= 0) != None:
            d['auto'] = d['auto']+1
        elif re.match(r'[A-Z]{2}\d{5}',elem, flags= 0) != None:
            d['moto'] = d['moto'] +1
        elif re.match(r'\b\w{5}\b',elem, flags= 0) != None:
            d['ciclomotore1'] = d['ciclomotore1'] +1
        elif re.match(r'\b\w{6}\b',elem, flags= 0) != None:
            d['ciclomotore2'] = d['ciclomotore2'] + 1
        else:
            d['errata']= d['errata'] +1
    return(d)
      
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
