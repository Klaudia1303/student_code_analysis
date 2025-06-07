def Ex5(file):
    d={'auto':0,'moto':0,'ciclomotore1':0,'ciclomotore2':0,'errata':0}
    file=open(file, encoding='UTF-8')
    for riga in file:
        patternAuto= r'\b[A-Z][A-Z]\d\d\d[A-Z][A-Z]\b'
        patternMoto= r'\b[A-Z][A-Z]\d\d\d\d\d\b'
        pattern1cicl= r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
        pattern2cicl= r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
        if re.findall(patternAuto, riga, flags=0):
            if 'auto' in d:
                d['auto']+=1
        elif re.findall(patternMoto, riga, flags=0):
            if 'moto' in d:
                d['moto']+=1
        elif re.findall(pattern1cicl, riga, flags=0):
            if 'ciclomotore1' in d:
                d['ciclomotore1']+=1
        elif re.findall(pattern2cicl, riga, flags=0):
            if 'ciclomotore2' in d:
                d['ciclomotore2']+=1
        else:
            if 'errata' in d:
                d['errata']+=1
    file.close()
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
