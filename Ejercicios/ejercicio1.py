import math
 
def leerDatos():
  x = float(input("x="))
  tolerancia = float(input("Tolerancia="))
  return x,tolerancia
 
def calcularAprox(x,tolerancia):
  valorReal = math.sin(x)
  k = 0
  aprox = 0
  while True:
    aprox += ((-1)**k*x**(2*k+1))/math.factorial(2*k+1)
    k += 1
    error = math.fabs((valorReal - aprox)/valorReal) * 100
    if error < tolerancia:
      break
  return valorReal,aprox,error
 
def mostrarResultados(valorReal,aprox,error):
  print("Valor Real = ",valorReal)
  print("Aproximacion = ",aprox)
  print("Error = ",error)
 
def ejercicio_1():
 x,tolerancia = leerDatos()
 valorReal,aprox,error = calcularAprox(x,tolerancia)
 mostrarResultados(valorReal,aprox,error)