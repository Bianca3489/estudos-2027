# Variáveis em Python são espaços na memória que armazenam valores.
# Elas são criadas quando atribuímos um valor a uma variável.

# Sintaxe: nome_da_variavel = valor
# As variáveis em Python são dinamicamente tipadas, ou seja, não precisamos declarar o tipo da variável.
# O tipo da variável é inferido automaticamente pelo valor que ela recebe.

# O operador "=" é usado para atribuir um valor a uma variável.

# Regras para nomear variáveis em Python:
# - Devem começar com uma letra ou underscore (_)
# - Podem conter letras, números e underscores
# - São case-sensitive
# - Não podem conter espaços
# - Não podem conter caracteres especiais
# - Não podem ser palavras reservadas

nome = 'Bianca'
idade = 37
estado = 'Rio de Janeiro'
profissao = 'Engenheira de Dados'
tem_cachorro = True

# Formatação de strings
# f-strings é uma forma de formatar strings em Python.
# Deve começar com a letra 'f' antes das aspas.
# Os valores das variáveis são colocados entre chaves {}.
# Exemplo: f'Nome: {nome}'
# Deve-se evitar espaço dentro das chaves. Se houver, deve-se usar f'Nome: {nome + " " + sobrenome}'

# Exemplo de formatação de strings usando f-string:
# nome = 'Bianca'

print(f'Nome: {nome}, Idade: {idade}, Estado: {estado}, Profissão: {profissao}, Tem cachorro: {tem_cachorro}')

# Verificação de tipos de variáveis

print(type(nome))
print(type(idade))
print(type(estado))
print(type(profissao))
print(type(tem_cachorro)) 


