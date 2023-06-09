"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO
if esta_lloviendo ==  True or riego_activado == True:
    print("El piso esta mojado")
# COMPLETAR - FIN

#assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
resultado = not(area_cuadrado < lado_cuadrado)
print(resultado)
# COMPLETAR - FIN

#assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
resultado = not(bool(numero_1 //7)) + bool(numero_2 // 2)
print(resultado)
# COMPLETAR - FIN

#assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO

resultado = variable_01 or variable_02 or not variable_04 or (variable_05 and variable_03)
if resultado:
    resultado = 80
print(resultado)

#print(resultado)
# COMPLETAR - FIN

#assert resultado == 80