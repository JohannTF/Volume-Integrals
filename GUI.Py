import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from logic_2d import main2d
from logic_3d import main3d

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class GUI(customtkinter.CTk):
    def __init__(self, *args, fg_color="default_theme", **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        # Configurando variables para el grafico 3d inicial
        self.fig3d = plt.figure(figsize=(5,7))
        self.ax3d = plt.axes(projection = '3d')
        self.ax3d.set_xlabel("X", color = 'w')
        self.ax3d.set_ylabel("Y", color = 'w')
        self.ax3d.set_zlabel("Z", color = 'w')
        self.ax3d.set_title((r'$\int \:\int \:x^a+y^b+cxy$'), color = 'w', fontsize=18, fontweight="bold")
        self.ax3d.tick_params(labelcolor = 'w')
        self.ax3d.set_facecolor('#242424')
        self.fig3d.set_facecolor('#242424')
        self.ax3d.view_init(20,30)

        # Configurando variables para el grafico 2d inicial
        self.fig2d, self.ax2d  = plt.subplots(figsize=(4, 7))
        self.ax2d.set_xlabel("X", color = 'w', loc = 'right')
        self.ax2d.set_ylabel("Y", color = 'w', loc = 'top')
        self.ax2d.set_title((f"Grafica 2d"), color = 'w', fontsize=18, fontweight="bold")
        self.ax2d.tick_params(labelcolor = 'w')
        self.ax2d.set_facecolor('#242424', )
        self.fig2d.set_facecolor('#242424')
        self.ax2d.grid()

        # Configurando la ventana
        self.title("CustomTKinter complex_example.py")
        self.geometry(f"{1100}x{670}") #Ancho y largo

        # Configurando el diseño de la cuadricula
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.pack(pady = 20, padx = 20, fill = "both", expand = True)
        self.frame_main.rowconfigure(0, weight=1)
        self.frame_main.columnconfigure((0,1,2), weight=1)

        # Declarando la posición y los nuevos frames dentro del principal
        self.frame_graphic2d = customtkinter.CTkFrame(master = self.frame_main, width=350)
        self.frame_graphic2d.grid(row = 0, column = 0, padx=10, pady=10, sticky = "nwes")
        
        self.frame_userDatas = customtkinter.CTkFrame(master = self.frame_main, width=180)
        self.frame_userDatas.grid(row = 0, column = 1, padx=10, pady=10, sticky="nwes")

        self.frame_graphic3d = customtkinter.CTkFrame(master = self.frame_main, width=500)
        self.frame_graphic3d.grid(row = 0, column = 2, padx=10, pady=10, sticky = "nwes")

        # Ajustando el número de filas que contendra el frame para ingresar los datos del usuario
        self.frame_userDatas.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14),weight=1)
        self.frame_userDatas.columnconfigure((0,1,2,3,4,5,6,7), weigh = 0)
        self.frame_graphic2d.rowconfigure(0, weight=1)
        self.frame_graphic2d.columnconfigure(0, weight=1)
        self.frame_graphic3d.rowconfigure(0, weight=1)
        self.frame_graphic3d.columnconfigure(0, weight=1)
        
        # Para las variables de a-f
        self.mensaje1 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "Volumenes", text_font = ("timmana", 24), justify = "center").grid(row = 0, columnspan = 8, sticky="nwes")
        self.mensaje2 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "a =", text_font = ("Arial", 14), width=10).grid(row=1, column = 0, sticky="e", padx = 10)
        self.mensaje3 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "b =", text_font = ("Arial", 14), width=10).grid(row=2, column=0, sticky="e", padx = 10)
        self.mensaje4 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "c =", text_font = ("Arial", 14), width=10).grid(row=3, column=0, sticky="e", padx = 10)
        self.mensaje5 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "e =", text_font = ("Arial", 14), width=10).grid(row=4, column = 0, sticky="e", padx = 10)
        self.mensaje6 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "f =", text_font = ("Arial", 14), width=10).grid(row=5, column=0, sticky="e", padx = 10)
        # Para insertar la ecuación de la recta
        self.mensaje7 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "y = ", text_font = ("Arial", 14), width=10).grid(row=7, column=0, sticky="e")
        self.mensaje7 = customtkinter.CTkLabel(master = self.frame_userDatas, text = r'x +', text_font = ("Arial", 14), width=10).grid(row=7, column=2, sticky="w")
        # Para insertar la ecuación de la parabola
        self.mensaje8 = customtkinter.CTkLabel(master = self.frame_userDatas, text = "y = ", text_font = ("Arial", 14), width=10).grid(row=10, column=0, sticky="e")
        self.mensaje9 = customtkinter.CTkLabel(master = self.frame_userDatas, text = r'x', text_font = ("Arial", 14), width=10).grid(row=10, column=2, sticky="w")
        self.mensaje10 = customtkinter.CTkLabel(master = self.frame_userDatas, text = r'+', text_font = ("Arial", 14), width=3).grid(row=10, column=4, sticky="w")
        self.mensaje11 = customtkinter.CTkLabel(master = self.frame_userDatas, text = r'x +', text_font = ("Arial", 14), width=10).grid(row=10, column=6, sticky="w")

        self.a_dato = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.a_dato.grid(row = 1, column = 1)
        
        self.b_dato = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.b_dato.grid(row = 2, column = 1)
        
        self.c_dato = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.c_dato.grid(row = 3, column = 1)
        
        self.e_dato = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.e_dato.grid(row = 4, column = 1, padx=0)

        self.f_dato = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.f_dato.grid(row = 5, column = 1, padx=0)
        
        self.m_recta = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.m_recta.grid(row = 7, column = 1)
        
        self.b_recta = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.b_recta.grid(row = 7, column = 3)

        self.a_parabola = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.a_parabola.grid(row = 10, column = 1)

        self.exponente_parabola = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.exponente_parabola.grid(row = 10, column = 3, sticky = "nw")

        self.b_parabola = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.b_parabola.grid(row = 10, column = 5, sticky = "w")

        self.c_parabola = customtkinter.CTkEntry(master = self.frame_userDatas, justify = "center", width=40)
        self.c_parabola.grid(row = 10, column = 7, sticky = "w")

        self.bottom = customtkinter.CTkButton(master = self.frame_userDatas, text="Calcular", command=self.envioDatos, cursor = 'hand2').grid(row = 12, columnspan = 8, sticky="nsew",pady = 10)
        
        # Para insertar el gráfico en la interfaz
        self.canvas3d = FigureCanvasTkAgg(self.fig3d, master = self.frame_graphic3d)
        self.canvas3d.draw()
        self.canvas3d.get_tk_widget().grid(row = 0, column=0, sticky="nwes")

        self.canvas2d = FigureCanvasTkAgg(self.fig2d, master = self.frame_graphic2d)
        self.canvas2d.draw()
        self.canvas2d.get_tk_widget().grid(row = 0, column=0, sticky="nwes")

        customtkinter.CTkLabel(master = self.frame_userDatas, text = "", text_font = ("Arial", 8), justify = "center").grid(row=14, columnspan = 8, sticky="nwes")

    def envioDatos(self):
        a = b = c = e = f = mRecta = bRecta = aParabola = expParabola = bParabola = cParabola = None
        try:
            customtkinter.CTkLabel(master = self.frame_userDatas, text = "", text_font = ("Arial", 8), justify = "center").grid(row=14, columnspan = 8, sticky="nwes")
            a = int(self.a_dato.get())
            b = int(self.b_dato.get())
            c = int(self.c_dato.get())
            e = int(self.e_dato.get())
            f = int(self.f_dato.get())
            mRecta = int(self.m_recta.get())
            bRecta = int(self.b_recta.get())
            aParabola = int(self.a_parabola.get())
            expParabola = int(self.exponente_parabola.get())
            bParabola = int(self.b_parabola.get())
            cParabola = int(self.c_parabola.get())
            main2d(a, b, c, e, f, mRecta, bRecta, aParabola, expParabola, bParabola, cParabola, self.fig2d, self.ax2d)
            self.canvas2d.draw()
            self.canvas2d.get_tk_widget().grid(row = 0, column = 0)
            main3d(a, b, c, e, f, mRecta, bRecta, aParabola, expParabola, bParabola, cParabola, self.fig3d, self.ax3d)
            self.canvas3d.draw()
            self.canvas3d.get_tk_widget().grid(row = 0, column = 0)
        except(ValueError):
            if((a or b or c or e or f or mRecta or bRecta or aParabola or expParabola or bParabola or cParabola) == None):
                customtkinter.CTkLabel(master = self.frame_userDatas, text = "Faltan parametros!", text_font = ("Arial", 8), fg_color = 'red', justify = "center").grid(row=14, columnspan = 8, sticky="nwes")
            else:
                customtkinter.CTkLabel(master = self.frame_userDatas, text = "Solo Valores Enteros!", text_font = ("Arial", 8), fg_color = 'red', justify = "center").grid(row=14, columnspan = 8, sticky="nwes")
        except(ZeroDivisionError):
            customtkinter.CTkLabel(master = self.frame_userDatas, text = "Hay una indeterminación!", text_font = ("Arial", 8), fg_color = 'red', justify = "center").grid(row=14, columnspan = 8, sticky="nwes")

interfaz = GUI()
interfaz.mainloop()