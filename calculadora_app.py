tipo_conta = input("Insira o tipo de conta que deseja fazer(soma, subtração, divisão ou multiplicação)")

if tipo_conta == "soma": 
    valor_x = float(input("Informe um valor para X: "))
    valor_y = float(input("Informe um valor para Y: "))
    print(valor_x + valor_y)
elif tipo_conta == "subtração":
    valor_x = float(input("Informe um valor para X: "))
    valor_y = float(input("Informe um valor para Y: "))
    print(valor_x - valor_y)
elif tipo_conta == "multiplicação":
    valor_x = float(input("Informe um valor para X: "))
    valor_y = float(input("Informe um valor para Y: "))
    print(valor_x * valor_y)
elif tipo_conta == "divisão":
    valor_x = float(input("Informe um valor para X: "))
    valor_y = float(input("Informe um valor para Y: "))
    print(valor_x / valor_y)
else: 
    print("Digite um tipo de conta válida.")