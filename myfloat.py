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
def cadena(a):
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


def suma(a,b):

    #a=([8,3,5,6],[3,2,1,9])
    #b=([8,4,5,3],[7,3,2,1,8,7,9])

    xe=[]
    xd=[]
    ye=[]
    yd=[]
    #print (len(a[0]))
    for i in range(len(a[0])):
        xe.append(a[0][i])

    #print (len(a[1]))
    for i in range(len(a[1])):
        xd.append(a[1][i])

    #print (len(b[0]))
    for i in range(len(b[0])):
        ye.append(b[0][i])

    #print (len(b[1]))
    for i in range(len(b[1])):
        yd.append(b[1][i]) 

    #los anteriores cuatro for's extraen las listas de la tuplas y las nombra dentro de 
    #los numero como xe parte entera etc

    #print(xe,"*", xd,"*",ye,"*",yd) 


    x=xe,xd
    y=ye,yd
    #print(x,"**",y)
    maxe=max(len(xe),len(ye))
    maxd=max(len(xd),len(yd))
    #print(maxe,"**",maxd)

    #ahora la idea es hacer que cada uno tengan la misma cantidad de cifras
    #la decimal agregar ceros a las derecha y la entera a la izquierda

    #parte entera
    xe.reverse()
    ye.reverse()

    if len(xe)<len(ye):         #Igualando los tamaños de la parte entera
        for i in range(len(ye)-len(xe)):
            xe.append(0)
    elif len(ye)<len(xe):
        for i in range(len(xe)-len(ye)):
            ye.append(0)
    xe.reverse()
    ye.reverse()

    #print ("partes enteras",xe,ye)

    #parte decimal


    if len(xd)<len(yd):         #Igualando los tamaños de la parte decimal
        for i in range(len(yd)-len(xd)):
            xd.append(0)
    elif len(yd)<len(xd):
        for i in range(len(xd)-len(yd)):
            yd.append(0)

    #print ("partes decimales",xd,yd)

    #en este punto se esta listo para efectuar la suma 

    xd.reverse()
    yd.reverse()
    rd=0
    sd=[]   #resultado de la suma decimal
    for i in range(len(xd)):
        s=xd[i]+yd[i]+rd
        if s>=10:
            rd=1
            s=(s%10)
            sd.append(s)
        else:
            rd=0
            sd.append(s)
    sd.reverse()
    #print ("resultado de la suma decimal",sd, "residuo decimal= ",residuod)

    #ahora la suma de la parte entera

    xe.reverse()
    ye.reverse()

    re=rd
    see=[]   #resultado de la suma entera
    for i in range(len(xe)):
        se=xe[i]+ye[i]+re
        if se>=10:
            re=1
            se=(se%10)
            see.append(se)
        else:
            re=0
            see.append(se)
    see.append(re)
    see.reverse()
    #print (see , "re=",re)

    #print (see, sd)
    
    return(see, sd)
    
                
# define MyFloat resta     
    
