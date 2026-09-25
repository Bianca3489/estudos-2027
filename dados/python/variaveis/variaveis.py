# Variaveis e tipos de dados

# Tipos de dados: 
#   String: texto
#   Inteiro: número inteiro
#   Float: número decimal
#   Booleano: True ou False

nome = 'Bianca'
idade = 37
altura = 1.61
estado = 'Rio de Janeiro'
profissao = 'Engenheira de Dados'
tem_cachorro = True

# O que são variáveis?
# Variáveis em Python são espaços na memória que armazenam valores.
# Elas são criadas quando atribuímos um valor a uma variável.

# O que são variáveis em python?
# Variáveis em Python são espaços na memória que armazenam valores.
# Elas são criadas quando atribuímos um valor a uma variável.

# Sintaxe: nome_da_variavel = valor
# As variáveis em Python são dinamicamente tipadas, ou seja, não precisamos declarar o tipo da variável.
# O tipo da variável é inferido automaticamente pelo valor que ela recebe.

# O operador "=" é usado para atribuir um valor a uma variável.

# Regras para nomear variáveis em Python:
# - Devem começar com uma letra ou underscore (_)
# - Podem conter letras, números e underscores (Ex: minha_variavel, minhaVariavel, minha_Variavel)
# - São case-sensitive (as variáveis 'nome', 'Nome' e 'NOME' são diferentes)
# - Não podem conter espaços (Ex: minha variavel - inválido)
# - Não podem conter caracteres especiais (exceto underscore) (Ex: minha@variavel - inválido)
# - Não podem ser palavras reservadas do Python (ex: if, else, for, while, def, class, etc.)


# Formatação de strings
# f-strings é uma forma de formatar strings em Python.
# Deve começar com a letra 'f' antes das aspas.
# Os valores das variáveis são colocados entre chaves {}.
# Exemplo: f'Nome: {nome}'
# Deve-se evitar espaço dentro das chaves. Se houver, deve-se usar f'Nome: {nome + " " + sobrenome}'

# Exemplo de formatação de strings usando f-string:
# nome = 'Bianca'

print(f'Nome: {nome}, Idade: {idade}, Altura: {altura}, Estado: {estado}, Profissão: {profissao}, Tem cachorro: {tem_cachorro}')

# Verificação de tipos de variáveis

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estado))
print(type(profissao))
print(type(tem_cachorro)) 


