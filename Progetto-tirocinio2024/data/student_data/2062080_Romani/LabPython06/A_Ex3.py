for i in range(0, 11):
    for j in range(0, 11):
        
        t = i
        i_ottale = 0
        i = 1
        while t != 0:
            r = t % 8
            t //= 8
            i_ottale += r * x
            x *= 10

        t = j
        j_ottale = 0
        x = 1
        while t != 0:
            r = t % 8
            t //= 8
            j_ottale += r * x
            x *= 10

        p = i * j

        p_ottale = 0
        x = 1
        while p != 0:
            r = p % 8
            p //= 8
            p_ottale += r * x
            x *= 10

        print(i_ottale, 'x', j_ottale, '=', p_ottale)
