pilha_livros = []

def menu():
    print("\n=== Sistema de Empilhamento de Livros ===")
    print("1 - Empilhar livro")
    print("2 - Desempilhar livro")
    print("3 - Visualizar pilha")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livro = input("Digite o nome do livro: ")
        pilha_livros.append(livro)
        print(f"Livro '{livro}' foi empilhado.")

    elif opcao == "2":
        if pilha_livros:
            livro = pilha_livros.pop()
            print(f"Livro '{livro}' foi removido da pilha.")
        else:
            print("Pilha vazia.")

    elif opcao == "3":
        if pilha_livros:
            print("\nPilha de livros:")
            for livro in reversed(pilha_livros):
                print(livro)
        else:
            print("Pilha vazia.")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
