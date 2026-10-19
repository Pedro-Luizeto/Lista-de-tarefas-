# Python Task List

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10 ou superior">
  <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" alt="Status: em desenvolvimento">
  <img src="https://img.shields.io/badge/Feito%20com-Aprendizado%20pr%C3%B3prio-2ea44f?style=for-the-badge" alt="Feito com aprendizado próprio">
</p>

## Sobre o projeto

O **Python Task List** é um programa de terminal para adicionar, remover e consultar tarefas pendentes por meio de um menu interativo.

Este projeto faz parte da minha jornada de aprendizado em programação. Foi criado para praticar os fundamentos do Python e desenvolver o raciocínio lógico construindo uma solução própria.

## Objetivos

- Praticar lógica de programação.
- Trabalhar com listas e estruturas de repetição.
- Utilizar condições e `match/case` para controlar as opções do menu.
- Aprimorar a interação com o usuário usando `input()` e `print()`.
- Aprender a percorrer e alterar uma lista.
- Desenvolver autonomia na resolução de problemas.

## Tecnologias utilizadas

- **Python 3.10 ou superior** — necessário para usar `match/case`.
- `while` — mantém o menu ativo até a escolha de sair.
- `match/case` — seleciona a ação escolhida no menu.
- `input()` e `print()` — recebem dados e mostram informações no terminal.
- Lista (`list`) — guarda as tarefas durante a execução.
- `append()` — adiciona uma tarefa à lista.
- `pop()` — remove uma tarefa da lista.
- `enumerate()` — percorre e numera as tarefas a partir de 1.
- `time.sleep()` — faz uma pequena pausa antes da exibição do menu.
- Funções `espaco()` e `linha()` — ajudam a organizar a apresentação.

## Funcionalidades

| Opção | Funcionalidade | Descrição |
|:---:|---|---|
| 01 | Adicionar tarefa | Recebe o texto e adiciona a tarefa à lista. |
| 02 | Remover tarefa | Mostra as tarefas numeradas e remove a escolhida. |
| 03 | Listar tarefas | Exibe todas as tarefas cadastradas. |
| 04 | Tarefas pendentes | Exibe as tarefas que ainda estão na lista. |
| 05 | Sair | Encerra o programa. |

## Como executar

**1.** Certifique-se de ter o Python 3.10 ou superior instalado.

**2.** Salve o código em um arquivo, por exemplo, `tarefas.py`.

**3.** Abra o terminal na pasta em que o arquivo foi salvo.

**4.** Execute o programa:

```bash
python tarefas.py
```

No Windows, você também pode executar:

```powershell
py tarefas.py
```

> **Nota:** troque `tarefas.py` pelo nome real do arquivo, caso tenha usado outro.

## Como funciona a remoção

O programa mostra cada tarefa com uma numeração que começa em 1. Como as posições de uma lista em Python começam em 0, ele subtrai 1 do número escolhido antes de chamar `pop()`:

```python
tarefa_removida = tarefas.pop(indice - 1)
```

Antes de remover, o programa verifica se o número informado corresponde a uma tarefa existente.

## Observação

As tarefas são armazenadas apenas em memória. Isso significa que elas ficam disponíveis enquanto o programa está aberto e são apagadas quando ele é encerrado.

## Próximos passos

- [ ] Tratar entradas inválidas, como letras na opção de remoção.
- [ ] Melhorar a apresentação da lista no terminal.
- [ ] Continuar praticando funções, listas e validação de dados.
- [ ] Evoluir o projeto gradualmente, conforme novos conceitos forem aprendidos.

## Autor

**Pedro Luizeto**

Estudante e programador em formação, aprendendo Python por meio da prática e de projetos próprios.

🔗 **GitHub:** [@Pedro-Luizeto](https://github.com/Pedro-Luizeto)

---

<p align="center">
  Aprendendo, praticando e organizando uma tarefa de cada vez.
</p>
