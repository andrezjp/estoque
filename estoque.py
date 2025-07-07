def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()
    if nome in estoque:
        print("Produto já existe no estoque.")
        return
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: Quantidade deve ser um número inteiro e preço um número decimal.")


def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio.")
        return

    print("\nProdutos no estoque:")
    for nome in sorted(estoque, key=lambda x: x.lower()):
        info = estoque[nome]
        print(f"{nome}: {info['quantidade']} disponível - R$ {info['preço']:.2f}")
    print()


def remover_produto(estoque):
    nome = input("Nome do produto a remover: ").strip()
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso.")
    else:
        print("Erro: Produto não encontrado.")


def atualizar_quantidade(estoque):
    nome = input("Nome do produto: ").strip()
    if nome in estoque:
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            estoque[nome]["quantidade"] = nova_quantidade
            print("Quantidade atualizada com sucesso.")
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")
    else:
        print("Erro: Produto não encontrado.")


def exibir_menu():
    print("\n--- Menu de Estoque ---")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")


def main():
    estoque = {}

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-5): ").strip()

        if escolha == "1":
            adicionar_produto(estoque)
        elif escolha == "2":
            listar_produtos(estoque)
        elif escolha == "3":
            remover_produto(estoque)
        elif escolha == "4":
            atualizar_quantidade(estoque)
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
