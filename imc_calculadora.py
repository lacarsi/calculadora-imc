altura = input("Insira a sua altura: ")
peso = input("Insira o seu peso: ")

peso_as_int = int(peso)
altura_as_float = float(altura)

# Using the exponent operator **
imc = peso_as_int / altura_as_float ** 2
# or using multiplication and PEMDAS
#imc = peso_as_int / (altura_as_float * altura_as_float)

imc_as_int = int(imc)

print("IMC: " + str(imc_as_int))