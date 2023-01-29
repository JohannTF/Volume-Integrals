import matplotlib.pyplot as plt
import numpy as np
from sympy import lambdify
from sympy.abc import x,y

class Grafica3D():
    def __init__(self, funcionF, funcionG, ecuacion, inicio, final, puntos, m_recta):
        self.__funcionF = funcionF
        self.__funcionG = funcionG
        self.__ecuacion = ecuacion
        self.__mRecta = m_recta
        self.x = np.linspace(inicio, final, puntos)
        self.e = inicio
        self.f = final
        self.dots = puntos

    def curvas(self, tipo, ax):
        if(tipo == 0): # Grafica de la recta
            y = self.__funcionF(self.x)
            c = "#00FFFF" 
        if(tipo == 1):
            y = self.__funcionG(self.x) # Grafica de la parabola
            c = '#ff00ff'
        if(self.__mRecta == 0):
            y = np.linspace(self.__funcionF(self.__mRecta), self.__funcionF(self.__mRecta), self.dots)
        xx = np.meshgrid(y, self.x)[1]
        yy = np.meshgrid(self.x, y)[1]
        z = self.__ecuacion(self.x, y)
        zz = np.empty(shape = (self.dots,self.dots))
        if(type(z) != int):
            for i in range(self.dots):    
                zz[i] = np.linspace(0, z[i], self.dots)
        else:
            for i in range(self.dots):
                zz[i] = np.linspace(0, z, self.dots)
        ax.plot(self.x, y, z, color = "black", lw = 4) # Linea arriba
        ax.plot(self.x, y, 0, color = "black", lw = 4) # Linea abajo
        ax.plot([self.x[0], self.x[0]], [y[0], y[0]], [zz[0][0], zz[0][-1]], color = "black", lw = 4) # Lineas lateral1
        ax.plot([self.x[-1], self.x[-1]], [y[-1], y[-1]], [zz[-1][0], zz[-1][-1]], color = "black", lw = 4) # Lineas lateral2
        ax.plot_surface(xx, yy, zz, color = c, alpha = 0.4)
        ax.plot_wireframe(xx, yy, zz, color = c, alpha = 0.3)

    def superficie(self, posicion, ax):
        xx = np.meshgrid(self.x, self.x)[1]
        y_parab = np.empty(shape=self.dots)
        y_rect = np.empty(shape=self.dots)
        #z_techoRecta = np.empty(shape=self.dots)
        #z_techoParab = np.empty(shape=self.dots)
        yy = np.empty(shape=(self.dots,self.dots))
        for i in range(self.dots):
            yy[i] = np.linspace(self.__funcionF(xx[i][0]), self.__funcionG(xx[i][0]), self.dots)
        if(posicion == 1): # Graficar el techo
            c = '#77DD'
            zz = self.__ecuacion(xx, yy)
            if(type(zz) == int):
                valorRelleno = self.__ecuacion(xx, yy)
                zz = np.full(shape=(self.dots, self.dots), fill_value = valorRelleno)
        else: # Graficar el suelo
            c = '#00F839'
            zz = np.zeros(shape=(self.dots, self.dots))
        for i in range(self.dots):
            y_rect[i] = yy[i][0]
            y_parab[i] = yy[i][-1]
        z_techoRecta = self.__ecuacion(self.x, y_rect)
        z_techoParab = self.__ecuacion(self.x, y_parab)
        ax.plot(self.x, y_parab, z_techoParab, color = "black", lw = 4) # Linea frontal
        ax.plot(self.x, y_rect, z_techoRecta, color = "black", lw = 4) # Linea Trasera
        ax.plot_surface(xx, yy, zz, color = c, alpha = 0.4)
        ax.plot_wireframe(xx, yy, zz, color = c, alpha = 0.3)
        
    def paredes(self, tipo, ax):
        if(tipo == 0): # Graficar la pared de e
            xx = np.meshgrid(np.linspace(self.e, self.e, self.dots), np.linspace(self.e, self.e, self.dots))[1]
            y = np.linspace(self.__funcionF(self.e), self.__funcionG(self.e), self.dots)
            c = "#DDA420"
        else: # Graficar la pared de f
            xx = np.meshgrid(np.linspace(self.f, self.f, self.dots), np.linspace(self.f, self.f, self.dots))[1]
            y =  np.linspace(self.__funcionF(self.f), self.__funcionG(self.f), self.dots)# Grafica de la parabola
            c = '#FFFF00'
        yy = np.meshgrid(y,y)[1]
        zz = np.empty(shape = (self.dots,self.dots))
        z = np.empty(shape=self.dots)
        for i in range(self.dots):
            zz[i] = np.linspace(0,self.__ecuacion(xx[i][0], yy[i][0]), self.dots)
        for i in range(self.dots): z[i] = zz[i][self.dots-1]
        ax.plot(xx[0], y, z, color = 'black', lw = 4) # Linea arriba
        ax.plot(xx[0], y, 0, color = 'black', lw = 4) # Linea abajo
        ax.plot([xx[0][0], xx[0][0]], [y[0], y[0]], [0, zz[0][self.dots-1]], color = 'black', lw = 4) # Lineas lateral1
        ax.plot([xx[0][0], xx[0][0]], [y[self.dots-1], y[self.dots-1]], [0, zz[self.dots-1][self.dots-1]], color = 'black', lw = 4) # Lineas lateral2
        ax.plot_surface(xx, yy, zz, color = c, alpha = 0.4)
        ax.plot_wireframe(xx, yy, zz, color = c, alpha = 0.3)
        
def main3d(a_dato, b_dato, c_dato, e_dato, f_dato, m_recta, b_recta, a_parabola, exponente_parabola, b_parabola, c_parabola, fig, ax):
    ax.clear()
    f = (m_recta*x)+b_recta # Ec recta
    g = a_parabola*(x**exponente_parabola) + b_parabola*x + c_parabola
    ecuacion = x**a_dato + y**b_dato + c_dato*x*y

    f_resultado = lambdify(x, f)    
    g_resultado = lambdify(x, g)
    ec_resultado = lambdify((x,y), ecuacion)

    miGrafica = Grafica3D(f_resultado, g_resultado, ec_resultado, e_dato, f_dato, 30, m_recta)
    for i in range(2):
        miGrafica.curvas(i, ax)
        miGrafica.superficie(i, ax)
        miGrafica.paredes(i, ax)

    # Graficando el plano z = 0
    limiteX = ax.get_xlim()
    limiteY = ax.get_ylim()
    baseX, baseY = np.meshgrid(limiteX, limiteY)
    baseZ = np.zeros((2,2))
    ax.set_xlabel("X", color = 'w')
    ax.set_ylabel("Y", color = 'w')
    ax.set_zlabel("Z", color = 'w')
    ax.set_title((r'$\int \:\int \:x^%d+y^%d+%dxy$' % (a_dato, b_dato, c_dato)), color = 'w', fontsize=18, fontweight="bold")
    ax.plot_surface(baseX, baseY, baseZ, color = "black", alpha = 0.4)
    ax.view_init(20, 30)