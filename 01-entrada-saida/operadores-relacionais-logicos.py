# --- ALGORITMO (Visualg) ---
# algoritmo "Par"
# var 
#    num: inteiro
#    par: logicos
# inicio
#    escreva("Informe um número: ")
#    leia(num)
#    par <- num % 2 = 0
#    escreva("O número ", num, " é par: ")
# fimalgoritmo

# --- CÓDIGO EM PYTHON ---
num = int(input("Informe um número: "))
par = (num % 2 == 0)

print(f'O número {num} é par? {par}')

# --- COMO ISSO AGE NO SISTEMA? ---
# 1. Conversão de Tipo (int): O 'input' sempre recebe TEXTO. O 'int()' 
#    avisa ao processador para tratar os sinais do teclado como NÚMEROS.
# 2. Operador de Resto (%): O sistema divide o número por 2 e olha 
#    apenas para o que sobrou. Se sobrar 0, o número é par.
# 3. Comparação (==): O processador compara o resto com zero. 
#    Diferente do '=', o '==' não guarda valor, ele faz uma PERGUNTA.
# 4. Tipo Booleano: O resultado dessa pergunta gera um bit (0 ou 1) 
#    que o Python traduz como 'True' (Verdadeiro) ou 'False' (Falso).