def resta(a,b):
    #a=([9,8,3],[8,2,1,9])
    #b=([8,4,8,9,8,7],[7,3,2,9])

    xe=[]
    xd=[]
    ye=[]
    yd=[]
    #print (len(a[0]))
    for i in range(len(a[0])):
        xe.append(a[0][i])

    #print (len(a[1]))
    for i in range(len(a[1])):
        xd.append(a[1][i])

    #print (len(b[0]))
    for i in range(len(b[0])):
        ye.append(b[0][i])

    #print (len(b[1]))
    for i in range(len(b[1])):
        yd.append(b[1][i]) 

    #los anteriores cuatro for's extraen las listas de la tuplas y las nombra dentro de 
    #los numero como xe parte entera etc

    #print(xe,"*", xd,"*",ye,"*",yd) 


    x=xe,xd
    y=ye,yd
    #print(x,"**",y)
    maxe=max(len(xe),len(ye))
    maxd=max(len(xd),len(yd))
    #print(maxe,"**",maxd)

    #ahora la idea es hacer que cada uno tengan la misma cantidad de cifras
    #la decimal agregar ceros a las derecha y la entera a la izquierda

    #parte entera
    xe.reverse()
    ye.reverse()

    if len(xe)<len(ye):         #Igualando los tamaños de la parte entera
        for i in range(len(ye)-len(xe)):
            xe.append(0)
    elif len(ye)<len(xe):
        for i in range(len(xe)-len(ye)):
            ye.append(0)
    xe.reverse()
    ye.reverse()

    #print ("partes enteras",xe,ye)

    #parte decimal


    if len(xd)<len(yd):         #Igualando los tamaños de la parte decimal
        for i in range(len(yd)-len(xd)):
            xd.append(0)
    elif len(yd)<len(xd):
        for i in range(len(xd)-len(yd)):
            yd.append(0)
    #print ("partes decimales",xd,yd)

    #ahora convertimos a cadena para evaluar cual numeo es mas grande 
    numero=float(cadena(a))-float(cadena(b))
    #print("la resta es ", numero)
    nop=0
    if numero<0:
        nop=1 
        #print ("a es menor que b", "**",nop)
    else:
        nop=2
        #print ("b es menor que a","**",nop)






    if nop==1:

        #parte decimal

        #hacer la resta de b-a
        xd.reverse()
        yd.reverse()
        rt=[] #resultado de la resta
        rst=0 #residuo de la resta
        res=0
        r=0
        for i in range(len(xd)):
            yd[i]=yd[i]-res
            if yd[i]>xd[i]:
                r=yd[i]-xd[i]
                rt.append(r)
                res=0
            if yd[i]<xd[i]:
                yd[i]=yd[i]+10

                if i == len(xd): #si es el ultimo numero de la resta hay que solo hacer la resta 
                    r=yd[i]-xd[i] #y guardar el residuo como 1
                    rt.append(r)
                    res=1                
                else:
                           #si no es el ultimo se le resta al siguiente uno
                    r=yd[i]-xd[i]
                    rt.append(r)
                    res=1 

            if yd[i]==xd[i]:
                rt.append(0)
                res=0
        rt.reverse()
        #print(rt , res)
        #ahora hay que restar la parte entera, para esto hay que tener en cuenta el residuo anterior
        #######


        xe.reverse()
        ye.reverse()
        rte=[] #resultado de la resta 
        rese=res
        re=0
        for i in range(len(xe)):
            ye[i]=ye[i]-rese
            if ye[i]>xe[i]:
                re=ye[i]-xe[i]
                rte.append(re)
                rese=0
            if ye[i]<xe[i]:
                ye[i]=ye[i]+10
                re=ye[i]-xe[i]
                rte.append(re)
                rese=1
            if ye[i]==xe[i]:
                rte.append(0)
                rese=0
        rte.reverse() 

    if nop==2:
        #parte decimal

        #hacer la resta de b-a
        xd.reverse()
        yd.reverse()
        rt=[] #resultado de la rest
        res=0
        r=0
        for i in range(len(xd)):
            xd[i]=xd[i]-res
            if xd[i]>yd[i]:
                r=xd[i]-yd[i]
                rt.append(r)
                res=0
            if xd[i]<yd[i]:
                xd[i]=xd[i]+10
                r=xd[i]-yd[i] 
                rt.append(r)
                res=1                    
            if xd[i]==yd[i]:
                rt.append(0)
                res=0
        rt.reverse()
        #print(rt , res)
        #ahora hay que restar la parte entera, para esto hay que tener en cuenta el residuo anterior

        #parte entera

        xe.reverse()
        ye.reverse()
        rte=[] #resultado de la resta 
        rese=res
        re=0
        for i in range(len(xe)):
            xe[i]=xe[i]-rese
            if xe[i]>ye[i]:
                #print("*****",xe[i],ye[i])
                re=xe[i]-ye[i]
                #print ("re=",i,"**", re)
                rte.append(re)
                rese=0
            if xe[i]<ye[i]:
                xe[i]=xe[i]+10
                #print("**lll***",xe[i],ye[i])
                re=xe[i]-ye[i]
                #print ("re=",i,"**", re)
                rte.append(re)
                rese=1
            if xe[i]==ye[i]:
                rte.append(0)
                rese=0
            #print (rte[i])
        rte.reverse()

    return(rte,rt) #restorna dos listas
