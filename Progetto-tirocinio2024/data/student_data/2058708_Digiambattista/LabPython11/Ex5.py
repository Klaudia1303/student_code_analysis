def Ex5(file):
    f = open(file)
    r = f.read()
    diff = len(r.split())
    diz = {"auto":0, "moto":0, "ciclomotore1":0, "ciclomotore2":0, "errata":0}
    pattern_auto = r"[A-Z]{2}\d{3}[A-Z]{2}"
    pattern_moto = r"[A-Z]{2}\d{5}"
    pattern_ciclomotore1 = r"[A-Z0-9][A-Z0-9]{3}[A-Z0-9]$"
    pattern_ciclomotore2 = r"[A-Z0-9][A-Z0-9]{4}[A-Z0-9]$"
    match_auto = re.findall(pattern_auto, r)
    match_moto = re.findall(pattern_moto, r)
    match_ciclomotore1 = re.findall(pattern_ciclomotore1, r)
    match_ciclomotore2 = re.findall(pattern_ciclomotore2, r)
    tot_len = len(match_auto) + len(match_moto) + len(match_ciclomotore1) + len(match_ciclomotore2)
    diz["auto"] += len(match_auto)
    diz["moto"] += len(match_moto)
    diz["ciclomotore1"] += len(match_ciclomotore1)
    diz["ciclomotore2"] += len(match_ciclomotore2)
    diz["errata"] += diff - tot_len 
    return diz 
    
      
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
