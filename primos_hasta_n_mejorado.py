def primos_hasta_n_mejorado(n:int)->list:
    import math
    primos = [2]
    i = 3
    while i <= n:
        esPrimo = True
        for j in range(1, len(primos)):
            if math.gcd(primos[j],i) != 1:
                esPrimo = False
                break

        if esPrimo:
            primos.append(i)
        
        i += 2

    return primos

print( primos_hasta_n_mejorado(140759) )
