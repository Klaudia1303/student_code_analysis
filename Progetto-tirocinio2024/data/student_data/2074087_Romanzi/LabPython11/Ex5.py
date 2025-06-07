def Ex5(file):
    
    import re
    f=open(file,encoding='UTF-8')
    ds={}
    d=[]
    d=f.readlines()
    f.close()
    f=open(file,encoding='UTF-8')
    ds['auto']=0
    ds['moto']=0
    ds['ciclomotore1']=0
    ds['ciclomotore2']=0
    pattern1=r'\b[A-Z][A-Z]\d\d\d[A-Z][A-Z]\b'
    pattern2=r'\b[A-Z][A-Z]\d\d\d\d\d\b'
    pattern3=r"\b[A-Z0-9]{5}\b"
    pattern4=r"\b[A-Z0-9]{6}\b"
    s=f.read()
    mn=re.findall(pattern1,s)
    ds['auto']=len(mn)
    mt=re.findall(pattern2,s)
    ds['moto']=len(mt)
    mr=re.findall(pattern3,s)
    ds['ciclomotore1']=len(mr)
    ms=re.findall(pattern4,s)
    ds['ciclomotore2']=len(ms)
    somma=0
    for i in ds:
        c=int(ds[i])
        somma=somma+c
    ds['errata']=int(len(d)-somma)
    f.close()   
    return ds


      
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
