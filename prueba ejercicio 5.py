print('Programa para calcular la tasa anual equivalente al interés de un préstamo')

ik=float(input('Dame el interés nominal: '))
m=float(input('Número de meses: '))

k=m*12
Mk=1+ik/(100*k)
TAE=100*(Mk**k-1)
TAE=round (TAE,2)

print('El TAE es: ',TAE)
