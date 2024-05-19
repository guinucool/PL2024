# Importação da bibliotecas necessárias
from ply.lex import lex
from datetime import datetime
import json
import sys

# Lista de elementos presentes na máquina
elems = []

# Listas de moedas possíveis
coins = { '2e' : 200, '1e' : 100, '50c' : 50, '20c' : 20, '10c' : 10, '5c' : 5, '2c' : 2, '1c' : 1 }

# Saldo atual do utilizador na máquina
wallet = 0

# Estados do analisador léxico
states = (
    ('insert', 'exclusive'),
    ('select', 'exclusive'),
)

# Tokens do analisador léxico
tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'COIN', 'SAIR', 'ID')

# Literais da linguagem da máquina
literals = ['.']

# Comando de listagem de elementos da máquina
def t_LISTAR(t):
    r'LISTAR'
    print(f'''cod   | nome      | quantidade    | preço
    -----------------------------------''')

    # Impressão de todos os elementos da máquina
    for elem in elems:
        print(f'{elem["cod"]} | {elem["nome"]} | {elem["quant"]} | {saldo_print(elem["preco"])}')

    # Sinaliza final da instrução
    return t

# Comando de início do modo de inserção de moedas
def t_MOEDA(t):
    r'MOEDA'
    
    # Atualiza o estado da máquina para inserção de moedas
    t.lexer.begin('insert')

    # Devolve o resultado obtido
    return t

# Comando de seleção de um produto
def t_SELECIONAR(t):
    r'SELECIONAR'

    # Atualiza o estado da máquina para seleção de produtos
    t.lexer.begin('select')

    # Devolve o resultado recolhido
    return t

def t_insert_COIN(t):
    r'\d{1,2}[ec]'

    # Variável de carteira
    global wallet

    # Verifica se a moeda é válida
    if t.value in coins:

        # Adição do seu valor à carteira
        wallet = wallet + coins[t.value]

    # Tratamento caso a moeda não seja válida
    else:
        print(f"Moéda ilegal introduzida - {t.value[:-1]}!")

    # Devolução do resultado obtido
    return t

# Comando de saída da máquina de venda
def t_SAIR(t):
    r'SAIR'

    # Impressão das mensagens de despedida
    print(f'Pode retirar o troco: {calc_change(wallet)}.')
    print('Até à próxima!')

    # Sinaliza final do programa
    return t

# Comando de saída do estado de inserção de moedas
def t_insert_DOT(t):
    r'\.'

    # Saída do estado de inserção de moedas
    t.lexer.begin('INITIAL')

    # Atualização do tipo do token recolhido
    t.type = '.'

    # Imprime o novo saldo atual
    print(f'Saldo = {saldo_print(wallet)}')

    # Devolve o resultado obtido
    return t

# Captura de identificadores de produto
def t_select_ID(t):
    r'\w\d{2}'

    # Variável de carteira
    global wallet

    # Verifica se o produto foi encontrado
    found = False

    # Busca pelo elemento pretendido
    for elem in elems:

        # Verifica se é o produto pretendido
        if elem['cod'] == t.value and elem['quant'] > 0:

            # Confirma o produto pedido
            found = True
            
            # Verifica se o utilizador tem saldo suficiente
            if elem['preco'] > wallet:

                # Impressão da falha na compra
                print("Saldo insuficiente para satisfazer o seu pedido!")
                print(f"Saldo = {saldo_print(wallet)}; Pedido = {saldo_print(elem['preco'])}")

            else:

                # Compra do produto
                elem['quant'] = elem['quant'] - 1
                wallet = wallet - elem['preco']

                # Impressão de informações úteis
                print(f'Pode retirar o produto dispensado "{elem["nome"]}"')
                print(f'Saldo = {saldo_print(wallet)}')

    # Verifica se o produto foi encontrado
    if not found:
        print("O produto selecionado não está disponível!")

    # Saída do estado de seleção do produto
    t.lexer.begin('INITIAL')

    # Devolução do resultado obtido
    return t

# Carácteres para ignorar
t_ignore = ' \t\n'

# Carácteres para ignorar na inserção de moedas
t_insert_ignore = ', \t\n'

# Carácteres para ignorar na seleção de produtos
t_select_ignore = ' \t\n'

# Captura de erros de inserção de comandos
def t_error(t):
    print(f"Comando ilegal introduzido - {t.value[:-1]}!")
    t.lexer.skip(len(t.value))

# Captura de erros de inserção de moedas
def t_insert_error(t):
    print(f"Moéda ilegal introduzida - {t.value[:-1]}!")
    t.lexer.skip(len(t.value))

# Captura de erros de seleção de produtos
def t_select_error(t):
    print(f"Produto ilegal introduzido - {t.value[:-1]}!")
    t.lexer.skip(len(t.value))

# Criação do analisador léxico que irá criar a máquina
lexer = lex()

# Impressão do valor do saldo formatado
def saldo_print(saldo):

    # Verifica se o saldo é superior a cêntimos
    if saldo >= 100:
        return f'{int(saldo / 100)}e{int(saldo % 100)}c'

    # Cálculo dos cêntimos
    else:
        return f'{int(saldo % 100)}c'
    
# Cálculo do troco dado pela máquina em moedas
def calc_change(saldo):

    # Dicionário de troco
    change = {}

    # Cria um dicionário de moedas
    for coin in coins:
        change[coin] = 0

    # Verifica qual moeda que melhor se encaixa no saldo atual
    while saldo > 0:

        # Moeda mais alta atualmente
        high = '1c'

        # Procura em todas as moedas
        for coin in change:

            # Guarda caso seja a mais alta
            if (saldo > coins[coin]) and (coins[coin] > coins[high]):
                high = coin

        # Incrementa a moeda mais alta
        change[high] = change[high] + 1

        # Retira o valor da moeda ao saldo
        saldo = saldo - coins[high]

    # String de quantidade troco
    changeInCoins = ""

    # Impressão das quantidas na string
    for coin in change:

        # Verifica se existe quantidade suficiente para imprimir a moeda
        if (change[coin] > 0):

            # Vefica se já alguma moeda foi inserida no resultado
            if (len(changeInCoins) > 0):
                changeInCoins = changeInCoins + ", "
            
            # Adição da moeda e da quantidade ao resultado final
            changeInCoins = changeInCoins + f'{change[coin]}x {coin}'

    # Devolução do dicionário de troco
    return changeInCoins

# Função de execução da máquina de vendas
def machine(config):

    # Abertura da configuração em formato json
    file = open(config, 'r+')

    # Variável que irá armazenar o conteúdo da máquina
    global elems

    # Conversão da informação em memória
    elems = json.load(file)

    # Mensagem de boas vindas
    print(f'{datetime.now().strftime("%Y-%m-%d")}, Stock carregado, Estado atualizado.')
    print('Bom dia! Estou disponível para atender o seu pedido!')

    # Leitura das várias linhas de comando da máquina    
    for line in sys.stdin:

        # Introdução no analisador léxico da máquina
        lexer.input(line)

        # Interpretação dos comandos
        while token := lexer.token():

            # Caso seja um comando de término
            if token.type == "SAIR":

                # Armazenamento da configuração
                json.dump(elems, file)

                # Conclusão do programa
                return

# Execução da máquina
machine(sys.argv[1])