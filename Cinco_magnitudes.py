from tabulate import tabulate

print('Bienvenido al programa de regla de tres')
print('Este programa le ayudara a realizar una regla de tres directa, inversa y de cinco magnitudes')
mg = int(input('Ingrese las magnitudes conocidas: '))

matriz = []
ind_incog = 0
tipe_proporcion =[]
datos_con = []
valor_incognita = 0

print('')

for count in range(mg):
    mag_1 = input('Ingrese el nombre de la magnitud: ')

    val_1_pedir = (input('Ingrese el primer valor: '))
    val_1 = float(val_1_pedir)

    val_2 = input('Ingrese el segundo valor o "x" si este es la incognita: ')
    print('')

    if val_2.lower() == 'x':
        ind_incog = count
        val_2 = "x"
        valor_incognita = val_1
    else:
        val_2 = float(val_2)
        tipe = input ("Ingrese el tipo de proporcion Directa (1) o Inversa (2) con respecto a la magnitud que contenga la incognita: ")
        datos_con.append((val_1, val_2, tipe))
        print('')
    
    matriz.append([mag_1, val_1, val_2])

# mostrar la tabla
print('')

print('La matriz de magnitudes y valores es la siguiente: ')
cabeceras = ['Magnitud', 'Valor 1', 'Valor 2']
print(tabulate(matriz, headers=cabeceras , tablefmt='psql'))

#calcular la x 

x = valor_incognita

for val_1, val_2, tipe in datos_con:
    if tipe == '1':
        x = x * (val_2 / val_1)
    else:
        x = x * (val_1 / val_2)

print(f'El valor de la incognita es: {x:.2f}')