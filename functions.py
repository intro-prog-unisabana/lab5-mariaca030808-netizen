def promedio_estudiante(calificaciones):

    if len(calificaciones)== 0:
        return 0.0 
    total = 0 
    for calificación in calificaciones:
        total = total + calificación
    promedio_total= total/ len(calificaciones)
    return float(promedio_total)

print(promedio_estudiante(calificaciones))