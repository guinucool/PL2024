import sys
import re

# Tradução dos títulos MarkDown para títulos HTML
def titleTranslate(match):
    
    # Divide o título e conteúdo do título
    title = match[1]
    content = match[2]

    # Tradução do título para a respetiva tag
    tag = f'h{len(title)}'

    # Tradução completa do título
    return f'<{tag}>{content}</{tag}>'
    

# Transformações do títulos MarkDown para títulos HTML
def titleConversion(text):
    return re.sub(r'^(#{1,3}) (.*)', titleTranslate, text, flags=re.MULTILINE)

# Transformações das formatações MarkDown para formatações HTML
def formatConversion(bold, text):

    # Expressão regulares úteis à interpretação
    delim = r'[^\* \n]'
    content = r'[^\*\n]'
    asteriks = r'\**'

    # Variável que irá armazenar o texto transformados
    format = ""

    # Variáveis de auxílio na mudança de formatação
    mark = r'{1}'
    tag = 'i'

    # Define a formatação que irá capturar
    if bold:
        mark = r'{2}'
        tag = 'b'

    # Captura das formatações
    format = re.sub(fr'(\*{mark})({asteriks}{delim}{content}+?{delim}{asteriks})\1', fr'<{tag}>\2</{tag}>', text)

    # Verifica se ainda existe mais formatação fazer para esta tag
    if format != text:
        format = formatConversion(bold, format)

    # Devolve a formatação a que se chegou
    return format

# Transformação de linhas MarkDown para linhas HTML
def lineConversion(text):
    return re.sub(r'^([\-*_])\1{2,}$', r'<hr>', text, flags=re.MULTILINE)

# Tradução de uma imagem MarkDown para imagem HTML
def imageTranslate(match):
    return f'<img src="{match[2]}" alt="{match[1]}"/>'

# Tradução de um link MarkDown para link HTML
def linkTranslate(match):
    return f'<a href="{match[2]}">{match[1]}</a>'

# Transformação de uma imagem ou link MarkDown para imagem ou link HTML
def linkableConversion(image, text):

    # Identificador do objeto
    identifier = ''

    # Função de tradução do objeto
    conversion = linkTranslate

    # Coloca o identificador e a tradução como sendo a da imagem
    if image:
        identifier = '!'
        conversion = imageTranslate

    # Transformação do objeto MarkDown para HTML
    return re.sub(fr'{identifier}\[(.+?)\]\(([^ ]+?)\)', conversion, text)

# Tradução de uma lista ordenada MarkDown para lista ordenada HTML
def orderedListTranslate(match):

    # Tradução dos elementos da lista ordenada
    translate = re.sub(r'\d+\. (.*)\n*', r'   <li>\1</li>\n', match[0])

    # Inicialização e fecho da lista ordenada
    return f'<ol>\n{translate}</ol>\n'

# Tradução de uma lista MarkDown para lista HTML
def listTranslate(match):

    # Tradução dos elementos da lista ordenada
    translate = re.sub(r'\- (.*)\n*', r'   <li>\1</li>\n', match[0])

    # Inicialização e fecho da lista ordenada
    return f'<ul>\n{translate}</ul>\n'

# Transformação de uma lista MarkDown para lista HTML
def listConversion(ordered, text):

    # Definição do ponto de início de uma lista
    start = r'\-'

    # Definição da função de tradução
    translate = listTranslate

    # Troca essas definições no caso da lista ser ordenada
    if (ordered):
        start = r'\d+\.'
        translate = orderedListTranslate

    # Definição da expressão regular para um elemento
    regex = fr'{start} .*\n*'

    # Captura e tradução de todos os elementos da lista ordenada
    return re.sub(fr'^{regex}(?:{regex})+', translate, text, flags=re.MULTILINE)

# Conversão de MarkDown para HTML
def mdToHtml(text):

    # Conversão de títulos
    text = titleConversion(text)

    # Conversão de formatos
    text = formatConversion(True, text)
    text = formatConversion(False, text)

    # Conversão de linhas
    text = lineConversion(text)

    # Conversão de imagens e links
    text = linkableConversion(True, text)
    text = linkableConversion(False, text)

    # Conversão de listas
    text = listConversion(False, text)
    text = listConversion(True, text)

    # Devolução do estado final
    return text

# Leitura do ficheiro MarkDown e conversão para ficheiro HTML
def main(inp):

    # Verifica se o número de argumentos é válido
    if (len(inp) == 2):
        
        # Abertura do ficheiro MarkDown
        file = open(inp[1], 'r')

        # Conversão para HTML
        final = mdToHtml(file.read())

        # Abertura do ficheiro para escrita
        html = open(f'{inp[1]}.html', 'x')

        # Escrita do ficheiro
        html.write(final)

    else:
        print("Argumentos inválidos!")


# Captura dos argumentos do programa
if __name__ == "__main__":
    main(sys.argv)
