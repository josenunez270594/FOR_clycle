'''
un agricultor realiza la siembra de 3 cultivos papa, yuca y zanahoria; el cultivo de papa requiere una cantidad X de riego a la semana, la yuca y la zanahoria tambien. consultar en internet dicho procedimiento y establecer esta caracteristica en el programa.
LITROS
'''
print('bienvenido a la granja feliz')
tipo_cultivo = int(input('que tipo de cultivo desea regar: \n1) papa \n2) yuca \n3) zanahoria \n'))
total = 0
if tipo_cultivo == 1:
    print('la papa por lo general se riega en un promedio de 3 veces por semana:')
    for i in range(3):
        litros = int(input('litros a regar:')) 
        total += litros
    print(f'el total de litros esta semana son: {total}')
elif tipo_cultivo == 2:
    print('la yuca por lo general se riega en un promedio de 2 veces por semana:')
    for i in range(2):
        litros = int(input('litros a regar:')) 
        total += litros
    print(f'el total de litros esta semana son: {total}')
elif tipo_cultivo == 3:
    print('la zanahoria por lo general se riega en un promedio de 2 veces por semana:')
    for i in range(2):
        litros = int(input('litros a regar:')) 
        total += litros
    print(f'el total de litros esta semana son: {total}')
