def suma_pares_fibonacci(n: int)->int:
  a = 1
  b = 1
  suma = 0

  while b <= n:
      aux = b
      b = a + b
      a = aux

      if b % 2 == 0:
          suma += b

  return suma