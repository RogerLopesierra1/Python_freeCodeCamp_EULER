def terna_pitagórica_especial(n:int)->int:
    resultado = 1
    encontrado = False
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i+j+k <= n:
                    if i*i + j*j == k*k and i+j+k == n:
                      resultado = i*j*k
                      encontrado = True
                      break
                else:
                    break
                
            if encontrado:
                break
        
        if encontrado:
            break
    
    return resultado

print( terna_pitagórica_especial(1000) )