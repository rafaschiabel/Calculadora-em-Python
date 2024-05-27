# 1. Calculadora Simples
# Crie uma calculadora que possa realizar operações básicas como adição, subtração, multiplicação e divisão. Pode ser um aplicativo de linha de comando.

print('## CALCULADORA ##')
print('Calcula operação matemática entre 2 números.')
print('')

# Conversão de string para float, substituindo , por .
def converter(num_string):
    if ',' in num_string:
        return num_string.replace(',','.')
    return float(num_string)

# Verificador de números
def verifica_num(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
# Recebe 1º número
num1 = input('Primeiro número: ')
while verifica_num(num1) == False:
    print('Valor inválido!')
    num1 = input('Primeiro número: ')
num1 = converter(num1)

# Recebe operador matemático
op = input('Operação: ')
while not any(operador in op for operador in ['+','-','*','/']):
    print('Operação inválida!')
    op = input('Operação: ')

# Recebe 2º número
num2 = input('Segundo número: ')
while verifica_num(num2) == False:
    print('Valor inválido!')
    num2 = input('Segundo número: ')
num2 = converter(num2)

# Calculadora
if op == '+':
    resultado = num1 + num2
    print(resultado)
else:
    if op == '-':
        resultado = num1 - num2
        print(resultado)
    else:
        if op == '*':
            resultado = num1 * num2
            print(resultado)
        else:
            if op == '/':
                if num2 == 0.0:
                   print('Impossível a divisão por 0!')
                else:
                    resultado = num1 / num2
                    print(resultado)