def maximo(a, b, c):
  if a > b and a > c:
    return a
  else:
    if b > a and b > c:
      return b
    else:
      return c
