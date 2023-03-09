def primo_en_posicion(posicion: int)->int:
    primos = [2]
    
    i = 3
    limite = i + 10000
    
    while len(primos) < posicion:
        while i <= limite:
            primos.append(i)
            i += 2
        
        for num in primos:
            i = primos.index(num)+1
            while i < len(primos):
                if primos[i]%num == 0:
                    primos.remove(primos[i])
                else:
                    i += 1

        i = primos[-1] + 2
        limite = i + 10000

    return primos[posicion - 1]

print( primo_en_posicion(10001) )