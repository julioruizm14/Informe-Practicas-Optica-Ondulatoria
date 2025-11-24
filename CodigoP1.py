
import numpy as np
import matplotlib.pyplot as plt
import pylab as plot
params = {'legend.fontsize': 20,
          'legend.handlelength': 2}
plot.rcParams.update(params)


############    I      LUZ PARALELA Y PERPENDICULAR          ###############

#PERPENDICULAR
theta1 = np.array([5, 10, 20, 30, 40, 50, 60, 70, 75])
theta1= theta1 *2*np.pi/360                                                     #medidas experimentales
I1 = [3, 4, 6, 5, 9, 10, 17, 25, 31]

#PARALELA
theta2 = np.array([5, 10, 20, 30, 40, 45, 47, 49, 50, 52, 55, 60, 70, 75])
theta2= theta2 *2*np.pi/360                                                     #medidas experimentales 
I2 = [10, 7, 6, 6, 4, 1, 1, 0, 0, 0, 0, 1, 5, 21]




thetaB =(49+ 50+ 52+ 55)/4  *2*np.pi/360   #angulo de Brewstel
n1= np.tan(thetaB)
print(n1)                           #n 1 = 1.2571722989189544


####   TEORICAS ####
n = 1
I0 = 160


#PERPENDICULAR
ttheta1 = np.linspace( 5*np.pi/180 ,75*np.pi/180 , 500)
ttheta1t = np.arcsin( (n/n1)*np.sin(ttheta1) )

I1t = I0*( (np.sin(ttheta1 - ttheta1t)**2 ) / (np.sin(ttheta1 + ttheta1t)**2 ) ) 

#PARALELA

ttheta2 = np.linspace( 5*np.pi/180 ,75*np.pi/180 , 500)
ttheta2t = np.arcsin( (n/n1)*np.sin(ttheta2) )

I2t = I0*( (np.tan(ttheta2 - ttheta2t)**2 ) / (np.tan(ttheta2 + ttheta2t)**2 ) ) 


#GRAFICAS

plt.figure(figsize=(15,8))
plt.xlabel('θ (rads)', fontsize=20)
plt.ylabel('I (Lux)', fontsize=20)
plt.plot(theta1,I1,'o',color='red')
plt.plot(theta2,I2,'o',color='blue')

plt.plot(ttheta1,I1t,color='red',  label='Orientación Perpendicular')
plt.plot(ttheta2,I2t,color='blue', label='Orientación Paralela')
plt.legend()
plt.grid()
plt.show()


##################    IV      EL LOCO DEL MALUS          ###############
theta4 = np.linspace(-90, 90, 37)*2*np.pi/360
I4=[3, 0, 2, 7, 16, 34, 50, 84, 125, 163 ,201, 241, 279, 318, 345, 377, 405, 390, 419, 416, 415, 422, 403, 385, 350, 336, 296, 259, 229, 195, 145, 115, 85, 63, 37, 19, 6]


Io = max(I4)
ttheta = np.linspace(-90, 90, 370)*2*np.pi/360

It= Io*(np.cos(ttheta))**2



plt.figure(figsize=(15,8))
#plt.title('Ley de Malus')
plt.xlabel('θ (rads)', fontsize=20)
plt.ylabel('I (Lux)', fontsize=20)
plt.plot(theta4,I4, color='red', label='Experimental')
plt.plot(ttheta,It, color='blue', label='Ley de Malus')
plt.plot(ttheta+0.12,It, color='purple',label='con θ desplazado')
plt.legend(loc='upper right', )
plt.grid()
plt.show()










