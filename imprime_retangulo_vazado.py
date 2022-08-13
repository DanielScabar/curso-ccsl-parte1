l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i = 1
j = 1

if l > 0 and a > 0:    
    while j <= a:
        while i <= l:
            if j == 1 or j == a:
                print("#", end = "")
            else:
                if i == 1 or i == l:
                    print("#", end = "")
                else:
                    print(" ", end = "")
            i = i + 1
        print()
        j = j + 1
        i = 1
    
