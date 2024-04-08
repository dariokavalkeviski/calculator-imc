# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para determinar a categoria do IMC
def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso Normal"
    elif imc < 29.9:
        return "Acima do peso"
    elif imc < 39.9:
        return "Obesidade"
    else:
        return "Obesidade grave"

# Solicitar peso e altura do usuário
peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Determinar a categoria do IMC
categoria = categoria_imc(imc)

# Imprimir o IMC e a categoria
print(f"Seu IMC é {imc:.2f}, que é considerado '{categoria}'.")