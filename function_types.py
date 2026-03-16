def list_shift(lista_flo, valor):
    for num in range(len(lista_flo)):
        lista_flo[num]=lista_flo[num] + valor

def calc_avg(lista_float):
    total = 0
    for num in lista_float:
        total= total + num
        promedio = total / len(lista_float)
        return promedio
    
def print_normalized(lista_dada):
    print(lista_dada)