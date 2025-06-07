def Ex5(file):
    d={}
    numRighe=0
    k=0
    f=open(file,encoding='UTF-8')
    CODauto=r'\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b'
    CODmoto=r'\b[A-Z]{2}[0-9]{5}\b'
    CODciclomotore2=r'\b\w{6}\b'
    CODciclomotore1=r'\b\w{5}\b'
    pattern=[CODauto,CODmoto,CODciclomotore2,CODciclomotore1]
    mezzi=['auto','moto','ciclomotore2','ciclomotore1','errata']
    for j in mezzi:
        d[j]=0
    for riga in f:
        numRighe+=1
        for i in range(len(pattern)):
            if k==numRighe:
                break
            regex=pattern[i]
            m=re.search(regex,riga)
            if m!=None:
                d[mezzi[i]]+=1
                k+=1
            if m==None and i==3:
                d['errata']+=1
                k+=1
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
