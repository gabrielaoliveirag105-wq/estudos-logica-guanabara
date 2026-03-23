
# 🚀 Meus Estudos de Algoritmos e Lógica

Este repositório contém os exercícios do curso de **Algoritmos** do [Curso em Vídeo](https://cursoemvideo.com), ministrado pelo professor Gustavo Guanabara.

## 🎯 Objetivo
O foco aqui é reforçar a lógica de programação. Para cada exercício proposto em Portugol (Visualg), eu realizo a implementação equivalente em **Python**.

## 📂 Estrutura do Repositório

- `/01-primeiros-passos`: Exercícios sobre entrada, saída e variáveis.
- `/02-condicionais`: Uso de `Se...Então`, `Caso` e operadores lógicos.
- `/03-repeticao`: Estruturas `Enquanto`, `Repita` e `Para`.
- `/04-estruturas-compostas`: Prática com Vetores e Matrizes.


## 🛠️ Ferramentas Utilizadas
- **Visualg 3.0** (Para os arquivos .alg)
- **VS Code** (Para codar em Python)
- **Git & GitHub** (Para controle de versão)

---
*Estudando e evoluindo um `commit` por vez!* 👨‍💻

---

# 🧠 Algoritmo

**-> Algoritmos computacionais:** Sequência de passos a serem seguidos por um módulo processador que sendo seguidos corretamente, realizam determinada tarefa para o usuário.

## 🔍 Conceitos Chave:
*- Módulo processador:* Tudo que é programavel (Celulares, computador, micro-ondas.

*- Usuário:* A pessoa que utilizará o sistema para resolver uma necessidade.  

*- Realizar/Tarefa:* A resolução de um problema real do cotidiano através do código.

## 🛠️ O Caminho da Criação:
*-> Passo para Algoritmos computacionais*

1°. **Lógica de programação:** Organizar o passo a passo mental da solução.

2°. **Linguagem de Programação:** Traduzir a lógica para um código (Python, Java, Go).

3°. **Sistema completo:** O projeto finalizado e funcional entregue ao usuário.

---

##  📝 Detalhamento dos Exercícios 

### 📍 Módulo 01: Primeiros Passos/Entrada-Saída

#### 1. Exercício: Olá Mundo
*O ponto de partida.*

**O Algoritmo (Visualg):**
No *Portugol*, declaramos o início e fim do programa para o interpretador:
```
algoritmo
algoritmo "OlaMundo"
inicio
  escreva("Olá, Mundo")
fimalgoritmo
```

*Em Python o código é direto:*
```
print("Olá, Mundo)
```

#### 2. Usando Variáveis
*Aqui aprendi como o computador armazena e guarda dados/valor temporariamente.*

**O Algoritmo (Visualg):**
```
algoritmo 
var msg: Caractere
msg <- "Olá, Mundo"
escreva("Iniciando...", msg)
```
---

*Em Python fica:*

```
msg = "Olá, Mundo"
print(f"Iniciando... {msg}")
```
---
## ⌨️ Entrada de Dados e Operadores
### 1. Interação com o Usuário
No **Algoritmo**, usamos o `Leia`.
Em **Python**, usamos o `input`.

* *O que acontece no sistema?* Pense no input como o momento em que você "conversa" com a máquina ou insere ingredientes para ela trabalhar.

*Exemplo em Algoritmo:*
```
algoritmo "somar"
Var
  n1:Inteiro
   n2:Inteiro
   soma:Inteiro
Inicio
    escreva("Primeiro valor: ")
    leia(n1) - *usuário interage*
    escreva("Segundo valor: ")
    leia(n2)
    soma <- n1+n2
    escreval("A soma entre ", n1, " e ", n2, " vale: ",soma)
Fimalgoritmo
```
*Exemplo em Python:*
```
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
media = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} vale: {media}')
```





