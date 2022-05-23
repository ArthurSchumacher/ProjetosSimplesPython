def inverterString(texto):
    return ''.join(reversed(texto))

def paraDecimal(n):
    expoente = 0
    decimal = 0
    digitos = inverterString(n)

    for i in digitos:
        decimal += int(i) * (2 ** expoente)
        expoente += 1
    
    return decimal

numero = input('Valor binario: ')

print('Valor em decimal: %d' % paraDecimal(numero))