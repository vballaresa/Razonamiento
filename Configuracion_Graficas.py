print('Primero vamos a calcular el determinante de una ecuación lineal 2x2')
print('La ecuación tiene la forma:')
print('a*x + b*y = e')
print('c*x + d*y = f')
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))
d = float(input('Ingrese el valor de d: '))
det = (a*d) - (b*c)
if det == 0:
    print('El determinante es cero, el sistema o no tiene solución o tiene infinitas soluciones')
else:
    print(f'Como el determinante es {det}, el sistema tiene una única solución porfavor ingrese las constantes de las ecuaciones')
    e = float(input('Ingrese el valor de e: '))
    f = float(input('Ingrese el valor de f: '))
    y = ((a*f) - (e*c)) / det
    x = ((d*e) - (f*b)) / det
    print(f'El valor de x es: {x}')
    print(f'El valor de y es: {y}')

    # Crear grafica de las ecuaciones lineales

    import matplotlib.pyplot as plt
    import numpy as np

    x_eje = np.linspace(-1000, 1000, 4000)

    y1 = (e - a*x_eje) / b
    y2 = (f - c*x_eje) / d

    plt.plot(x_eje, y1, label='Ecuación 1', color='blue', linestyle='-')
    plt.plot(x_eje, y2, label='Ecuación 2', color='red', linestyle='--')
    plt.scatter(x, y, label='Solución', color='green', s=100, zorder=4)
    plt.title('Gráfica de las ecuaciones lineales 2x2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    plt.show()

input('Presiona enter para salir')




#Vballares_a