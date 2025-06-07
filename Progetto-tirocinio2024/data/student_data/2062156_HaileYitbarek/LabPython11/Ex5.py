def Ex5(file):
    d=dict()
    l=['auto', 'moto', 'ciclomotore1', 'ciclomotore2', 'errata']
    h1=0
    h2=0
    h3=0
    h4=0
    p1=r'\b([A-Z])([A-Z])([0-9])([0-9])([0-9])([A-Z])([A-Z])\b'
    p2=r'\b([A-Z])([A-Z])([0-9])([0-9])([0-9])([0-9])([0-9])\b'
    p3=r'\b([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])\b'
    p4=r'\b([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])([A-Z0-9])\b'
    p5=0
    f=open(file,encoding='UTF-8')
    for riga in f:
        riga=riga.strip()
        if re.findall(p1,riga):
            h1+=1
        elif re.findall(p2,riga):
            h2+=1
        elif re.findall(p3,riga):
            h3+=1
        elif re.findall(p4,riga):
            h4+=1
        else:
            p5+=1
    k=[h1,h2,h3,h4,p5] 
    for i in range(len(l)):
        d[l[i]]=k[i]
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
