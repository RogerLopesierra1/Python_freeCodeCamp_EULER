def mayor_producto_de_palíndromos(n: int)->int:
    limite_final =  '1'+n*'00' 
    limite_inicial =  int( limite_final[0: len(limite_final) - 1 ] )
    limite_final = int( limite_final )
    mitad = int(  len( str(limite_inicial) )/2)

    import primos_hasta_n as phn
    primos = phn.primos_hasta_n(limite_final)   

    mayor = -1
    for i in range( limite_inicial, limite_final ):
        parte_1 = str( i )[0:mitad]
        parte_2 = str( i )[mitad : mitad*2]
        inverso = ''

        aux = i

        for j in range( mitad ):
            inverso += parte_2[mitad - 1 - j]

        if parte_1 == inverso:
            if primos.count(i) == 0:
                divisores = []
                for num in primos:
                    while i%num == 0:
                        i /= num
                        divisores.append(num)

                        if i == 1:
                            break

                    if i == 1:
                        break
                v1 = 1
                v2 = 1
                for valor in divisores:
                    if len(str(v1*valor)) <= 2:
                        v1 *= valor
                    elif len(str(v2*valor)) <= 2:
                        v2 *= valor
                    else:
                        break
                
                if v1*v2 == aux:
                    mayor = aux                   
                      

    return mayor
        


print( mayor_producto_de_palíndromos(2) )