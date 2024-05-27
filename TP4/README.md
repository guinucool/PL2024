# Analisador léxico para uma linguagem de Query
**Autor: Guilherme Oliveira, A100592**

## Lista de parágrafos
- O analisador léxico para uma linguagem de *Query*, utilizando a biblioteca **PLY**. Ele lê comandos escrito nesta linguagem do *stdin* e converte essas consultas numa sequência de *tokens* que representam as diferentes componentes da linguagem.
- Os *tokens* são definidos para identificar comandos da linguagem (**SELECT, FROM, WHERE**), colunas de informação das tabelas (**ID**), números (*NUMBER*), strings (**STRING**), operadores de comparação (**OPERATOR**), conectores lógicos (**CONNECTOR**), e operadores de negação (**NEGATOR**).
- Ainda são considerados literais como vírgulas e asteriscos, que pretendem permitir a criação de um conjunto de colunas ou a agregação de todas nos comandos, respetivamente.