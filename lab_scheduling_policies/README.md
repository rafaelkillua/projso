# Especificação do Algoritmo de Escalonamento - Lab 02


## Especificação do Algoritmo planejado

O **algoritmo de escalonamento** de processos será implementado seguindo o modelo de loteria com prioridade.

Existirão **quatro classes de prioridade** no sistema com valores que variam de 0 a 3, sendo a **prioridade 0** como a **menos relevante** e a **prioridade 3** como a **mais relevante**.

Os processos a serem executados serão enfileirados em uma lista, que é **ordenada segundo seu PID**, representando a ordem de chegada no sistema.

O **escalonador irá selecionar a prioridade** do próximo processo a ser executado a partir de um **sorteio** de um valor que pode **variar entre 0 e 100**, onde os valores menores que 10 representam a prioridade 0, os menores que 25 e maiores que 10 representam a prioridade 1, os maiores que 25 e menores que 50 representam a prioridade 2, e os maiores que 50 representam a prioridade 3.

Desta forma, a seleção do próximo processo a ser realizado segue o seguinte padrão: *sorteio de um valor -> seleção da prioridade correspondente -> validação de existência de pelo menos um processo com a prioridade selecionada -> a partir do último processo executado, selecionar o próximo processo na lista que tenha a prioridade selecionada*.

Assim, o algoritmo visa **garantir uma preferência na alocação** de processos com maior prioridade na CPU, reduzindo o risco Inanição (*Starvation*), ao **custo de um aumento do processamento** na hora de selecionar a prioridade do processo a ser alocado.

Portanto, em um **processamento médio de várias interações** é esperado que a distribuição de acesso a CPU dos processos de cada prioridade se aproximem da seguinte divisão: 

- Prioridade 0: 10%
- Prioridade 1: 15%
- Prioridade 2: 25%
- Prioridade 3: 50%

## Análise do Desempenho na simulação

As simulações foram realizadas considerando três políticas de escalonamento de processos:

* **Round Robin**: que distribui igualmente o tempo de CPU entre os processos ativos;
* **Priority Random**: que realiza um sorteio da prioridade a ser atendida, conforme descrito no tópico anterior;
* **Xv6 Priority Random**: que faz o mesmo que o anterior, porém realiza um novo sorteio a cada vez que não é encontrada um processo com a prioridade sorteada na lista, em uma varredura parcial.

Para realizar a simulação foram geradas duas cargas de trabalho, cada uma com trinta processos.

### Simulação com Carga de Trabalho Aleatória

A primeira que tem o objetivo de gerar um situação próxima da realidade onde entrega-se a aleatoriedade a decisão sobre o tempo de duração do processo, sua prioridade e o momento em que ele é iniciado.

![](plots/workload_rnd_plot.png)

A partir da imagem podemos verificar que a duração dos processos nunca ultrapassa o limite de 1000 segundos no caso da carga de trabalho aleatória.

Outro ponto importante a se mencionar é que a duração dos procesoss de prioridade 2 e 3 são considerávelmente maiores que os de prioridade menor.

Assim realizar ao simulação utilizando a política de escalonamento **Round Robin** ficou clara a distribuição equânime da CPU entre os processo:

![](plots/extra_time_rnd_rr_plot.png)

Assim podemos perceber que os processos de todas as prioridades tiveram um tempo de execução médio entre 1750 e 2000 segundos.

No caso da política de escalonamento **Priority Random** a política de priorização causou uma drástica redução no tempo de execução das tarefas de prioridade 3 em detrimento das demais.

Contudo o mesmo não aconteceu integralmente com as prioridas 1 e 2, onde era esperado que todos os processos de prioridade 2 tivessem um tempo de execução inferior aos de prioridade 1, mas como o intervalo dos dois casos tem valores sobrepostos, então não podemos afirmar com toda a certeza de que o comportamento esperado não ocorreu. 

![](plots/extra_time_rnd_pr_plot.png)

Por fim, no caso do algoritmo implementado no xv6 é perceptível resultados similares ao anterior, mas devido as diferenças de implementação, que causam uma maior quantidade de sorteios, o que resultou numa maior equalização dos resultados, inclusive com a redução da diferença no tempo de execução entre as prioridades 1 e 2.

![](plots/extra_time_rnd_xpr_plot.png)

Assim, podemos concluir que as políticas de prioridade atigiram seu objetivo, e a política implementada no kernel do xv6 teve um desempenho melhor do que o esperado, visto que a diferença de implementação foi vista inicialmente como um equívoco.

### Simulação com Carga de Trabalho Ocupada

A segunda modifica a anterior apenas para que todos os processos tenham a mesma duração de 100 segundos, e sejam iniciados em uma ordem com diferença de início de apenas 1 segundo entre o processo anterior e o atual, fazendo com que haja um maior congestionamento na hora do escalonador selecionar um processo.

![](plots/workload_busy_plot.png)

A partir da imagem acima fica claro que a duração da maioria dos procesos de prioridade 0 e 1 são maiores que os de prioridade 2, mas os processos de prioridade 3 tem duração maior que os de prioridade 1 e 2, mas ainda são menores que os prioridade 0. 

Novamente o **Round Robin** teve o comportamento esperado distribuindo por igual o tempo de execução dos processos ficando entre 1250 e 1500 segundos.

![](plots/extra_time_busy_rr_plot.png)

Assim como na simulação anterior, tivemos resultados satisfatórios, onde os processos de maior prioridade concluíram sua execução em temos menor, especialmente os processo de prioridade 3, e novamente uma sobreposição entre os resultados dos processos de prioridade 1 e 2.

![](plots/extra_time_busy_pr_plot.png)

Assim como na simulação anterior, a implementação do kernel xv6 causou um maior agrupamento dos resultados, porém no caso de haver uma situação de sobrecarga, houve uma redução inesperada no tempo de execução dos processos de prioridade 1, fato este que é consequência direta do excesso de sorteio, que pode desfavorecer os processos com valor de sorteio tão próximo.

![Xv6 Ocupado](plots/extra_time_busy_xpr_plot.png)

Desta forma, após a coleta dos resultados das simulações podemos concluir que o algoritmo de priorização utilizando o sorteio obteve êxito em reduzir o tempo de execução dos processos com prioridade 3 quando comparado com os demais, contudo o mesmo não pode ser dito quanto aos processos de prioridade 1 e 2 que ficaram com tempo de execução próximo, o que não foi esperado, mas esse comportamento pode ser atribuído a pequena  diferença entre a chance de ambas, que não ultrapassa o valor de 10.
