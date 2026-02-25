from Ejercicios.ejercicio1 import ejercicio_1
from Ejercicios.ejercicio2 import ejercicio_2
from Ejercicios.ejercicio3 import ejercicio_3 
from Ejercicios.ejercicio4 import ejercicio_4
#referenciar la clase
from poo.clases.ejer1poo import ejercicio1
 #carpeta carpeta carpeta       clase
 
def menuPrincipal():
    while True:
        print("\n::Menú::")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")
       
        op = int(input("Ingrese la opcion deseada: "))
        match(op):
            case 1:
                #Llamada a la funcion
                #ejercicio_1()
                
                #crear el objeto de la clase
                e1 = ejercicio1 ()
                #Llamada a los metodos 
                e1.leerDatos()
                e1.calcularAprox()
                e1.mostrarResultados()
                
            
            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4()
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Ingrese un dato válido")