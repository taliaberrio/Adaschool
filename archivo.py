# Define una variable de cada tipo de primitivo
edad = 26
estatura = 1.66
mujer = True
cadena = "str"

# concatena a la cadena de otras variables aplicando la conversión correcta pa funcionar, guarda el resultado en una variable
concatena = cadena + " " + str(edad) + " " + str(estatura) + " " + str(mujer)
print (concatena) 

# Investiga sobre el límite de los enteros y los flotantes en python
# Los enteros en Python 3 son de presición ilimitada, pero depende de la memoria disponible
# Los flotantes en Python utilizan el estandar IEE 754, que tiene limites:
# Mínimo valor positivo: 2.2250738585072014e-308
# Máximo valor positivo: 1.7976931348623157e+308
# Precisión de aproximadamente 15- 17 dígitos decimales

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20
resultado = 0
for i in range (2,n+1,2):
    resultado += i
print (resultado)
