import os
import math

directorio = os.getcwd()
print(f"Current working directory: {directorio}")
num = int(input("Enter an integer: "))
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")
floor_val = math.floor(log_val)
ceil_val = math.ceil(log_val)

print(f"Floor: {floor_val}")
print(f"Ceiling: {ceil_val}")