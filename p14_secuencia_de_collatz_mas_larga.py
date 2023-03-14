def secuencia_de_collatz_mas_larga(limit:int)->int:
    mas_larga = []
    for num in range(2, limit):
        posible = [num]
        while True:
            if num != 1:
                if num % 2 == 0:
                    num = num/2
                else:
                    num = 3*num + 1
                
                posible.append(num)
                
            else:
                break
        
        if len( mas_larga ) < len( posible[0:len(posible)-1] ):
            mas_larga = posible[:][0:len(posible)-1]

    return mas_larga[0]

print(secuencia_de_collatz_mas_larga(14))
                
                
