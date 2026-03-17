from utils import flip, count_letters
mensaje =input("Please type your message\n")
mensajeINvertido =flip(mensaje)
numeroDe_a = count_letters(mensaje, "a")
mensaje_codificado = (mensajeINvertido + str(numeroDe_a))
print(f"Your encoded message is:",{mensaje_codificado})