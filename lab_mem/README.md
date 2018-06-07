# Políticas de Reposição de Páginas - Laboratório 4

## Motivação

A atividade consitui em uma análise de eficiência de cinco políticas de reposição de páginas na memória, tendo uma sexta política como opcional. 

O objetivo será avaliar o grau de eficiência de cada política, considerando o parâmetro *page fault*, a partir de simulações a serem realizadas.

## Políticas

As políticas de reposição de páginas a serem apreciadas serão **FIFO**, **Second-chance**, **LRU**, **NRU**, **Aging**. Como política opcional teremos a avaliação da política **Bélády**. 

Desta forma, necessário iniciar com uma apresentação dos conceitos de cada política que já estarão ordenadas conforme a expectativa de grau de eficiência:

1. **FIFO** - Substitui a página que foi carregada na memória a mais tempo, pela nova página referenciada que não foi encontrada. Como consequência o algoritmo pode substituir páginas que são usadas muito frequentemente, mas que foram colocadas na memória há muito tempo. Assim *Tanebaum* afirma que "... em sua configuração pura, raramente é usado."

2. **Second-chace** - Constitui uma variação do algoritmo **FIFO**, pois adiciona uma *flag* na página relativa a referência, atualizando esse valor na primeira vez que a página for referenciada. Dessa forma, o algoritmo continua analizando as páginas pela ordem da lista, mas ao percorrer a lista, reinicia a *flag* daquelas que tiverem um valor positivo e as coloca no final da lista, até encontrar uma página cujo valor nunca foi atualizado, sendo esta a selecionada para a substituição. Assim nas palavras de *Tanebaum* "razoável, mas desnecessariamente ineficaz, pois permanece constantemente reinserindo páginas no final da lista".

3. **NRU** - Substitui a página não usada recentemente considerando duas *flags*, a primeira relativa a referência que é atualizada sempre que a página é referenciada, e reiniciada a cada tick do relógio, e a segunda relativa a modificação, que é atualizada na primeira modificação sofrida pela página. Dessa forma, na hora de decidir qual página substituir, o algoritmo opta pela primeira que encontrar seguindo a ordem: não referenciada e não modificada; não referenciada e modificada; referenciada e não modificada; referenciada e modificada. Assim, o algoritmo considera páginas que foram referenciadas mais importantes que páginas que sofreram alteração, dessa forma existe um custo relativo a substituição da página modificada na memória. Como consequência disto, o autor *Tanebaum* afirma que "... fornece um desempenho que, apesar de não ser ótimo, pode ser adequado."

4. **LRU** -

5. **Aging** -  