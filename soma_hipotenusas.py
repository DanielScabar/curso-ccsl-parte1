import math

def é_hipotenusa(n):
    i = 1
    j = 1
    while i <= n:
        while j <= n:
            if math.sqrt(i**2 + j**2) == n:
                print(i, " ", j, " ", n)
            j = j + 1
        i = i + 1
