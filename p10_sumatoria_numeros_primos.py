def sumatoria_numeros_primos(n:int)->int:
    import primos_hasta_n as phn
    import math
    primos = phn.primos_hasta_n(n-1)
    return int( math.fsum(primos) )

print( sumatoria_numeros_primos( 2000000 ) )