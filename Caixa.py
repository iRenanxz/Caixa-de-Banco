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