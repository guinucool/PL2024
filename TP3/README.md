# Somador de números com estados On/Off
**Autor: Guilherme Oliveira, A100592**

## Lista de parágrafos
- O somador é definido através de um autômato finito determinístico (**AFD**) para processar uma sequência de comandos, fazendo operações numa soma acumulada e alternando entre dois estados: *"On"* e *"Off"*.
- O autômato recebe uma lista já filtrada de elementos que podem ser possíveis comandos e percorre-os um a um.
- Existem várias operações definidas para cada estado do autômato, sendo que várias delas são comuns entre estados. Ou seja, é possível transitar entre estados independentemente do estado atual, e é sempre possível imprimir a soma atual.
- A diferença é nos comandos que tratam a soma e a subtração de números, que são transições apenas definidas para o estado *"On"*. Sempre que um número aparece na lista e o autômato está neste estado, esse número (que pode ser positivo ou negativo) é adicionado à soma global.
- O input do programa é dado pelo próprio utilizador através da própria linha de comandos.