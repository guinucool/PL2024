# Importação de bibliotecas necessárias
from ply.lex import lex
import sys

# Tokens que identificam os elementos da linguagem
tokens = ('SELECT', 'FROM', 'WHERE', 'ID', 'NUMBER', 'STRING', 'OPERATOR', 'CONNECTOR', 'NEGATOR')

# Literais de elementos da linguagem
literals = [',', '*']

# Definição da recolha de tokens de select
def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'

    # Devolução do token recolhido
    return t

# Definição da recolha de tokens de from
def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'

    # Devolução do token recolhido
    return t

# Definição da recolha de tokens de where
def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'

    # Devolução do token recolhido
    return t

# Definição da recolha de conectores de comparação
def t_CONNECTOR(t):
    r'([Aa][Nn][Dd])|([Oo][Rr])'

    # Devolução do token lido
    return t

# Definição da recolha de conectores de negação
def t_NEGATOR(t):
    r'[Nn][Oo][Tt]'

    # Devolução do token lido
    return t

# Definição da recolha de operadores de comparação
def t_OPERATOR(t):
    r'([<>]=?)|([!=]=)'

    # Devolução do token lido
    return t

# Definição da recolha de identificadores
def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'

    # Devolução do identificador recolhido
    return t

# Definição da recolha de números
def t_NUMBER(t):
    r'[+-]?\d+(\.\d+)?'

    # Conversão do valor em formato numérico
    t.value = float(t.value)

    # Devolução do token lido
    return t

# Definição da recolha de elementos textuais
def t_STRING(t):
    r'"[^\n"]*"'

    # Captura do valor contido na string de texto
    t.value = t.value[1:-1]

    # Devolução do elemento textual
    return t

# Definição dos elementos da string para ignorar
t_ignore = ' \t\n'

# Definição da captura de erros na captura
def t_error(t):
    print(f"Carácter ilegal encontrado - {t.value[0]}!")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex()

# Tradução da frase dada para tokens
def analex(query):
    
    # Introdução da query
    lexer.input(query)
    
    # Tradução para tokens
    while token := lexer.token():
        print(token)

# Programa de tradução de queries
def parser():

    # Leitura do input do utilizador
    for line in sys.stdin:
        analex(line)

# Execução da leitura e tradução de queries
parser()