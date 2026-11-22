import json
from modelo import CampanaPruebas

# los datos los saque de mongo con mongoexport --jsonArray
archivo = open("mongo/evidencias/datos_defectos.json", encoding="utf-8")
datos = json.load(archivo)
archivo.close()

# saco solo el numero de defectos de cada semana
defectos = []
for semana in datos:
    defectos.append(semana["defectos_encontrados"])

campana = CampanaPruebas(defectos)
print("acumulados:", campana.acumulados)

a, b = campana.ajustar()
print("a:", round(a, 1))
print("b:", round(b, 4))

print("restantes:", round(campana.restantes(), 1))
print("semana 95%:", round(campana.semana_95(), 1))

campana.graficar()
