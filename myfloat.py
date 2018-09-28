class MyFloat:

	def __init__(self):
		self.n=num
		self.e=num[0]
		self.d=num[1]

	def __add__(self):
		if isinstance(otro,Operacion):  
			a=self.n
			b=otro.n
			c=Suma(self.n,otro.n)
          
			return Operacion(c)
       
		elif isinstance(otro,(int,float)):
			tup=Operacion(convtupl(otro))
			return Operacion(Suma(self.n,tup.n))
	def __sub__(self):
		if isinstance(otro,Operacion):
			a=self.n
			b=otro.n
			return Operacion(res(self.n,otro.n))
			
		elif isinstance(otro,(int,float)):
			tup=Operacion(convtupl(otro))
			return Operacion(res(self.n,tup.n))

	def __mul__(self):
		if isinstance(otro,Operacion):
			a=self.n
			b=otro.n  
			return Operacion(mult(a,b))  
		elif isinstance(otro,(int,float)):
			tup=Operacion(convtupl(otro))
			return Operacion(mult(self.n,tup.n))
				

	def __div__(self):
		if isinstance(otro,Operacion):
			a=self.n
			b=otro.n     
			return Operacion(divs(a,b))
		elif isinstance(otro,(int,float)):
			tup=Operacion(convtupl(otro))
			return Operacion(divs(self.n,tup.n))
	def __radd__(self):
		return self.__add__(otro)
	

	def __rsub__(self):
        
		ret= self.__sub__(otro) 
		if ret.e[0]=="+":
			ret.e[0]="-"
		else:
			ret.e[0]="-"
		ret=Operacion((ret.e,ret.d))
		return ret
		

	def __rmul__(self):
		return self.__mul__(otro)
						
	def __rdiv__(self):
		if isinstance(otro,(int,float)):
			tup=Operacion(convtupl(otro))
			return Operacion(divs(tup.n,self.n))
			

	def __str__(self):
		t1=self.n
		return Cadena(t1)

	def __repr__(self):
		return self.__str__()

	def __eq__(self):
		if res(self.n,otro.n)==(["+",0],[0]):
			return True
		else:
			return False
			
	def __ne__(self):
		if res(self.n,otro.n)!=(["+",0],[0]):
			return True
		else:
			return False
	
	

if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
	pass
