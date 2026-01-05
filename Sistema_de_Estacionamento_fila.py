from collections import deque

estacionamento = deque()

def menu():
    print("\n=== Sistema de Estacionamento ===")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Visualizar estacionamento")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Digite a placa do veículo: ")
        estacionamento.append(placa)
        print(f"Veículo {placa} entrou no estacionamento.")

    elif opcao == "2":
        if estacionamento:
            veiculo = estacionamento.popleft()
            print(f"Veículo {veiculo} saiu do estacionamento.")
        else:
            print("Estacionamento vazio.")

    elif opcao == "3":
        if estacionamento:
            print("\nVeículos no estacionamento:")
            for v in estacionamento:
                print(v)
        else:
            print("Estacionamento vazio.")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
