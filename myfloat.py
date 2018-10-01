###########################################33

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
def Cadena(a):
    m=a[0]
    n=a[1]
    inter=""
    decil=""
    for i in m:
        inter=inter + str(i)
    for i in n:
        decil=decil+str(i)
    num=inter+"."+decil
    return num

def ImTupig(a):
    num=a
    return num
        

def convtupl(otro): #Convierte a Tupla
    t=str(otro)
    for i in range(len(t)):
        if t[i]==".":
            dec=True
            break
        else:
            dec=False
            
    etupl=[]
    dtupl=[]
    for j in range(0,i):
        etupl.append(int(t[j]))
    if dec==True:
        for j in range(i+1,len(t)):
            dtupl.append(int(t[j]))
    else:
        dtupl.append(0)
        etupl.append(int(t[i]))
    return etupl,dtupl
#sumamamam
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
    
                
# define MyFloat resta     
    
def res(a,b):
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
# define MyFloat multiplicacion        
def mult(a,b):

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
# define MyFloat divicion 
def divs(x,y):
             
    a=x[0][::1],x[1][::1]     
    b=y[0][::1],y[1][::1]
    
    resta=a
    c=[]
    bol=1
    l=1 
    for i in range(len(b[0])+1-len(a[0])): #Cual es más grande
        B=res(resta,b)
        if B[0][0]=="-":
            bol=0
               
            c.append(0)
            r3=resta[1][0]
            ra=resta[0]+[r3]
            resta[1].pop(0)
            rb=resta[1]
            if rb==[]:
                rb=rb+[0]
            resta=ra,rb
        else:
            break
                
            
            
    while len(c)<50: 
        for k in range(10,-1,-1):
            if k==10:
                decen=([1,0],[0])
                pro=mult(b,decen)
            else:
                decen=([0,k],[0])
                pro=mult(b,decen)
                
            resid=res(resta,pro)    
            if resid[0][0]=="+":
                break
            
        if k==10: #Aumentando una cifra al divisor
            r=b[1][0]
            be=b[0]+[r]
            b[1].pop(0)
            bd=b[1]  
            b=be,bd
            if b[1]==[]:
                bd=bd+[0]
            b=be,bd
            l=l+1
            
                                        
        else:
            resid[0].pop(0)
            r2=resid[1][0]
            re=resid[0]+[r2]
            resid[1].pop(0)
            rd=resid[1]
            resta=re,rd
            c.append(k)
            
        if resta==([0,0],[]):
            break
                        
           #print "ahora residuo es" 
           #print resta
                 
    c1=[]
    if bol==0:
        c1=[0]
        c.pop(0)
    else: 
        for i in range(l):
            if len(c)<l:
                c.append(0)
            c1.append(c[0])
            c.pop(0)
    if c==[]:
        c=[0]        
    coc=c1,c
    return coc

def comparacion(a, b):
    pass




###############################################3
class MyFloat:
    
    def __init__(self,num):
        self.n=num
        self.e=num[0]
        self.d=num[1]
        
         
    
       
           
    def __add__(self,otro):
        
        if isinstance(otro,MyFloat):  
            a=self.n
            b=otro.n
            c=Suma(self.n,otro.n)
          
            return MyFloat(c)
       
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(Suma(self.n,tup.n))
        
        
    
    def __radd__(self,otro):
        return self.__add__(otro)
    
    def __sub__(self,otro):
        if isinstance(otro,MyFloat):
            a=self.n
            b=otro.n
            return MyFloat(res(self.n,otro.n))
            
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(res(self.n,tup.n))
    
    def __rsub__(self,otro):
        
        ret= self.__sub__(otro) 
        if ret.e[0]=="+":
            ret.e[0]="-"
        else:
            ret.e[0]="-"
        ret=MyFloat((ret.e,ret.d))
        return ret
        
    def __mul__(self,otro):
        if isinstance(otro,MyFloat):
            a=self.n
            b=otro.n  
            return MyFloat(mult(a,b))  
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(mult(self.n,tup.n))
                
    def __rmul__(self,otro):
        return self.__mul__(otro)
                        
    def __truediv__(self,otro):
        if isinstance(otro,MyFloat):
            a=self.n
            b=otro.n     
            return MyFloat(divs(a,b))
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(divs(self.n,tup.n))
        #return print ("algo")
    
    def __rtruediv__(self,otro):
        if isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(divs(tup.n,otro.n))
          # return print ("algo") 
    def __eq__(self, otro):
        if res(self.n,otro.n)==(["+",0],[0]):
            return True
        else:
            return False
            
    def __ne__(self, otro):
        if res(self.n,otro.n)!=(["+",0],[0]):
            return True
        else:
            return False
    
    
    def __str__(self):
        t1=self.n
        return Cadena(t1)
    
    def __repr__(self):
        return self.__str__()
	
	

if __name__ == "__main__":
    
	#calculo de pi 
	Pie2=MyFloat(([0],[0]))
	Tupla1=MyFloat(([1],[0]))
	Tupla2=MyFloat(([2],[0]))
		
	for l in range(0,10):
		for j in range(0,10):
			for i in range(0,10):
				for k in range(0,10,2):
					ka=[l]+[j]+[i]+[k]
					Tuplak=MyFloat((ka,[0]))
					dk=Tupla2*Tuplak
					dkm1=dk+Tupla1
					usdkm1=Tupla1/dkm1
					Pie2=Pie2+usdkm1
	print (Pie2)
