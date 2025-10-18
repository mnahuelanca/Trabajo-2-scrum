# Motor de encadenamiento hacia adelante
# Diagnóstico de fallas en un automóvil

# Base de conocimiento
reglas = [
    {"si": ["batería descargada"], "entonces": "auto no enciende"},
    {"si": ["sin combustible"], "entonces": "auto no enciende"},
    {"si": ["auto no enciende"], "entonces": "necesita revisión"}
]

# Solicitar hechos iniciales
hechos = input("Ingrese hechos iniciales separados por coma: ").lower().split(",")

# Limpieza de espacios
hechos = [h.strip() for h in hechos]

nuevos_hechos = True
paso = 1

while nuevos_hechos:
    nuevos_hechos = False
    print(f"\n--- Paso {paso} ---")
    paso += 1

    for regla in reglas:
        # Si todos los hechos de la condición se cumplen
        if all(cond in hechos for cond in regla["si"]):
            conclusion = regla["entonces"]
            # Si la conclusión es nueva, se agrega
            if conclusion not in hechos:
                hechos.append(conclusion)
                nuevos_hechos = True
                print(f"Se cumple la regla: SI {regla['si']} ENTONCES {conclusion}")
                print(f"➡ Nuevo hecho generado: {conclusion}")

print("\n--- Razonamiento finalizado ---")
print("Hechos conocidos:", hechos)
