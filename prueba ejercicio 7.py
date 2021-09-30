from turtle import *

print( 'Visualizar un diagrama de pastel coroleado basandose en tus notas de una asignatura')

#Pedir los datos
sus=int(input('Numero de sus: '))
apr=int(input('Numero de apr: '))
notables=int(input('Numero de notables: '))
sobresalientes=int(input('Numero de sobresalientes: '))
radio=100

#calculo de porcentajes y angulos
t=sus+apr+notables+sobresalientes


por_suspensos=100*suspensos//total
por_aprobados=100*aprobados//total
por_notables=100*notables//total
por_sobresalientes=100*sobresalientes//total

angulosuspensos=360*por_suspensos//100
anguloaprobados=360*por_aprobados//100
angulonotables=360*por_notables//100
angulosobresalientes=360*por_sobresalientes//100



#Crear pantalla y turtle
pantalla=Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)
tortuga=Turtle()
tortuga.pensize(2)

#Dibujo de sus
tortuga.pendown()
tortuga.pencolor('Red')
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,angulosus)
tortuga.penup()
tortuga.home()

#Dibujo de apr
tortuga.pencolor('yellow')
tortuga.pendown()
tortuga.left(angulosus)
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,anguloapr)
tortuga.penup()
tortuga.home()

#Dibujo de notables
tortuga.pencolor('green')
tortuga.pendown()
tortuga.left(angulonotables)
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,angulonotables)
tortuga.penup()
tortuga.home()

#Dibujo de sobresalientes
tortuga.pencolor('black')
tortuga.pendown()
tortuga.right(angulosobresalientes)
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,angulosobresalientes)
tortuga.penup()
tortuga.home()

#Escribir los datos en el lado
tortuga.pencolor('red')
tortuga.goto(110,50)
tortuga.write('sus:{0}'.format(round(por_sus,2)))
tortuga.goto(110,25)
tortuga.pencolor('yellow')
tortuga.write('apr:{0}'.format(round(por_apr,2)))
tortuga.goto(110,0)
tortuga.pencolor('green')
tortuga.write('Notables:{0}'.format(round(por_notables,2)))
tortuga.goto(110,-25)
tortuga.pencolor('black')
tortuga.write('Sobresalientes:{0}'.format(round(por_sobresalientes,2)))
