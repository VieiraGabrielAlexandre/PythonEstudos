print ("Escrever um algoritmo para determinar o consumo\n"
       "médio de um carro sendo fornecido a distância total\n"
       "total de combustivel gasto. Leve em consideração que o consumo\n"
       "médio é quilometros percorridos/litros gastos.")

litros = input ("Digite a quantidade de litros gastos no percuso : ")
percorrido = input ("Digite o tamanho do percuso : ")
total = litros / percorrido
print ("Consumo médio : {} ".format(total))