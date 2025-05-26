# 🤖 Cire - Assistente Virtual com Voz

Cire é uma assistente virtual escrita em Python que responde por comandos de texto e fala com você usando voz feminina. Ela pode criar pastas e arquivos, abrir programas, limpar a lixeira e muito mais.

## 🧠 Comandos Disponíveis

Use o nome "cire" antes do comando, por exemplo: `cire criar pasta`.

| Comando                | Ação                                                                 |
|------------------------|----------------------------------------------------------------------|
| `cire ajuda`           | Mostra todos os comandos disponíveis                                 |
| `cire criar pasta`     | Pergunta onde deseja criar e o nome da pasta                         |
| `cire criar arquivo`   | Cria um arquivo `.py` na pasta desejada                              |
| `cire abrir navegador` | Abre o navegador e acessa `google.com.br`                            |
| `cire abrir yt`        | Abre o YouTube no navegador                                          |
| `cire abrir pasta`     | Pergunta o nome da pasta e a abre                                    |
| `cire abrir [nome]`    | Tenta abrir um programa, jogo ou arquivo pelo nome                   |
| `cire pesquisa [texto]`| Abre o navegador e pesquisa o texto fornecido                        |
| `cire esvaziar lixeira`| Esvazia a lixeira do Windows                                         |
| `cire sair`            | Encerra a assistente com uma mensagem final                          |

## 🛠 Instalação

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
