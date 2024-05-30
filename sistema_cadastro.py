#funções: adicionar- deletar- pesquisar
#Detalhes: nome- numero de sereal- data de entrada/saida- setor


inventario = {}
while True:
     opcao = int(input("""Digite:
                       1 para adicinar
                       2 persistir no arquivo
                       3 para exibir maquina
                       4 para excluir
                       5 para sair"""))
     if opcao == 1:
          resposta = "S"
          while resposta =="S":
               numero_sereal = input("SEREAL: ")
               data_Entrada = input("Digite a data de entrada: ")
               nome = input("Nome do equipamento: ")
               departamento = input("DEPARTAMENTO: ")

               inventario[numero_sereal] = [data_Entrada, nome, departamento]
               resposta = input("DIgite 'S' para continuar: ").upper()


     elif opcao == 2:
          with open("Inventario.csv", "a") as inv:
               for chave, valor, in inventario.items():
                    inv.write(chave + ";" + valor [0] + ";" +
                              valor [1] + ":" + valor [2] + "\n")
                    print("Persistindo com sucesso")


     elif opcao == 3:
          with open("Inventario.cvs", "r") as inv:
               print(inv.readlines()) 


     #elif opcao == 4:
         # os.remove() inventario[numero_sereal, data_Entrada, nome, departamento]
          #print("** Arquivo deletado com sucesso **")


     elif opcao == 5:
          break
     else:
          print("** Opcao invalida **")     
   #erros na linha 39
   #erros para adicionar no inventario 