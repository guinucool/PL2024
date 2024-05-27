# Análise estatística de exames médicos desportivos
## Guilherme Oliveira, A100592

## Lista de parágrafos
- A calculadora de estatísticas lê um *dataset* acerca de exames médicos desportivos (passando-o como argumento do programa) e exibe informações estatísticas pedidas sobre o mesmo (através de um segundo argumento do programa).
- As opções de estatísticas são **modalidades, aptidao e escaloes (idade)**, sendo que o escalão será o que contiver a idade escolhida como argumento.
- As estatísticas vão sendo calculadas linha a linha da leitura do *dataset*, sendo adicionadas a um conjunto (para evitar repetições) todas as modalidades, contados os atletas aptos e inaptos (para calcular as percentagens posteriormente) e adicionados os atletas ao respetivo escalão, dependendo da idade.
- Cada linha é dívida pelas vírgulas para obter os dados individuais.