def factor_primo_mas_grande( n: int )->int:
    totales = [2]

    if n != 2:
      i = 3
      while i <= n:
        totales.append(i)
        i += 2

      for num in totales:
        i = totales.index(num)+1
        while i < len(totales):
           if totales[i]%num == 0:
              totales.remove(totales[i])
           else:
              i += 1

    divisores = []
    for num in totales:
      while n%num == 0:
          n /= num
          if divisores.count(num) == 0:
             divisores.append(num)

      if n == 1:
          break
    
    return divisores[-1]
        
