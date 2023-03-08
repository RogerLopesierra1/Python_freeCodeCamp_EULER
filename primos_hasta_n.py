def primos_hasta_n(n:int):
    primos = [2]
    
    i = 3
    while i <= n:
        primos.append(i)
        i += 2

    for num in primos:
        i = primos.index(num)+1
        while i < len(primos):
            if primos[i]%num == 0:
                primos.remove(primos[i])
            else:
                i += 1

    return primos