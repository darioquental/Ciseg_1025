# if estrutura de decisão

# operadores de decisão
# == igualdade 
# != diferente
# > maior que
# >= maior ou igual
# < menor que
# <= menor ou igual
# VALOR1 od VALOR2
#EX. VALOR1 > VALOR2

# operadores Logicos
# and  e
# or   ou 

#VALOR1 od VALOR2 op VALOR2 od VALOR3
# EX. VALOR1 > VALOR2 or VALOR2 > VALOR3 


# Standart -  Declarar/Criar sempre variaveis no topo e dar um nome apelativo do valor que a variavel contem , inicializar para saber o tipo de dados
num1=0
num2=0
num3=0


num1=int(input("intrud o 1 numero"))

num2=int(input("intrud o 2 numero"))

num3=int(input("intrud o 3 numero"))


if num1>num2 and num2>num3: # num1>num2>num3       12 - 10  - 8
    print(f" O maior numero é {num1}, O menor numero é {num3}")
elif num1>num3 and num3>num2: # num1>num3>num2     12 - 8  - 10
    print(f" O maior numero é {num1}, O menor numero é {num2}")

elif num2>num1 and num1>num3: # num2>num1>num3     10 - 12  - 8
    print(f" O maior numero é {num2}, O menor numero é {num3}")
elif num2>num3 and num3>num1: # num2>num3>num1     8 - 12 - 10
    print(f" O maior numero é {num2}, O menor numero é {num1}")

elif num3>num2 and num2>num1: # num3>num2>num1     8 - 10 - 12
    print(f" O maior numero é {num3}, O menor numero é {num1}")
elif num3>num1 and num1>num2: # num3>num1>num2     10 - 8 - 12
    print(f" O maior numero é {num3}, O menor numero é {num2}")
else: 
    print("alguns eram iguais")