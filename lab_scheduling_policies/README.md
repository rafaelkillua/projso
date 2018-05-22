# Especificação do Algoritmo de Escalonamento - Lab 02

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
