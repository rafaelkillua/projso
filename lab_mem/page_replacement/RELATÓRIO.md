# Políticas de Reposição de Páginas - Laboratório 4

## Motivação

A atividade consitui em uma análise de eficiência de cinco políticas de reposição de páginas na memória, tendo uma sexta política como opcional. 

O objetivo será avaliar o grau de eficiência de cada política, considerando o parâmetro *page fault*, a partir de simulações a serem realizadas.

## Políticas

As políticas de reposição de páginas a serem apreciadas serão **FIFO**, **Second-chance**, **LRU**, **NRU**, **Aging**. Como política opcional teremos a avaliação da política **Bélády**. 

Desta forma, necessário iniciar com uma apresentação dos conceitos de cada política que já estarão ordenadas conforme a expectativa de grau de eficiência:

1. **FIFO** - Substitui a página que foi carregada na memória a mais tempo, pela nova página referenciada que não foi encontrada. Como consequência o algoritmo pode substituir páginas que são usadas muito frequentemente, mas que foram colocadas na memória há muito tempo. Assim *Tanenbaum* afirma que "... em sua configuração pura, raramente é usado."

2. **Second-chance** - Constitui uma variação do algoritmo **FIFO**, pois adiciona uma *flag* na página relativa a referência, atualizando esse valor na primeira vez que a página for referenciada. Dessa forma, o algoritmo continua analizando as páginas pela ordem da lista, mas ao percorrer a lista, reinicia a *flag* daquelas que tiverem um valor positivo e as coloca no final da lista, até encontrar uma página cujo valor nunca foi atualizado, sendo esta a selecionada para a substituição. Assim nas palavras de *Tanenbaum* "razoável, mas desnecessariamente ineficaz, pois permanece constantemente reinserindo páginas no final da lista".

3. **NRU** - Substitui a página não usada recentemente considerando duas *flags*, a primeira relativa a referência que é atualizada sempre que a página é referenciada, e reiniciada a cada tick do relógio, e a segunda relativa a modificação, que é atualizada na primeira modificação sofrida pela página. Dessa forma, na hora de decidir qual página substituir, o algoritmo opta pela primeira que encontrar seguindo a ordem: não referenciada e não modificada; não referenciada e modificada; referenciada e não modificada; referenciada e modificada. Assim, o algoritmo considera páginas que foram referenciadas mais importantes que páginas que sofreram alteração, dessa forma existe um custo relativo a substituição da página modificada na memória. Como consequência disto, o autor *Tanenbaum* afirma que "... fornece um desempenho que, apesar de não ser ótimo, pode ser adequado."

4. **LRU** - Baseado na ideia de que as páginas mais recentemente utilizadas provavelmente serão utilizadas novamente nas próximas instruções, o algoritmo LRU sugere que, quando ocorrer uma falta de página, a página não utilizada pelo maior período de tempo deve dar lugar a nova página. Para implementar corretamente o LRU, é necessário que seja em hardware, pois é muito custoso não sendo possível sua implementação. Mas existem duas abordagens que aproximam sua proposta:

    - **NFU** (Not Frenquently Used) que mantém contadores em hardware para cada página, incrementado a cada *instrução* realizada e salva a cada referência à página, assim, a menos recentemente utilizado seria a que tivesse o menor contador. Mas esta abordagem não esquece o histórico, logo uma página que foi muito usada no início da execução nunca sairá da memória, mesmo que não venha a ser mais utilizada no futuro;

    - **outra abordagem** é utilizar matrizes de nxn bits (n = quantidade de molduras de página), e, sempre que uma moldura k for referenciada, todos os bits da linha k se tornam 1 e todos os bits da coluna k se tornam 0. Num instante qualquer, a linha cujo valor binário é o menor é o menos recentemente utilizado. A limitação dessa abordagem decorre do fato de que podem ocorrer empates, visto que o bit é a manutenção e atualização da matriz que é muito custosa conforme houver o aumento do número de páginas a serem monitoradas.

5. **Aging** - O algoritmo **Aging** (envelhecimento) consiste em associar a cada página um contador de 8 bits, e a cada tick de clock, o contador é deslocado à direita e o valor do bit **R** é adcionado ao bit mais às esquerda do contador, ao invés do bit mais à direita. A página a ser removida é aquela que tem o menor contador, pois, se não for referenciada por um tempo, terá valores 0 nos bits mais signifcativos. Há duas diferenças do **Aging** para o **LRU**: se temos duas páginas a escolher para remover A, de contador 00100000, e B, de contador 00100100, que não foram referenciadas nos últimos 2 ticks de clock, o LRU removeria aleatoriamente entre A e B, e o Aging removeria A, pois tem contador menor; se duas páginas não foram referenciados há mais de 8 ticks de clock, fazendo o contador chegar a 00000000, o Aging não tem como verificar qual página foi referenciada há mais tempo e removeria aleatoriamente entre as duas, e o LRU teria essa informação. Este algoritmo é considerando por Tanebaum um dos melhores, sendo amplamente utilizado na prática.


## Workloads

Para testar a eficiência dos algoritmos, dois workloads foram criados, ambos com 1 milhão de entradas compostos pelo ID do frame e o modo de operação (leitura ou escrita).

**O primeiro workload** foi construído usando...

**Já o segundo workload** é um pouco diferente e...

## Resultados

**Para o primeiro workload**, temos o seguinte gráfico resultante (Page Faults x Número de Frames):

![Gráfico 1](https://github.com/rafaelkillua/projso/blob/lab4/lab_mem/page_replacement/python/output/trace.1.mem.plot.png)

Com isso, mostramos que, para esse workload, claramente o algoritmo AGING é o pior, independente da quantidade de frames utilizados. Em média, o segundo pior algoritmo é o NRU. Nessa situação, o melhor foi o SECOND CHANCE, e o segundo melhor foi o FIFO, contrariando um pouco o resultado esperado por nós. 

**Já para o segundo workload** temos o seguinte gráfico resultante (Page Faults x Número de Frames):

![Gráfico 2](https://github.com/rafaelkillua/projso/blob/lab4/lab_mem/page_replacement/python/output/trace.2.mem.plot.png)

Com isso, mostramos que, para esse workload, não temos um candidato absoluto a melhor ou pior algoritmo, pois depende mais do número de frames. Por exemplo, o algoritmo AGING é o melhor com 4, 8 ou 16 frames, mas com 32 frames é o pior. O mais equilibrado é o SECOND CHANCE, e o que mais sofre alteração com a mudança do número de frames utilizados é o NRU, que gera um page fault muito grande com poucos frames, mas com 32 frames é bem próximo ao SECOND CHANCE.

## Conclusão

**Com isso, concluimos que** a eficiência dos algoritmos de reposição de páginas na memória depende de como foi construído o workload.