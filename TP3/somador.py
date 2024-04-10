# Importação do módulo de expressões regulares
import re

# Importação do módulo do sistema
import sys

# Definição das expressões regulares pertinentes
inteiro = r'[+\-]?\d+'
on = r'[Oo][Nn]'
off = r'[Oo][Ff]{2}'
equal = r'='

# Variável que irá armazenar o estado da soma
soma = 0

# Definição de um autômato finito determinístico
class AFD:

    # Construtor do autômato finito determinístico
    def __init__(self, States, Alphabet, Final, Trasition, Initial):
        
        # Conjunto de estados do autômato
        self.__States = States

        # Conjunto do alfabeto do autômato
        self.__Alphabet = Alphabet

        # Conjunto de estados finais do autômato
        self.__Final = Final

        # Conjunto de transições do autômato
        self.__Trasition = Trasition

        # Estado inicial do autômato
        self.__Current = Initial

    # Execução do conteúdo no autômato
    def run(self, content):

        # Inverte a ordem da lista de conteúdo
        content.reverse()

        # Percorre a lista de conteúdo inteira
        while len(content) > 0:
            
            # Retira o primeiro elemento da lista original
            elem = content.pop()

            # Percorre as transições definidas no estado
            for transition in self.__Trasition[self.__Current]:

                # Verifica qual é a transição associado ao elemento
                if (re.match(transition[0], elem)):

                    # Aplicação a função associada à transição
                    transition[1](elem)

                    # Mudança do estado atual para o estado associado à transição
                    self.__Current = transition[2]

        
    # Devolve o estado final do autômato    
    def finish(self):
        return self.__Current in self.__Final
    
# Função de adição de um número à soma
def token_add(token):

    # Enunciação da propriedade global de soma
    global soma

    # Conversão do token para inteiro
    value = int(token)

    # Soma do valor do token ao acumulador de soma
    soma += value

# Função de impressão da soma atual
def token_print(token):

    # Enunciação da propriedade global de soma
    global soma

    # Impressão da soma para o stdout
    print(soma)

# Função que ignora um token dado
def token_pass(token):
    pass

# Tronco principal do programa de leitura e conversão do texto e execução da máquina de estados
def main():

    # Criação do autômato pretendido
    machine = AFD({'On', 'Off'},
                {inteiro, on, off, equal},
                {'On', 'Off'},
                {'On': [(inteiro, token_add, 'On'), (equal, token_print, 'On'), (on, token_pass, 'On'), (off, token_pass, 'Off')],
                 'Off': [(inteiro, token_pass, 'Off'), (equal, token_print, 'Off'), (off, token_pass, 'Off'), (on, token_pass, 'On')]},
                'On')

    # Leitura de um texto do stdin até o EOF
    for line in sys.stdin:

        # Conversão do texto lido do stdin em tokens
        tokens = re.findall(fr'{inteiro}|{on}|{off}|{equal}', line)
        
        # Execução do autômato
        machine.run(tokens)

# Execução do tronco principal do programa
main()