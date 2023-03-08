def factor_primo_mas_grande( n: int )->int:
    primos = [2]

    if n != 2:
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

    divisores = []
    for num in primos:
      while n%num == 0:
          n /= num
          if divisores.count(num) == 0:
             divisores.append(num)

      if n == 1:
          break
    
    return divisores[-1]
        
