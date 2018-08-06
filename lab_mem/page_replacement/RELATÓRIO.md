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

Para testar a eficiência dos algoritmos, dois workloads foram criados, ambos com 1 milhão de entradas compostos pelo ID do frame a ser referenciado e o modo de operação (leitura ou escrita).

**No primeiro workload** foram acessados 2852 frames diferentes, com 892816 leituras e 107184 escritas, e foi construído de uma maneira equilibrada, sem grande diferença de quantidade de acessos entre os frames.

**Já no segundo workload** foram acessados 2543 frames diferentes, com 932830 leituras e 67170 escritas, e foi construído de uma maneira desequilibrada, com um frame (102567) sendo referenciado 47,40% das vezes.

Os 10 frames mais acessados de cada workload são:

Pos | Workload 1 | Workload 2
---|------------|-----------
1  | 195709 -> 103479 (10.35%) | 102567 -> 474010 (47.40%)
2  | 158751 -> 94913 (9.49%) | 102575 -> 39115 (3.91%)
3  | 194679 -> 77321 (7.73%) | 125679 -> 26047 (2.60%)
4  | 198834 -> 57039 (5.70%) | 86550 -> 25913 (2.59%)
5  | 251689 -> 38243 (3.82%) | 153356 -> 25831 (2.58%)
6  | 201598 -> 30098 (3.01%) | 47 -> 17595 (1.76%)
7  | 194932 -> 24218 (2.42%) | 15 -> 16883 (1.69%)
8  | 30813 -> 20440 (2.04%) | 293 -> 13100 (1.31%)
9  | 28129 -> 18863 (1.89%) | 102591 -> 9912 (0.99%)
10 | 15 -> 18343 (1.83%) | 301 -> 8539 (0.85%)
*FrameID -> Quantidade de vezes referenciado (%)*

## Resultados

**Para o primeiro workload**, temos o seguinte gráfico resultante (Número de Frames x Page Faults):

![Gráfico 1](https://github.com/rafaelkillua/projso/blob/lab4/lab_mem/page_replacement/python/output/trace.1.mem.plot.png)

Com isso, mostramos que, para esse workload equilibrado:

- O algoritmo **AGING** é o pior, independente da quantidade de frames utilizados.
- Em média, o segundo pior é o **NRU**.
- o segundo melhor foi o **FIFO**.
- O melhor foi o **SECOND CHANCE**.

**Já para o segundo workload** temos o seguinte gráfico resultante (Número de Frames x Page Faults):

![Gráfico 2](https://github.com/rafaelkillua/projso/blob/lab4/lab_mem/page_replacement/python/output/trace.2.mem.plot.png)

Com isso, mostramos que, para esse workload desequlibrado:

- Não temos um candidato absoluto a melhor ou pior algoritmo, pois depende do número de frames.
- O **FIFO**, em média, é muito ruim nesse cenário, pois é o segundo pior com 4, 8 e 32 frames e o pior com 16 frames.
- O que mais sofre alteração com a mudança do número de frames utilizados é o **NRU**, que gera um page fault muito grande com poucos frames, mas com 32 frames é bem próximo ao SECOND CHANCE.
- O algoritmo **AGING** é o melhor com 8 ou 16 frames, com 4 frames é muito próximo ao SECOND CHANCE, mas com 32 frames é o pior.
- O mais equilibrado é o **SECOND CHANCE**, que é o melhor com 4 e com 32 frames e com 8 e 16 frames é o segundo melhor.

## Expectativas x Resultados

Pos | Expectativa | Resultado (workload 1) | Resultado (workload 2)
----|-------------|------------------------|-----------------------
1   | FIFO        | SECOND CHANCE          | SECOND CHANCE
2   | SECOND CHANCE | FIFO                 | AGING
3   | NRU         | NRU                    | NRU
4   | AGING       | AGING                  | FIFO
*Resultados aproximados*

## Conclusão

**Com isso, concluimos que** a maneira como o workload foi construído afeta a eficiência dos algoritmos de reposição de páginas na memória, e, não levando em conta o algoritmo ótimo, não é possível chegar a uma conclusão exata de qual algoritmo dentre esses estudados e implementados é o melhor.