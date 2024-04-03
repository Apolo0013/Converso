from time import sleep

def km_para_milha():
    titulo('Km Pra Milha')
    kms = int(input('quantos km?: '))
    milha = kms * 0.6
    return (f'{kms} são em {milha}milha')


def Milha_Pra_Km():
    titulo('Milha Pra Km')
    milha = int(input('milhas: '))
    km = milha * 1.6
    return (f'{milha} milha são em {km :.0f}km')


def Celsius_pra_Fahrenheit():
    titulo('Celsius pra Fahrenheit')
    c = int(input('ºc: '))
    f = ((9*c)/5)+32
    return (f'ºf {c} são em ºf {int(f)}')


def Fahrenheit_pra_Celsius():
    titulo('Fahrenheit Pra Celsius')
    f = int(input('ºf: '))
    c = (f - 32) * 5/9
    return (f'ºf {f} são em ºc {int(c)}')


def Metros_para_Pés():
    titulo('Metros para Pés')
    metro = float(input('Metros: '))
    pes = metro * 3.28084
    return (f'{metro}m convetido para pés: {pes :.2f}pés')


def Pés_para_Metros():
    titulo('pès para Metros')
    pes =  float(input('pès: '))
    metro = pes * 0.3048
    return (f'{pes}pés é em metros: {metro :.2f}m')


def Quilogramas_para_Libras():
    titulo('Quilogramas para Libras')
    quilo = float(input('Quilos: '))
    libras = quilo * 2.20462
    return (f'{quilo}kg em libras: {libras :.2f}libras')


def Libras_para_Quilogramas():
    titulo('Libras para Quilogramas')
    libra = float(input('libras: '))
    quilo = libra * 0.453592
    return (f'{libra}libras em quilos(kg): {quilo}kg')


def titulo(msg):
    print('_' * 50)
    print(f'{msg :^45}')
    print('_' * 50)


# Programa Principal
while True:
    print('\033[1m{:^40}'.format(' ESCOLHA '))
    print('[ 1 ] - Km Pra Milha')
    print('[ 2 ] - Milha Pra Km')
    print('[ 3 ] - Celsius pra Fahrenheit')
    print('[ 4 ] - Fahrenheit Pra Celsius')
    print('[ 5 ] - Metros para Pés')
    print('[ 6 ] - Pés para Metros')
    print('[ 7 ] - Quilogramas para Libras')
    print('[ 8 ] - Libras para Quilogramas')
    while True:
        opcao = int(input('digite sua opcao: '))
        if opcao in (1,2,4,5,6,7,8,9,3):
            break
    sleep(5)
    if opcao == 1:
        print(km_para_milha())
    elif opcao == 2:
        print(Milha_Pra_Km())
    elif opcao == 3:
        print(Celsius_pra_Fahrenheit())
    elif opcao == 4:
        print(Fahrenheit_pra_Celsius)
    elif opcao == 5:
        print(Metros_para_Pés())
    elif opcao ==  6:
        print(Pés_para_Metros())
    elif opcao == 7:
        print(Quilogramas_para_Libras())
    elif opcao == 8:
        print(Libras_para_Quilogramas())
    print('=' * 50)
    sleep(3)
    if opcao == 9:
        break