# --- ALGORITMO (Visualg) ---
# var nome: caractere
# inicio
#    Escreva("Qual é o seu nome? ")
#    Leia(nome)
#    Escreva("Muito prazer, ", nome)
# fimalgoritmo

# --- CÓDIGO EM PYTHON ---
nome = input("Qual é o seu nome? ")
print(f"Muito prazer, {nome}!")

# --- COMO ISSO AGE NO SISTEMA? ---
# 1. O comando 'input' envia uma interrupção ao processador.
# 2. O computador PAUSA a execução e fica vigiando o teclado.
# 3. Quando você digita e aperta 'Enter', os sinais elétricos do teclado 
#    são convertidos em texto e guardados na RAM, no endereço chamado 'nome'.
# 4. O 'f' no print (f-string) serve para o sistema buscar esse valor na RAM 
#    e "colar" ele dentro da frase antes de mandar para o monitor.