# define MyFloat multiplicacion        
def multiplicacion(a,b):
    #a=([9],[8,2,8,9,7,8,7,9,3,1,5,7,8,9,3,2,4,8,9,6,9,3,2,1,5,7,4,8,9])
    #b=([8],[7,8])

    x=[0]+a[0]+a[1]
    y=[0]+b[0]+b[1]

    #print("x=",x)
    #print("y=",y)

    x.reverse()
    y.reverse()
    res=0

    rsult=[0]
    for i in range(len(y)-1):
        p=[]
        for j in range(len(x)):
            f=y[i]*x[j]+res
            p.append(f%10)
            res=int(f/10)
        pd=i*[0]+p #se agraga el cero de la suma 
        pd.reverse()
        rsult=Sum(rsult,pd) #se ejecuta la suma de dos listas
    #print("resultado de la multiplicaion", rsult)
    h=len(rsult)
    #print(h)
    g=len(a[1])
    m=len(b[1])

    u=h-1-g-m
    PZ=[]
    PD=[]
    for k in range(h):
        if k<=u:
            PZ.append(rsult[k])
        else:
            PD.append(rsult[k]) 


    if PZ[0]==0:
        PZ.pop(0)

    prod=PZ,PD #retorna dos listas, una con la parta entera otra con la parte decimal


    #print( prod)
    return(prod)


