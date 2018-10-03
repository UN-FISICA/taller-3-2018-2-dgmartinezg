# taller-3-2018-2


Este trabajo consiste en unprograma que utilizas las clases para definir las operaciones de multiplicacion, división, suma y resta para operar en una tupla de listas. 
La tupla es de dos listas una con la parte entera y la otra con la parte decimal.
Para definir las operaciones con sus respectivos simbolos se utilizo la clase MyFloat donde esta definidas las operaciones
__div__, __add__, __sub__,__mul__.
En el archivo MyFloat.py esta todo las definiciones y la clase MyFloat, tambien se encuentra el programa que utiliza las definiciones de las operaciones para las tuplas para cualcular el numero Pi.

Para operar las tupla, lo que hice fue defnir las operaciones componente a componente entre las listas de cada tupla
Para efectuar las suma de dos tupla hace falta hacer lo siguiente:
~~
a=MyFloat([5,5,6],[5,5,6])
b=MyFloat([a,7,6],[5,8,9])
~~
Esto lo que hace es convertir las tuplas a la forma en la cual se va a operar, seguido esto se puede entonces hacer cualquier operacion entre a y b
~~
a*b
a/b
a+b
a-b
~~

Despues con estas operaciones defnindas para las tuplas de listas
se procedio a calcular pi con estas operaciones



~~




calculo de pi 
	Pie2=MyFloat(([0],[0]))
	Tupla1=MyFloat(([1],[0]))
	Tupla2=MyFloat(([2],[0]))
	a=([1],[0])
	b=([2],[0])
	imprimir(a)
	imprimir(b)
	h=(res(a,b))
	print (h)
	print(Tupla1+Tupla2)
	print(Tupla1-Tupla2	)	
	for l in range(0,55):
		
		ka=[l]
		Tuplak=MyFloat((ka,[0]))
		dk=Tupla2*Tuplak
		dkm1=dk+Tupla1
		usdkm1=Tupla1/dkm1
		h=ka[0]
		if h % 2 ==0:
			Pie2=Pie2+usdkm1
		#else:
		#	Pie2=Pie2-usdkm1
  resturn Pie
  

~~
