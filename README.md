# parcial-ds2-RojasCaicedo-Bautista
 Juan Esteban Rojas Caicedo 20221204189
 Daniel Santiago Bautista Contreras 20221205218


#  bd
 HuilaSoft

# coleccion
usuarios:
    - Nombre: texto
    - cargo: texto
Ticket
    -id: texto
    -llegada: numerico
    -atencion: numerico
    -prioridad: texto
defectos
    -semana: numerico
    -defectos_encontrados: numerico 



# Ejercicio
    escogimos el ejercicio b


# Interpretacion
    Al ajustar el modelo de Goel-Okumoto a los defectos acumulados de las ocho semanas de pruebas obtivimos a = 198,1 y b = 0,152. Esto significa que la versión 11.0 tendría cerca de 198 defectos en total de los cuales ya se han encontrado 139, si se libera hoy quedarían aproximadamente 59 defectos sin descubrir.
    Siguiendo el modelo, el 95 % de los defectos se alcanzaría en la semana 19,7 (t = ln 20 / b) o sea, unas 12 semanas más de pruebas.
    En la gráfica vemos que la curva ajustada pasa muy cerca de los puntos reales, tambien que en la semana 8 todavía sigue subiendo sin aplanarse, aunque cada semana se encuentran menos defectos. Por eso recomendamos a HuilaSoft no liberar la versión 11.0 todavía, deberían continuar las pruebas hasta superar el 95 % de defectos encontrados y priorizar la corrección de los defectos críticos.