# define MyFloat divicion 
def divs(x,y):
    
    DEC=30
             
    a=x[0][::1],x[1][::1]     
    b=y[0][::1],y[1][::1]
    
    resa=a
    c=[]
    bol=1
    l=1
    #print("**",resa,b)
    for i in range(len(b[0])+1-len(a[0])): #Cual es más grande
        B=resta(resa,b)
        #print("BIEN",B)
        t1=float(cadena(resa))
        t2=float(cadena(b))
        #print(t1,t2)
        t=t1-t2
        
        if t<0:
            bol=0
               
            c.append(0)
            r3=resa[1][0]
            ra=resa[0]+[r3]
            resa[1].pop(0)
            rb=resa[1]
            if rb==[]:
                rb=rb+[0]
            resa=ra,rb
        else:
            break
            
            
    #print(len(c))        
    while len(c)<DEC: 
        for k in range(10,-1,-1):
            if k==10:
                decen=([1,0],[0])
                pro=multiplicacion(b,decen)
            else:
                decen=([0,k],[0])
                pro=multiplicacion(b,decen)
                
            resid=resta(resa,pro)
            g=float(cadena(resa))-float(cadena(pro))
            if g>0:
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
            resa=re,rd
            c.append(k)
            
        if resa==([0,0],[]):
            break
                        
           #print "ahora residuo es" 
           #print resta
    #print("******",resa)              
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
def comparacion(a,b):



    ###toca igualar los tamaños para la parte entera
    if len(ae)<len(be):
        ae.reverse()
        for i in range(len(be)-len(ae)):
            ae.append(0)
        ae.reverse()

    elif len(be)<len(ae):
        be.reverse()
        for i in range(len(ae)-len(be)):
            be.append(0)
        be.reverse()

    #print("**",x,y)

    #igualando la parte decimal 

    if len(ad)<len(bd):         #Igualando los tamaños de la parte decimal
        for i in range(len(bd)-len(ad)):
            ad.append(0)
    elif len(bd)<len(ad):
        for i in range(len(ad)-len(bd)):
            bd.append(0)

    #print("**",x,y)



    #quitando los ceros de la izquierda de la parte entera

    while i<len(ae):
        if ae[i]!=0:
            break
        else:
            ae.pop(ae[i])
        i=0


    while i<len(be):

        if be[i]!=0:
            break
        else:
            be.pop(be[i])
        i=0





    #print("partes enteras",ae,"*",be)
    #print("partes decimales",ad,"*",bd)
    ####
    m=max(len(ae),len(be))
    #print("m",m)
    n=m-1
    #print(n)

    z=max(len(ad),len(bd))
    #print("z",z)
    c=z-1
    #print(c)


    for j in range(m):
        if ae[j]==be[j]:
            #print("aaa")
            if j==n:
                igue=1
                #print("las partes enteras son iguales")
                break
            else:
                continue

        else:
            igue=2
            #print("las partes enteras son diferentes")
            break

    for j in range(z):
        if ad[j]==bd[j]:
            #print("aaa")
            if j==c:
                igued=1
                #print("las partes decimales son iguales")
                break
            else:
                continue

        else:
            igued=2
            #print("las partes decimales son diferentes")
            break   
    if igue==1 and igued==1:
        print("iguales")
        return True
    else:
        print("diferentes")
        return False

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
            c=suma(self.n,otro.n)
          
            return MyFloat(c)
       
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(suma(self.n,tup.n))
        
        
#####
        
    def __sub__(self,otro):
        if isinstance(otro,MyFloat):
            a=self.n
            b=otro.n
            return MyFloat(resta(self.n,otro.n))
            
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(resta(self.n,tup.n))
    
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
            return MyFloat(multiplicacion(a,b))  
        elif isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(multiplicacion(self.n,tup.n))
                
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
    
    def __rtruediv__(self,otro):
        if isinstance(otro,(int,float)):
            tup=MyFloat(convtupl(otro))
            return MyFloat(division(tup.n,otro.n))

    
###3
    def __radd__(self,otro):
        return self.__add__(otro)
    
    def __eq__(self, otro):
        if resta(self.n,otro.n)==(["+",0],[0]):
            return True
        else:
            return False
            
    def __ne__(self, otro):
        if resta(self.n,otro.n)!=(["+",0],[0]):
            return True
        else:
            return False
    
    
    def __str__(self):
        return '{}'.format(self.n)

    def __repr__(self):
        return '{}'.format(self.n)
        
    def __getitem__(self, key):
        return self.pi[key]
    	
	

if __name__ == "__main__":
    
	#calculo de pi
    # x=0.0
    # for m in range(0,10):
        # if m%2==0:
            # x=x+4/(2*MyFloat((,[0,0]))+1)   
        # else:
            # x=x-4/(2*MyFloat((ka,[0,0]))+1)
   
    # print(imprimir(x))
	
	
	
	
	Pie2=MyFloat(([0,0],[0,0]))
	Tupla1=MyFloat(([0,1],[0,0]))
	tupla4=MyFloat(([0,4],[0,0]))
	Tupla2=MyFloat(([0,2],[0,0]))
	
	for l in range(0,10):
		for j in range(0,10):
			for i in range(0,10):
				for k in range(0,10):
					ka=[l]+[j]+[i]+[k]
					Tuplak=MyFloat((ka,[0]))
                
					dk=Tupla2*Tuplak
					dkm1=dk+Tupla1
					usdkm1=tupla4/dkm1
				
					
					if k % 2 ==0:
						Pie2=Pie2+usdkm1
					else:
						Pie2=Pie2-usdkm1
	
	# while i<len(Pie2[0]):
		# if Pie2[0][i]!=0:
			# break
		# else:
			# Pie2[0].pop(Pie2[0][i])
		# i=0
	
	pi=Pie2

	print (pi)
		
