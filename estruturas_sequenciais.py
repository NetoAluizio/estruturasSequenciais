#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Estrutura sequencial:

# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

saudacao = 'Alo'
local = 'Mundo'
print(saudacao, local)

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input('Digite um número: ')
print('O número informado foi', numero)

# Faça um Programa que peça dois números e imprima a soma.

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
soma = (int(num1) + int(num2))
print(soma)

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.


nota1 = input('digite a nota do 1º bimestre: ')
nota2 = input('digite a nota do 2º bimestre: ')
nota3 = input('digite a nota do 3º bimestre: ')
nota4 = input('digite a nota do 4º bimestre: ')
media_final = ((int(nota1) + int(nota2) + int(nota3) + int(nota4))/4)
print(int(media_final))


# Faça um Programa que converta metros para centímetros.

metros = int(input('Valor, em metros, a ser convetido: '))
centimetros = int(metros * 100)
print(metros, 'metro(s) equivalem a', centimetros, 'centímetro(s).')

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

while True:
    r = input('Qual o valor do raio do círculo?')
    if not r.isnumeric():
        print('Insira só o valor, sem unidades de medida, pontos ou vírgulas!')
        continue
    else:
        r = float(r)
        area = (3.14 * r * r)
        circ = (3.14 * r * 2)
        print(f'Um círculo de raio {r} tem área no valor de {area:.2f} e circunferência no valor de {circ:.2f}.')
        break


# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    l = input('Qual o valor do lado do quadrado?')
    if not l.isnumeric():
        print('Insira só o valor, sem unidades de medida, pontos ou vírgulas!')
        continue
    else:
        l = int(l)
        areaQ = (l * l)
        areaQDobro = areaQ * 2
        print(f'O dobro da área de um quadrado de lado {l} tem valor igual a {areaQDobro}.')
        break

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

ganho = int(input('Informe o valor que você recebe por hora: '))
horas = int(input('Informe quantas horas vc trabalha ao mês: '))
salario = ganho * horas
print(f'Neste mês, seu salário foino valor de R$ {salario:.2f}')

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = ((F-32) */1.8).

while True:
    f = input('Informe a temperatura em Fahrenheit: ')
    if f.replace('.',  '', 1).isdigit():
        f = float(f)
        c = ((f-32)/1.8)
        print(f'A temperatura de {f} graus Fahrenheit equivale(m) a {c:.2f} graus Celsius.')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

while True:                                                 # loço retorna sempre que não é uma entrada válida
    c = input('Informe a temperatura em Celsius: ')
    if c.replace('.', '', 1).replace('-', '', 1).isdigit(): # verifica entrada de dados, inclusive floats e negativos
        c = float(c)                                        # converte entrada em float
        f = ((c*1.8) + 32)
        print(f'A temperatura de {c} graus Celsius equivale(m) a {f:.2f} graus Fahrenheit.')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo.
# b -  a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.


while True:
    num_int_1 = input('Informe um número inteiro: ')
    if num_int_1.replace('-', '', 1).isdigit():
        num_int_1 = float(num_int_1)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
        
while True:
    num_int_2 = input('Informe outro número inteiro: ')
    if num_int_2.replace('-', '', 1).isdigit():
        num_int_2 = float(num_int_2)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
while True:
    num_real = input('Informe um número real: ')
    if num_real.replace('.', '', 1).replace('-', '', 1).isdigit():
        num_real = float(num_real)
        a = float((num_int_1*2)*(num_int_2/2))
        b = float((num_int_1*3)+(num_real))
        c = float(num_real*num_real*num_real)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
        
print(f'As respostas são as seguintes: a = {a:.2f}, b = {b:.2f} e c = {c:.2f}')
                

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal. 
# Use a seguinte fórmula: (72.7*altura) - 58


while True:
    altura = input('Informe a sua altura: ')
    if altura.replace('.', '', 1).isdigit():
        altura = float(altura)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
peso_ideal = ((72.7*altura)-58)

