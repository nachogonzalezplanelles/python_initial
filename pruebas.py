#Condicionales
print("Para calcular el promedio de un alumno")
nombre = input("¿Cómo te llamas?: ")

matematicas = float(input("\nPues " + nombre + " ¿qué has sacado en mates?: "))
fisica_y_quimica = float(input("Y en F.Q que has sacado " + nombre + ": "))
biología = float(input("Vale, por último, qué has sacado en biología: "))

promedio = (matematicas + fisica_y_quimica + biología) /3

if promedio >= 5:
    print("\nFelicidades!!!! tu media del curso es: " , round(promedio,2))
else: 
    print(nombre + "\n ,a repetir el curso aprende cacho notas" , round(promedio,2))


#Practica sentencias condicionales
nombre = input("\n¿Oye tu como t llamas?: ")
eleccion = int(input(nombre + " elige un nro ¿1 o 2?: "))

if eleccion == 1:
    print("\n" + nombre + "tenias un 50 50 y has elegido el malo, si que hay que tener suerte")
    print("El nro que has elegido era para saber que......")
    eleccion_2 = int(input(nombre + " pulsa -1- : "))
    if eleccion_2 == 1:
        print("\nLa noticia tan lamentable es q M TIENES QUE DAR UN PC")
    else:
        print("\nPq eres tan retrasao d q si pone -1- le das a otro nro??")
elif eleccion == 2: 
    print("Te ha tocado el nro bno pro desafortunadamente.....")
    eleccion_3 = int(input(nombre + " pulsa el nro -5- : "))
    if  eleccion_3 == 5:
        print("\n" + nombre + "la noticia es... QUE ME TIENES QUE COMPRAR UN IPHONE") 
    else: 
        print("\nTu eres tonto o q t pasa t he dicho que pulses el nro -5- ")   
else:
    print("\nPORQUE LE DAS A OTRO NRO DEL Q T PIDEEEEEEN")
 