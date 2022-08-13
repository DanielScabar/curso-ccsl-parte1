l = int(input("digite a largura: "))
a = int(input("digite a algura: "))

i = 1
j = 1

if l > 0 and a > 0:        
    while j <= a:
        while i<=l:
            print("#", end = "")
            i = i + 1
        print()
        j = j + 1
        i = 1
