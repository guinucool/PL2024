# Importação de bibliotecas necessárias
import sys

# Leitura do CSV e criação das estatistícas
def read_csv(path):
    
    # Abertura do CSV
    csv = open(path, 'r')

    # Ignora o índice do CSV
    next(csv)

    # Criação das variáveis que vão armazenar as estatísticas
    modalidades = set()
    aptos = 0
    inaptos = 0
    escaloes = {}

    # Leitura das linhas do dataset
    for line in csv:

        # Divisão das informações de um utilizador
        info = line.split(',')

        # Adição da modalidade ao conjunto de modalidades
        modalidades.add(info[8])

        # Verificação de aptidão
        if (info[12] == "true\n"):
            aptos = aptos + 1
        else:
            inaptos = inaptos + 1

        # Conversão da idade do atleta
        age = int(info[5])
        ageI = age // 5

        # Atribuição do atleta ao escalão
        if (ageI in escaloes.keys()):
            escaloes[ageI].append(f'{info[3]} {info[4]}')
        else:
            escaloes[ageI] = [f'{info[3]} {info[4]}']

    # Devolução das estatistícas
    return (modalidades, aptos / (aptos + inaptos), inaptos / (aptos + inaptos), escaloes)

# Leitura e obtenção das estatísticas
(mod, apt, inapt, esc) = read_csv(sys.argv[1])

# Interpretação do comando para seleção da estatística
if (sys.argv[2] == "modalidades"):
    
    # Impressão das modalidades
    print("Modalidades:")

    # Impressão de todos os elementos
    for elem in mod:
        print(elem)

elif (sys.argv[2] == "aptidao"):

    # Impressão das percentagens
    print(f"Aptidão: { apt * 100 }%")
    print(f"Inaptidão: { inapt * 100 }%")

elif (sys.argv[2] == "escaloes" and len(sys.argv) == 4):

    # Determina o escalão pretendido
    e = int(sys.argv[3]) // 5

    # Impressão do escalão
    print(f'Escalão[{e*5}-{(e*5)+4}]:')

    # Impressão dos membros
    for elem in esc[e]:
        print(elem)

else:

    # Em caso de parâmetro inválido
    print("Estatística escolhida é inválida")