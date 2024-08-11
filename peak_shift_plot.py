import matplotlib.pyplot as plt

# data for BNG-1-B heating run wihtout window

peak1 =[8.941,8.941,8.941,8.9565,8.972,8.972,8.972,8.9875,9.0031,9.0188,9.0345,9.0503,9.0503,9.082,9.082,9.0979]
peak2 =[14.445,14.445,14.485,14.485,14.567,14.567,14.608,14.649,14.691,14.774,14.817,14.817,14.859,14.859,15.031,15.031]
peak3 =[15.859,15.859,15.859,15.859,15.907,15.907,15.956,15.956,16.055,16.055,16.055,16.105,16.105,16.225,16.305,16.48]
peak4 =[16.621,16.621,16.621,16.675,16.675,16.728,16.728,16.783,16.783,16.837,16.892,17.003,17.003,17.059,17.115,17.172]

temp = [24,50,100,150,200,250,300,350,400,450,500,532]
temp2 = [-190,-150,-100,-50,0,24,50,100,150,200,250,300,350,400,450,500]


plt.subplot(2,2,1)
plt.plot(temp2,peak1,'red')
plt.xlabel('Temperatue (Celsius)')
plt.ylabel('Peak position ($\mu$m)')
plt.title('Peak 1: 8.9-9.1 micron')

plt.subplot(2,2,2)
plt.plot(temp2,peak2,'orange')
plt.xlabel('Temperatue (Celsius)')
plt.ylabel('Peak position ($\mu$m)')
plt.title('Peak 2: 14.4-15.1 micron')

plt.subplot(2,2,3)
plt.plot(temp2,peak3,'green')
plt.xlabel('Temperatue (Celsius)')
plt.ylabel('Peak position ($\mu$m)')
plt.title('Peak 3: 15.8-16.5 micron')

plt.subplot(2,2,4)
plt.plot(temp2,peak4,'indigo')
plt.xlabel('Temperatue (Celsius)')
plt.ylabel('Peak position ($\mu$m)')
plt.title('Peak 4: 16.6-17.2 micron')

plt.suptitle('PUG-16-5b : Peak Shift v/s Temperature')
plt.show()
