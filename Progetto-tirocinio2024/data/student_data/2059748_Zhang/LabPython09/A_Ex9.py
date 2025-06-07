t1w=-1
tie=0
t2w=1

def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x=open(fileName,encoding='UTF-8')
    x.readline() 
    b={ }
    for l in x:
        r=l.strip().split(',')
        m=g(r)
        u(b,r,m)

    return s(b,squadra)

def s(b:dict,k:str)->int:
    if k in b:
        return b[k]
    return 0

def u(b:dict,r:list,m:int)->None:
    t1=r[0]
    t2=r[1]
    if not t1 in b:
        b[t1]=0
    if not t2 in b:
        b[t2]=0
    if m==tie:
        b[t1]+=1
        b[t2]+=1
    elif m==t1w:
        b[t1]+=3
    else:
        b[t2]+=3

def g(r: list)->int:
    t1s=r[2]
    t2s=r[3]
    if t1s==t2s:
        return tie
    elif t1s>t2s:
        return t1w
    else:
        return t2w

    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