print(f'Com base na sua altura, seu peso ideal é: {peso_ideal:.2f} quilos.')

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal. 
# Use as seguintes fórmulas:
# a - Para homens: (72.7*h) - 58
# b - Para mulheres: (62.1*h) - 44.7

while True:
    h = input('Informe a sua altura: ')
    if h.replace('.', '', 1).isdigit():
        h = float(h)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

while True:
    n = input('O peso ideal é para uma estatura masculina(x) ou feminina(y)? ')
    if n == 'x':
        hx = float(h)
        peso_ideal_x = ((72.7*hx)-58)
        print(f'Com base na sua altura, seu peso ideal é: {peso_ideal_x:.2f} quilos.')
        break
    if n == 'y':
        hy = float(h)
        peso_ideal_y = ((62.1*hy)-44.7)
        print(f'Com base na sua altura, seu peso ideal é: {peso_ideal_y:.2f} quilos.')
        break
    else:
        print('Digite x para masculina ou y para feminina.')
        continue


"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de  4,00 reais por quilo excedente."""

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite.
# Na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

while True:
    peso = input('Informe o peso total dos peixes de hoje: ')
    if (peso.replace('.', '', 1).isdigit()) and (peso <= '50'):
        print('Não haverá multa, pois o peso não excedeu 50 kg.')
        break
    if peso.replace('.', '', 1).isdigit():
        peso = float(peso)
        excesso = peso - 50
        multa = excesso * 4
        print(f'O peso do pescado excedeu em {excesso:.2f} quilos.')
        print(f'Sendo assim, o valor da multa a ser paga é de: {multa:.2f} reais.')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue



# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a - salário bruto.
# b - quanto pagou ao INSS.
# c - quanto pagou ao sindicato.
# d - o salário líquido.
# e - calcule os descontos e o salário líquido, conforme a tabela:
"""(+ Salário Bruto : R$);
(- IR (11%) : R$);
(- INSS (8%) : R$);
(- Sindicato ( 5%) : R$);
(= Salário Liquido : R$)."""

# Obs.: Salário Bruto - Descontos = Salário Líquido.

while True:
    valor_hora = input('Informe quanto você ganha por hora: ')
    if valor_hora.replace('.', '', 1).isdigit():
        valor_hora = float(valor_hora)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
        
while True:
    horas = input('Informe quantas horas foram trabalhadas no mês: ')
    if horas.replace('.', '', 1).isdigit():
        horas = float(horas)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

salario_bruto = valor_hora*horas
ir = salario_bruto*11/100
inss = salario_bruto*8/100
sindicato = salario_bruto*5/100
salario_liquido = salario_bruto - ir - inss - sindicato

print('Com base em suas informações, segue demonstrativo financeiro do mês em questão:')
print(f'Salário bruto: R$ {salario_bruto:.2f}.')
print(f'Imposto de renda: R$ {ir:.2f}.')
print(f'INSS: R$ {inss:.2f}.')
print(f'Sindicato: R$ {sindicato:.2f}.')
print(f'Salário líquido: R$ {salario_liquido:.2f}.')


# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados.
# A tinta é vendida em latas de 18 litros, que custam 80,00 reais. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

valor_lata = 80.00
while True:
    area = input('Quantos metros quadrados tem a área a ser pintada? ')
    if area.replace('.', '', 1).isdigit():
        area = float(area)
        litros = area/3
        if litros <= 18:
            print(f'Com base em suas informações, você precisará de 1 lata para pintar a área informada.')
            print(f'O valor total para pintar essa área será de R$ {valor_lata:.2f}')
            break
        else:
            if (litros % 18 == 0):
                latas = litros/18
            else:
                latas = int((litros/18)+1)
        print(f'Com base em suas informações, você precisará de: {latas:.2f} latas para pintar a área informada.')
        print(f'O valor total para pintar essa área será de R$ {(latas*valor_lata):.2f}')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
        



# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados.
# A tinta é vendida em latas de 18 litros, que custam 80,00 reais ou em galões de 3,6 litros, que custam 25,00 reais.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

valor_lata = 80.00
valor_galao = 25.00
relacao_volume = int(18/3.6)

