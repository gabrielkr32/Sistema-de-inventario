#funções: adicionar- deletar- pesquisar
#Detalhes: nome- numero de sereal- data de entrada/saida- setor


inventario = [] 
nome = input("Nome do Equipamento: ") # pede o nome do item
inventario.append(nome) #adicona o nome da lista
print(inventario)

numero_serie = int(input("Numero de sereal: ")) #entrada de numero
inventario.append(numero_serie) #adiciona o numero sereal
print(inventario)

data_entrada = (input("Data de entrada: ")) #Data de entrada do objeto
inventario.append(data_entrada) # // data
print(inventario)

setor = input("Setor de destino: ")#Nome do setor
inventario.append(setor)# // setor
print(inventario)
