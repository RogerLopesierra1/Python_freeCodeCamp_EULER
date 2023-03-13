def primos_hasta_n(n:int):
    primos = [2]
    
    i = 3
    while i <= n:
        primos.append(i)
        i += 2

    for j in range(1,len(primos)):
        i = j+1
        while i < len(primos):
            if primos[i]%primos[j] == 0:
                primos.remove(primos[i])
            else:
                i += 1

    return primos

print( primos_hasta_n(140759) )