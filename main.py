
# Cronograma simple del plan de 100 minutos

tareas = [
    ("A", "Identificar servidores", "08:00", "08:15"),
    ("B", "Priorizar datos críticos", "08:15", "08:35"),
    ("C", "Activar protocolo", "08:15", "08:25"),
    ("D", "Asignar técnicos", "08:25", "08:30"),
    ("E", "Recuperar servidor 1", "08:30", "09:00"),
    ("G", "Validar datos Srv1", "09:00", "09:15"),
    ("F", "Recuperar servidor 2", "09:00", "09:25"),
    ("H", "Informe dirección", "09:15", "09:25"),
    ("I", "Comunicar clientes", "09:15", "09:35"),
    ("J", "Coordinar legal", "09:15", "09:30"),
    ("K", "Plan de contingencia", "09:15", "09:40"),
]

print("Cronograma del plan (100 minutos):")
print("-" * 50)
for t in tareas:
    print(f"{t[0]} - {t[1]} | {t[2]} a {t[3]}")
print("-" * 50)
print("Fin del plan: 09:40 (100 minutos desde 08:00)")
