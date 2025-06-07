def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,encoding='UTF-8')
    d = {'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern = r'[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    m30 = "DHPS"
    m31 = "ACELMRT"
    m28 = "B"
    s = f.readline()
    l = []
    while s!="":
        if re.match(pattern,s):
            aa = re.match(pattern,s).group(1)
            mm = re.match(pattern,s).group(2)
            gg = int(re.match(pattern,s).group(3))
            x = ''
            if mm in m28:
                if(gg>=1 and gg<=28):
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=68):
                    gg -= 40
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                else:
                    l.append("Giorno errato")
            elif mm in m30:
                if(gg>=1 and gg<=30):
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=70):
                    gg -= 40
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                else:
                    l.append("Giorno errato")
            elif mm in m31:
                if(gg>=1 and gg<=31):
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
                    if int(aa) <= 20:
                        x += "20"+str(aa)
                        l.append(x)
                    else:
                        x += "19"+str(aa)
                        l.append(x)
                elif (gg>=41 and gg<=71):
                    gg -= 40
                    x += str(gg).zfill(2)+'/'+d.get(mm)+'/'
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
        s = f.readline()
    print(l)
    return l 
    
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
