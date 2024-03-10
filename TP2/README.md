# Conversor simples de Markdown para HTML
**Autor: Guilherme Oliveira, A100592**

## Lista de parágrafos
- O conversor de **Markdown** para **HTML** funciona de forma simples definindo uma função de conversão, através do uso de expressões regulares, para cada tipo de elemento.
- Os títulos são todos capturados pela mesma expressão, sendo apenas avalidado o número de **cardinais** para se decidir qual o tipo do título (**h1, h2 ou h3**).
- As formatações de texto (*itálico* e **negrito**) são definidas de forma recursiva (visto que pode existir conteúdo com ***ambas as formatações***), começando por se substituir todos os duplos astericos por **< b >** e **</ b >** e, seguidamente, todos os singulares por *< i >* e *</ i >*.
- As linhas são capturadas apartir do momento que existem três ou mais travessões, astericos ou underscores seguidos, numa linha única, sendo substituídos pela tag respetiva.
- As imagens e links são capturadas e substítuidas de forma semelhante, usando grupos de captura (um para a ligação e outro para o nome da ligação). Como a sua estrutura é quase idêntica são capturadas primeiro as imagens, restando depois apenas os links, não havendo, portanto, possibilidades de conversões erradas.
- Uma lista é capturada de uma só vez, sendo depois os conteúdos do seus elementos colocados em tags **< li >** e embrulhados nas tags de lista respetivas (**< ul >** em caso de listas e **< ol >** em caso de listas ordenadas).
- O conversor recebe, portanto, como input do programa o local do ficheiro **Markdown** e coloca, no mesmo local, um ficheiro com exatamento o mesmo nome mas em formato **HTML**, já convertido.