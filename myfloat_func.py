#!/usr/bin/python
# -*- coding: utf8 -*-
from pylab import *
import math as m

def imprimir(a):
    e,d=a
    r=""
    for i in range(len(e)):
        r=r+str(e[i])
    r=r[::1]
    r=r+","
    
    for i in d:
        r=r+str(i)
        
    
    print (r)
    return r

def Sum(x,y):
	a=x[::-1]
	b=y[::-1]
	nd=max(len(a),len(b))
	red=0
	rs=[]
	for i in range(nd):
		na=0 if i>=len(a) else a[i]
		nb=0 if i>=len(b) else b[i]
		s=na+nb+red
		red=0 if s<10 else 1
		rs.append(s%10)
	if red==1:
		rs.append(1)
	rs.reverse()
	return rs


def Suma(x,y):
	a=x[1][::]
	b=y[1][::]
	c=x[0][::-1]
	d=y[0][::-1]
	nd=max(len(a),len(b))
	red=0
	rs=[]
	for i in range(nd-1,-1,-1):
		if i>=len(a):
			na=0
		else:
			na=a[i]
		if i>=len(b):
			nb=0
		else:
			nb=b[i]
		s=na+nb+red
		if s<10:
			red=0
		else:
			red=1
			rs.append(s%10)
		rs.reverse()
		
		nmax=max(len(c),len(d))
		
		rent=[]
		
		for j in range(nmax):
			if j>=len(c):
				na=0
			else:
				na=c[j]
			if j>=len(d):
				nb=0
			else:
				nb=d[j]
			s2=na+nb+red
			if s2<10:
				red=0
			else:
				red=1
			rent.append(s2%10)
		if red==1:
			rent.append(1)
		rent.reverse()
	return rent,rs 



def resta(a, b):
	me=[0]+b[0]
	md=[1]+b[1]
	me.pop(0)
	md.pop(0)
	m=me,md
	le=[0]+a[0]
	ld=[1]+a[1]
	le.pop(0)
	ld.pop(0)
	l=le,ld
	
	ea,da=l
	eb,db=m
	
	ea.reverse()
	eb.reverse()
	
	
	if len(ea)<len(eb):         #Igualando los tamaños de la parte entera
		for i in range(len(eb)-len(ea)):
			ea.append(0)
	elif len(eb)<len(ea):
		for i in range(len(ea)-len(eb)):
			eb.append(0)
	if len(da)<len(db):         #Igualando los tamaños de la parte decimal
		for i in range(len(db)-len(da)):
			da.append(0)
	elif len(db)<len(da):
		for i in range(len(da)-len(db)):
			db.append(0)
        
	da.reverse()
	db.reverse()
	ca=da+ea
	cb=db+eb
	
	  
        
	for i in range(len(ca)-1,-1,-1): #Comprobando cual es el número mayor
		if ca[i]<cb[i]:
			c=cb
			d=ca
			sig="-"
			bolen=1
			break
		elif ca[i]>cb[i]:
			c=ca
			d=cb
			sig="+"
			bolen=1
			break
		else:
			bolen=2
        
        
	if bolen==2: #Si los números son iguales da 0 
		sig="+"
		r=[0]
		er=[0] 
           
           
	else:
		r=[]
		for i in range(len(c)):      #Efectuando resta
			
			if c[i]<d[i]:
				
				if c[i+1]!=0:
					c[i+1]=c[i+1]-1     
				else:
					c[i+1]=9
					for k in range(i+2,len(c)):
						if c[k]==0:
							c[k]=9
						else:
							c[k]=c[k]-1
							break
                   
                   
				r.append(10+c[i]-d[i])
			else:
				r.append(c[i]-d[i])
        
            
		r.reverse() #Organizando resta y quitando ceros a la izquierda   
          
		#creando la tupla de la resta
		er=[]
		for z in range(len(r)-len(da)):
			er.append(r[0])
			r.pop(0)
			   
		#Quitando ceros
		for q in range(len(er)):
			if er[0]==0:
				del er[0]
				   
			else:
				break
		if er==[]:
			er=[0]
        
	return [sig]+er,r 



def multiplicacion(a, b):


	ca=[0]+a[0]+a[1]
	cb=[0]+b[0]+b[1]
             
	ca.reverse()
	cb.reverse()
	res=0
             
	suma=[0]
	for i in range(len(cb)-1):
		P=[]
		for j in range(len(ca)):
			x=cb[i]*ca[j]+res
			P.append(x%10)
			res=int(x/10)
              
		Pd=i*[0]+P
		Pd.reverse()
              
		suma=Sum(suma,Pd)
                 
              
	p=len(suma)-1-len(a[1])-len(b[1])
	PZ=[]
	PD=[]
	for k in range(len(suma)):
		if k<=p:
			PZ.append(suma[k])
		else:
			PD.append(suma[k]) 
                                    
	if PZ[0]==0:
		PZ.pop(0)
	prod=PZ,PD
              
	return prod 


def division(a, b):
    pass


def comparacion(a, b):
    pass


def pi():
    pass


if __name__ == "__main__":
    print(imprimir(pi()))
