def multiples_de_3_y_5(n: int)->int:
    suma = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            suma += i

    return suma