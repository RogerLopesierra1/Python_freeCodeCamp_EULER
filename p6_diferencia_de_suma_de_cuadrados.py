def diferencia_de_suma_de_cuadrados(n: int)->int:
    suma_cuadrada = 0
    suma = 0
    import math
    for i in range(1, n + 1):
        suma += i
        suma_cuadrada += math.pow(i,2)

    return int( math.pow(suma, 2) - suma_cuadrada )

print(diferencia_de_suma_de_cuadrados(100)) 