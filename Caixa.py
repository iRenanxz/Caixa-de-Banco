saldo = 0.0

def deposito(valor):
    global saldo
    saldo += valor
    if valor <= 0:
        print("Valor de depósito inválido. O valor deve ser maior que zero.")
    else:
        print(f"Dpósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}")

def saque(valor):
    global saldo
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor <= 0:
        print("Valor de saque inválido")
    else:
        saldo -=valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}")

def consultar_saldo():
    print(f"Saldo atual: R${saldo:.2f}")

def menu():
    while True:
        print("\n=== Menu ===".center(30))
        print("1. Depósito")
        print("2. Saque")
        print("3. Consultar Saldo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            valor = float(input("Digite um valor para depósito: "))
            deposito(valor)

        elif opcao == "2":
            valor = float(input("Digite um valor para saque: "))
            saque(valor)
        elif opcao == "3":
            consultar_saldo()
        elif opcao == "4":
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    menu()