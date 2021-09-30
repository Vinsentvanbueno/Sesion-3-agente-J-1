from turtle import *

print( 'Visualizar un sector circular')

#Pedir datos
X=float(input('Dame el valor de X en el espacio: '))
Y=float(input('Dame el valor de Y en el espacio: '))
radio=float(input('Dame el radio para el sector circular: '))
angulo=float(input('Dame el ángulo del sector circular: '))

#Crear pantalla y turtle
pantalla=Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)
tortuga=Turtle()

#Dibujar quesito con la tortuga
tortuga.penup()
tortuga.goto(X,Y)
tortuga.pendown()
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,angulo)
tortuga.goto(X,Y)

#Escribir los datos
tortuga.penup()
tortuga.left(-90-angulo)
tortuga.goto(0,-25)
tortuga.write('({0},{1}  Radio={2})'.format(X,Y,radio))

tortuga.goto(30,15)
tortuga.write('Ángulo={0}'.format(angulo))
