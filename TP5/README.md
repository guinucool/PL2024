# Máquina de Venda Automática
**Autor: Guilherme Oliveira, A100592**

## Lista de parágrafos
- A máquina de venda automática é definida através de um analisador léxico que, consoante os *tokens* que recebe, permite a impressão da listagem de produtos, inserção de moedas, seleção e compra de produtos e o término da sessão.
- A lista de produtos inicial da máquina, e as suas quantidades, é carregada de uma configuração **JSON** especificada como argumento do programa.
- A máquina utiliza um conjunto de estados (**insert e select**) para gerir a inserção de moedas e a seleção de produtos, respetivamente. O estado inicial é o modo de comandos, onde a máquina espera por comandos do utilizador.
- Os *tokens* definidos permitem o reconhecimento de comandos (**LISTAR, MOEDA, SELECIONAR, SAIR**), moedas e seus valores (**COIN**) (usados apenas no estado de inserção de moedas) e identificadores de produtos (**ID**) (usados apenas no estado de seleção de produto).
- O literal ponto (.) é usado para sinalizar o fim da inserção de moedas, retomando o estado de reconhecimento de comandos.
- Durante o estado inteiro do programa é mantido o saldo consoante as operações executadas, sendo que no final do programa é calculdado o número e tipos de moedas para que seja dado o minímo número de moedas de troco possível.
- A seleção de um produto para compra apenas funciona caso o utilizador tenha saldo suficiente para o adquirir.