print(f'A proporção lata/galão é de: {relacao_volume} para 1.')
print(f'Caso o volume necessário seja superior a {(relacao_volume - 1)}, recomenda-se a compra da lata de 18 litros.')

print(' ')
print('Compra apenas de latas de 18 litros:')
while True:
    area = input('Quantos metros quadrados tem a área a ser pintada? ')
    if area.replace('.', '', 1).isdigit():
        area = float(area)
        litros = area/6
        if litros <= 18:
            print(f'Com base em suas informações, você precisará de 1 lata para pintar a área informada.')
            print(f'O valor total para pintar essa área será de R$ {valor_lata:.2f}')
            break
        else:
            if (litros % 18 == 0):
                latas = litros/18
            else:
                latas = int((litros/18)+1)
        print(f'Com base em suas informações, você precisará de: {latas:.2f} latas para pintar a área informada.')
        print(f'O valor total para pintar essa área será de R$ {(latas*valor_lata):.2f}')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

print(' ')
print('Compra apenas de galões de 3,6 litros:')
while True:
    area = input('Quantos metros quadrados tem a área a ser pintada? ')
    if area.replace('.', '', 1).isdigit():
        area = float(area)
        litros = area/6
        if litros <= 3.6:
            print(f'Com base em suas informações, você precisará de 1 galão para pintar a área informada.')
            print(f'O valor total para pintar essa área será de R$ {valor_galao:.2f}')
            break
        else:
            if (litros % 3.6 == 0):
                latas = litros/3.6
            else:
                latas = int((litros/3.6)+1)
        print(f'Com base em suas informações, você precisará de: {latas:.2f} galões para pintar a área informada.')
        print(f'O valor total para pintar essa área será de R$ {(latas*valor_galao):.2f}')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

print(' ')
print('Compra de galões de 3,6 litros e latas de 18 litros:')
while True:
    area = input('Quantos metros quadrados tem a área a ser pintada? ')
    if area.replace('.', '', 1).isdigit():
        area = float(area)
        litros = area/6
        if litros <= 3.6:
            print(f'Com base em suas informações, você precisará de 1 galão para pintar a área informada.')
            print(f'O valor total para pintar essa área será de R$ {valor_galao:.2f}')
            break
        if ((litros > 3.6) and (litros <= 10.8)):
            galao = int(litros/3.6)
            print(f'Com base em suas informações, você precisará de {galao} galões para pintar a área informada.')
            print(f'O valor total para pintar essa área será de R$ {(galao*valor_galao):.2f}')
            break
        else:
            if (litros % 18 == 0):
                latas = litros/18
                print(f'Com base em suas informações, você precisará de: {latas:.2f} lata(s) para pintar a área informada.')
                print(f'O valor total para pintar essa área será de R$ {(latas*valor_lata):.2f}')
                break
            else:
                latas = int(litros/18)
                galao = round((litros % 18)/3.6)
                if galao < 1:
                    print('Com base em suas informações, você precisará de:')
                    print(f'{latas} latas e 1 galão para pintar a área informada.')
                    print(f'O valor total para pintar essa área será de R$ {((latas*valor_lata)+valor_galao):.2f}')
                    break
                else:
                    print('Com base em suas informações, você precisará de:')
                    print(f'{latas} latas e {galao} galão(ões) para pintar a área informada.')
                    print(f'O valor total para pintar essa área será de R$ {((latas*valor_lata)+(galao*valor_galao)):.2f}')
                    break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps).
# Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = ('Informe o tamanho do arquivo para download: ')
velocidade = ('Informe a velocidade do download: ')

while True:
    tamanho = input('Informe o tamanho do arquivo para download: ')
    if tamanho.replace('-', '', 1).isdigit():
        tamanho = float(tamanho)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue

while True:
    velocidade = input('Informe a velocidade do download: ')
    if velocidade.replace('-', '', 1).isdigit():
        velocidade = float(velocidade)
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue
tempo = (tamanho/velocidade)/60
print('')
print(f'O tempo aproximado de download para este arquivo, usando este link é de {tempo:.2f} minutos')

