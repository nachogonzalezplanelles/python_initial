#Condicionale simples y complejas

num_uno = 5
if num_uno == 5:
    print("El numero es cinco")
print("Fin.")

print("Para calcular el promedio de un alumno")
nombre = input("¿Cómo te llamas?: ")
matematicas = float(input("Pues " + nombre + " ¿qué has sacado en mates?: "))
fisica_y_quimica = float(input("Y en F.Q que has sacado " + nombre + ": "))
biología = float(input("Vale, por último, qué has sacado en biología: "))

promedio = (matematicas + fisica_y_quimica + biología) /3

if promedio >= 5:
    print("Felicidades!!!! tu media del curso es: " ,round(promedio,2))
else: 
    print(nombre + ", a repetir el curso con un" ,round(promedio,2)  ,"aprende cacho notas")


num_uno = 10
if num_uno == 5:
    print("El numero es Cinco")
else:
    print("El numero no es Cinco es otro numero")

print("Fin")