for i in range(1,9):
    for j in range(1,9):
        h = i*j
        q1 = h//8
        r = h%8
        rpl = str(r)

        if q1 == 0:
            baseotto = r
        else:
            while q1 != 0:
                q = q1//8
                r = q1%8
                rpl = rpl+str(r)
                v = rpl[::-1]
                q1 = q
                baseotto = int(v)
        if (baseotto < 10):
            print("0", i, "x", "0", j, "=", "0", baseotto, sep='')
        else:
            print("0", i, "x", "0", j, "=", baseotto, sep='')
