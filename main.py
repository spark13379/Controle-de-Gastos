import json
from datetime import datetime

def carregar_gastos():
    try:
        with open('gastos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_gastos(gastos):
    with open('gastos.json', 'w') as arquivo:
        json.dump(gastos, arquivo, indent=4)

def adicionar_gasto(gastos):
    categoria = input("Categoria do gasto: ")
    valor = float(input("Valor do gasto: R$ "))
    descricao = input("Descrição (opcional): ")
    data = datetime.now().strftime('%d/%m/%Y')

    gasto = {
        'categoria': categoria,
        'valor': valor,
        'descricao': descricao,
        'data': data
    }
    gastos.append(gasto)
    salvar_gastos(gastos)
    print("Gasto adicionado com sucesso!\n")

def mostrar_gastos(gastos):
    total = 0
    print("\n--- Lista de Gastos ---")
    for gasto in gastos:
        print(f"{gasto['data']} - {gasto['categoria']} - R$ {gasto['valor']:.2f} - {gasto['descricao']}")
        total += gasto['valor']
    print(f"\nTotal gasto: R$ {total:.2f}\n")

def menu():
    gastos = carregar_gastos()
    while True:
        print("1. Adicionar gasto")
        print("2. Ver gastos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_gasto(gastos)
        elif opcao == '2':
            mostrar_gastos(gastos)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
