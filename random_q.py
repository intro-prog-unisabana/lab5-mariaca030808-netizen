import random
inicio_valor= int(input("Enter the start value:\n"))
final_valor = int(input("Enter the end value:\n"))
randomnum = random.randint(inicio_valor, final_valor)

print(f"Generated random number: {randomnum}")