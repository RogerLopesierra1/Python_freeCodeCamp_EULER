def multiplo_más_bajo(n: int):
    import primos_hasta_n as phn

    primos = phn.primos_hasta_n(n)

    numeros = []
    MCM = 1
    for i in range(2, n + 1):
        numeros.append(i)

    for pri in primos:
        es_dividido = True
        if numeros.count(1) != len(numeros):
            while es_dividido:
              es_dividido = False
              aparicion = 0
              for i in range( len(numeros) ):
                  if numeros[i] % pri == 0:
                      es_dividido = True
                      numeros[i] /= pri
                      if aparicion == 0:
                          MCM *= pri
                          aparicion += 1
        else:
            break             
        

    return MCM

print( multiplo_más_bajo(20) )