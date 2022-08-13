def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

n = int(input())
while n >= 0:
    print("Fatorial =", fatorial(n))
    n = int(input())
