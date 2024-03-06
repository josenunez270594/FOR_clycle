'''
un tirista realiza un viaje de un punto a A un punto B, dentro del rango del punto A al punto B debe realizar varias escalas, las cuales dependen de el realizar; diseñe un algoritmo que permita ingresar la CANTIDAD de ESCALAS dentro de las cuales el turista debe ingresar la distancia a recorrer e ir sumando cada una. al final decir: cuantas distancias y etapas realizo
'''

total=0
print('se realizara una carrera de un punto A a un punto B')
etapas = int(input('ingrese las etapas a realizar: '))
for i in range(etapas):
   km = int(input('kilometros recorridos en la etapa realizada: '))
   total += km 
print(f'los kilometros recorridos son: {total}\nlas etapas realizadas son: {etapas}')


