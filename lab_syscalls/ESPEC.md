# Laboratório 1 - Systemcalls

## Objetivo
Se familiarizar com o modelo de programação UNIX que implementa a abstração de processo. Para isso, o aluno desenvolverá um shell.

## Métodos
gcc e make para a compilação do código fonte do shell
código fonte xeu.c (lab_syscalls)
use este programa como base para o seu shell. Para compilar o programa, digite `make xeu`.
use a função readline definida em xeu.c para fazer o prompt com o usuário.
Uma vez compilado, para executar o seu shell, abra um outro shell (p.ex o gnome-terminal) e execute ./xeu.
As funções utilitárias em [link](https://github.com/thiagomanel/labSO/tree/master/lab_syscalls/xeu_utils).

## Forma de envio e avaliação
Ao fim da última parte do laboratório, envie uma nova versão do código fonte xeu.c que implementa os requisitos definidos. Mantenha seu código em um repositório privado, p.ex no github (ou no bitbucket).

## Roteiro

### Parte1
Seu shell foi feito para executar programas. Modifique o código base de maneira que seja possível executar programas com ou sem argumentos. Somente um programa pode ser especificado pelo usuário por cada vez. O usuário poderá dar entrada a um novo programa no prompt após o fim da execução do programa anterior. A saída dos programas, quando houver, deverá ser feita na saída padrão. Dois programas possíveis seriam:

```
| ~ @ Thiagos-MacBook-Pro (manel)
| =>  date
Sex 18 Nov 2016 16:36:43 BRT

| ~ @ Thiagos-MacBook-Pro (manel)
| =>  sleep 5
```

Para processar os argumentos, use o código utilitário da seguinte forma (note que há outros métodos úteis, leiam a API):

Declare os tipos necessários
```
vector<Command> commands;
ParsingState p;
Command c;
```

Leia a entrada padrão

```
p = StreamParser().parse();
```
E processe os comandos lidos
```
commands = p.commands();
for (i = 0; i < commands.size(); i++) {
            c = commands[i];
            int code;
            if (!strcmp(c.filename(), "xpto")) { }
}
```
### Parte2
Quem não se comunica … Pipes são bastante usados interprocess communication (IPC) no shell. Até agora seu shell não dá suporte a pipes (p.ex tente executar `ps xau | grep root`). Nessa parte do laboratório, você precisará implementar o suporte a pipes. Deve ser possível usar um número arbitrário de pipes.

### Parte3 (LabSO UFMG - EXTRA)
Redirecionamento de entrada/saída
Implemente comandos com redirecionamento de entrada e saída para que você possa rodar:
```
$ echo "FOO" > baa.txt
$ cat < baa.txt
```
Referências
[fork](https://linux.die.net/man/2/fork), 
[execve](https://linux.die.net/man/2/execve), 
[wait](https://linux.die.net/man/2/wait), 
[exit](https://linux.die.net/man/2/exit),
[pipe](https://linux.die.net/man/2/pipe). 

P.S Obrigado a Rafael Perrella (https://github.com/rafaelclp) pelo suporte no ao xeu.
