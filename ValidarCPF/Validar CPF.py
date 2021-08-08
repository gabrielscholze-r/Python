cpf = str(input("Digite o seu CPF:"))
x = cpf
if len(x)<11:
    print("CPF INVÁLIDO")
else:
    a = int(x[0]) * 10
    b = int(x[1]) * 9
    c = int(x[2]) * 8
    d = int(x[3]) * 7
    e = int(x[4]) * 6
    f = int(x[5]) * 5
    g = int(x[6]) * 4
    h = int(x[7]) * 3
    i = int(x[8]) * 2
    soma = a + b + c + d + e + f + g + h + i
    soma = (soma * 10) % 11
    if soma == int(x[9]):
        a = int(x[0]) * 11
        b = int(x[1]) * 10
        c = int(x[2]) * 9
        d = int(x[3]) * 8
        e = int(x[4]) * 7
        f = int(x[5]) * 6
        g = int(x[6]) * 5
        h = int(x[7]) * 4
        i = int(x[8]) * 3
        j = int(x[9]) * 2
        soma = a + b + c + d + e + f + g + h + i + j
        soma = (soma*10) % 11
        if soma == int(x[10]):
            print(f"o CPF {cpf} é válido")

        elif soma == 10 and x[10] == 0:
            print(f"o CPF {cpf} é válido")
        else:
            print(f"o CPF {cpf} não é válido")

    elif soma==10 and x[9]==0:
        if soma == x[9]:
            a = int(x[0]) * 11
            b = int(x[1]) * 10
            c = int(x[2]) * 9
            d = int(x[3]) * 8
            e = int(x[4]) * 7
            f = int(x[5]) * 6
            g = int(x[6]) * 5
            h = int(x[7]) * 4
            i = int(x[8]) * 3
            j = int(x[9]) * 2
            soma = a + b + c + d + e + f + g + h + i + j
            soma = (soma * 10) % 11
            if soma == x[10]:
                print(f"o CPF {cpf} é válido")

            elif soma == 10 and x[10] == 0:
                print(f"o CPF {cpf} é válido")
            else:
                print(f"o CPF {cpf} não é válido")
    else:
        print(f"o CPF {cpf} não é válido")
