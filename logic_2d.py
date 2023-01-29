import matplotlib.pyplot as plt
import numpy as np
from sympy import integrate, lambdify, solve, Equality
from sympy.abc import x, y

def recta(f_resultado, m_recta, e_dato, f_dato):
    x_valores = np.array([e_dato-2, f_dato+2])
    if(m_recta != 0):
        y_valores = f_resultado(x_valores)
    else:
        y_valores = np.array([f_resultado(x_valores), f_resultado(x_valores)])
    x_areaRecta =  np.linspace(e_dato, f_dato, 100)
    y_areaRecta = f_resultado(x_areaRecta)
    return x_valores ,y_valores, y_areaRecta

def parabola(g_resultado, e_dato, f_dato):
    x_valores = np.linspace(e_dato-2, f_dato+2, 100)
    y_valores = g_resultado(x_valores)
    x_areaParabola = np.linspace(e_dato, f_dato, 100)
    y_areaParabola = g_resultado(x_areaParabola)
    return x_valores ,y_valores, x_areaParabola, y_areaParabola

def interseccion(f,g):
    ecInterseccion = Equality(f,g)
    soluciones = solve(ecInterseccion, x)
    cadena = str(soluciones[0])
    for i in cadena:
        if(i == "I"):
            return 0; # No hay intersección
            break;
        elif(i == cadena[-1]):
            return soluciones; # Si hay interseccion
            break;

def volumen(f,g,ecuacion, e_dato, f_dato):
    intersecciones = interseccion(f,g)
    resultado = 0
    if(intersecciones == 0): # No hay intersecciones (CASO 1)
        print("No hay intersecciones")
        resultado = 1
        primeraIntegral = integrate(ecuacion, (y, f, g))
        segundaIntegral = integrate(primeraIntegral, (x, e_dato, f_dato))
        resultado = segundaIntegral

    else: # Si hay intersecciones
        resultado = 1
        if(len(intersecciones) == 1): # Una intersección
            print("Hay una intersección")
            if(e_dato < intersecciones[0]): # (CASO 2)
                primeraIntegral1 = integrate(ecuacion, (y, f, g))
                primeraIntegral2 = integrate(ecuacion, (y, f, g))
                segundaIntegral1 = integrate(primeraIntegral1, (x, e_dato, intersecciones[0]))
                segundaIntegral2 = integrate(primeraIntegral2, (x, intersecciones[0], f_dato))
                resultado = segundaIntegral1 + segundaIntegral2
            else: # (CASO 1 APLICADO A UNA INTERSECCIÓN)
                primeraIntegral = integrate(ecuacion, (y, f, g))
                segundaIntegral = integrate(primeraIntegral, (x, e_dato, f_dato))
                resultado = segundaIntegral

        if(len(intersecciones) == 2): # Dos intersecciones
            print("Hay dos intersecciones")
            print(intersecciones)
            """ if(e_dato<intersecciones[1] and f_dato>intersecciones[0]):
                primeraIntegral = integrate(ecuacion, (y, f, g))
                segundaIntegral1 = integrate(primeraIntegral, (x, e_dato, intersecciones[1]))
                segundaIntegral2 = integrate(primeraIntegral, (x, intersecciones[1], intersecciones[0]))
                segundaIntegral3 = integrate(primeraIntegral, (x, intersecciones[0], f_dato))
                resultado = segundaIntegral1 + segundaIntegral2 + segundaIntegral3 """

            #if(e_dato == intersecciones[1] and f_dato == intersecciones[0])
            if(e_dato<intersecciones[0] and f_dato>intersecciones[0]): # (CASO 4)
                primeraIntegral1 = integrate(ecuacion, (y, g, f))
                primeraIntegral2 = integrate(ecuacion, (y, f, g))
                segundaIntegral1 = integrate(primeraIntegral1, (x, e_dato, intersecciones[0]))
                segundaIntegral2 = integrate(primeraIntegral2, (x, intersecciones[0], f_dato))
                resultado = segundaIntegral1 + segundaIntegral2

            if(e_dato<intersecciones[1] and f_dato>intersecciones[1]): # (CASO 5)
                primeraIntegral1 = integrate(ecuacion, (y, f, g))
                primeraIntegral2 = integrate(ecuacion, (y, g, f))
                segundaIntegral1 = integrate(primeraIntegral1, (x, e_dato, intersecciones[1]))
                segundaIntegral2 = integrate(primeraIntegral2, (x, intersecciones[0], f_dato))
                resultado = segundaIntegral1 + segundaIntegral2

            if(e_dato>intersecciones[1] and f_dato<intersecciones[0]): # (CASO 6)
                primeraIntegral = integrate(ecuacion, (y, g, f))
                segundaIntegral = integrate(primeraIntegral, (x, e_dato, f_dato))
                resultado = segundaIntegral
    print("Volumen:",resultado)
    return resultado

def main2d(a_dato, b_dato, c_dato, e_dato, f_dato, m_recta, b_recta, a_parabola, exponente_parabola, b_parabola, c_parabola, fig, ax):
    ax.clear()
    f = (m_recta*x)+b_recta
    g = a_parabola*(x**exponente_parabola) + b_parabola*x + c_parabola

    #global f_resultado, g_resultado, ec_resultado
    f_resultado = lambdify(x, f)    
    g_resultado = lambdify(x, g)

    x_recta = recta(f_resultado, m_recta, e_dato, f_dato)[0]
    y_recta = recta(f_resultado, m_recta, e_dato, f_dato)[1]
    y_areaR = recta(f_resultado, m_recta, e_dato, f_dato)[2]

    x_parabola = parabola(g_resultado, e_dato, f_dato)[0]
    y_parabola = parabola(g_resultado, e_dato, f_dato)[1]
    x_areaP = parabola(g_resultado, e_dato, f_dato)[2]
    y_areaP = parabola(g_resultado, e_dato, f_dato)[3]

    # volum = volumen(f,g,ecuacion, e_dato, f_dato)

    ax.plot(x_recta, y_recta)
    ax.plot(x_parabola, y_parabola)
    #vol = volumen()
    # verts = [(e_dato, f_resultado(e_dato)), *zip(parabola()[2],parabola()[3]), (f_dato, f_resultado(f_dato))]
    # poly = Polygon(verts, facecolor='#ffA420', edgecolor='black', label = "hola")
    # ax.add_patch(poly)
    #print("Volumen:", vol, "u³")
    ax.fill_between(x_areaP, y_areaR, y_areaP, facecolor = '#ffA420', edgecolor='0.2', alpha = 0.5)
    ax.grid()
    #ax.set_title(("Volumen =", volum), color = 'w', fontsize=18, fontweight="bold")
    ax.set_xlabel("X", loc = 'right')
    ax.set_ylabel("Y", loc = 'top')