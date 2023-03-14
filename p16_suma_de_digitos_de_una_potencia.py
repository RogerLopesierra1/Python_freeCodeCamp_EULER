def suma_de_digitos_de_una_potencia(exp:int)->int:
    suma = 0
    numero = str( 2**exp )

    for i in range( len(numero) ):
        suma += int( numero[i] )

    return suma

print( suma_de_digitos_de_una_potencia( 1000 ) )