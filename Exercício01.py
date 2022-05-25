'''Exercicio 1: Faça um programa que tenha uma função chamada amplitude. A função deve receber uma lista e
imprimir a amplitude.
Crie também um código para testar sua função'''

def amplitude(lista):
     return lista

lista = [1,2,3,4,5,6]
print(amplitude(lista[1]))


'''exercicio 2: Faça uma função que receba uma string e imprima esta string na forma vertical
              Por exemplo: se receber python, deve imprimir
              p
              y
              t
              h
              o
              n
Dica: uma string do python funciona como uma lista!
Crie também um código para testar sua função '''


def python_str(lista):
    for i, str in enumerate(var_str):
        print(str)

    return lista
var_str = str(input('Digite alguma coisa: ')).strip()
python_str(var_str)


''' Exercício 3:   Crie um programa que leia o peso de uma carga em números inteiros. Se o peso for até 10 kg, informe
que o valor será de R$ 50,00. Entre 11 e 20 kg, informe que o valor será de R$ 80. Se for maior que 20
informe que o transporte não é aceito. Teste vários pesos.'''

from time import sleep

while True:
    try:
        carga = int(input('Digite o peso da carga: ').strip())
    except ValueError:
        print("Valor incorreto, digite novamente")
        carga = int(input('Digite o peso da carga: ').strip())
    # if carga.isnumeric() == False:
    if carga <= 10: 
        print("Processando informação...")
        sleep(2)
        print("O valor será de R$ 50,00")   
    elif carga >= 11 and carga <= 20:
        print("Processando informação...")
        sleep(2)
        print("O valor será de R$ 80,00")
    else:
        print("O transporte não é aceito")
    resp = str(input("Quer continuar? S/N: "))
    if resp in 'Nn':
        print('Ok..')
        sleep(2)
        print("Finalizando o programa..")
        break