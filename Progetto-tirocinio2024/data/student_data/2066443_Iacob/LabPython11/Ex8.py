def Ex8(file):
    o = open(file,encoding="UTF-8")
    diz = {'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern = r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    m_30 = "DHPS"
    m_31 = "ACELMRT"
    m_28 = "B"
    r = o.readline()
    l = []
    while r!="":
        if re.match(pattern, r):
            aa = re.match(pattern, r).group(1)
            mm = re.match(pattern, r).group(2)
            gg = int(re.match(pattern, r).group(3))
            x = ''
            if mm in m_28:
                if(gg>=1 and gg<=28):
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=68):
                    gg = gg-40
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                else:
                    l.append("Giorno errato")
            elif mm in m_30:
                if(gg>=1 and gg<=30):
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=70):
                    gg = gg-40
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                else:
                    l.append("Giorno errato")
            elif mm in m_31:
                if(gg>=1 and gg<=31):
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=71):
                    gg -= 40
                    x += str(gg).zfill(2)+'/'+diz.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                else:
                    l.append("Giorno errato")
            else: 
                l.append("Mese errato")
        else:
            l.append("Codice errato")
        r = o.readline()
    return l
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
