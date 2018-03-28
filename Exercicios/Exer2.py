print ("Escrever um algoritmo para solicitar ao\n"
       "usuario que informe o nome, a altura e o\n"
       "peso. Após isso calcule qual o IMC deste\n"
       "usuário (peso/altura²). Ao final dos \n"
       "cálculos, mostre para o usuario qual o seu IMC")

nome = input("Digite seu nome: ")
altura = float (input("Agora digite sua altura: "))
peso = float (input("Agora o peso: "))
IMC = peso * (altura * 2)

print(nome, "seu IMC é ", IMC)
