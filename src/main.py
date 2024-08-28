from frota import *

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)


if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input(' Nivel do tanque: '))
    cm = float(input(' consumo medio: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0,False, litros, cm)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input(' Nivel do tanque: '))
    cm = float(input(' consumo medio: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0 , False, litros, cm)


    while carro1.get_odometro() < 600 and carro2.get_odometro() < 600 and (carro1.get_tanque() > 0 or carro2.get_tanque() > 0):
        try:
            op = 0
            while op not in (1,2):
                op = int(input("Qual carro quer operar? [1-2]: "))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    print('\n')

try:
    carro1.desligar()
    carro2.desligar()
except:
    print('ERRO! Carro ja desligado!')

print(carro1)
print(carro2)

    if carro1.get_odometro() > carro2.get_odometro():
        print('\nCarro '+carro1.marca+' '+carro1.modelo+' ganhou!')
    else:
        print('\nCarro ' + carro2.marca + ' ' + carro2.modelo + ' ganhou!')


