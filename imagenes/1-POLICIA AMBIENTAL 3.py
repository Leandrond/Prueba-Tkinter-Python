from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import tkinter as tk
from io import open

def numero():
    doc = open("Archivo_denuncia.txt","r")#abrimos el archivo en modo lectura
    archivo = doc.read()#leemos el archivo
    registros = archivo.split("\n")#identificamos el final
    for registro in registros:     
        var = registro.split(",")   
        prueba = var[0]
        contador=int(prueba)+1
    doc.close
    return contador

#  VENTANAS 

def ventana2():
    #VENTANA 2 SELECCIONAR OPCIONES
    home = Tk()
    home.title("seleccionar")
    home.config(bg="white")
    home.iconbitmap("./Escudo_PA.ico")
    home.geometry("900x700")
    home.resizable(0,0)

                                                   #MARCO PAPA 1 - ENCABEZADO
    marco_papa = Frame(home, height=90, width=900)
    marco_papa.config(bg="white")
    marco_papa.pack(
        fill=X,
        anchor=N,
        side=TOP    
    )
    marco_papa.pack_propagate(False)

                                                      #MARCO PAPA 2 - CUERPO
    marco_papa_2 = Frame(home, height=610, width=900)
    marco_papa_2.config(bg="white")
    marco_papa_2.pack(
        fill=X,
        anchor=N,
        side=BOTTOM    
    )
    marco_papa_2.pack_propagate(False)

    #MARCO PARA EL TITULO
    marco = Frame(marco_papa,height=90)
    marco.config(bg="deepskyblue") 
    marco.pack(fill=X,
                anchor=N,
                side=TOP)
    marco.pack_propagate(False)

    #TITULO
    Titulo = Label(marco, text ="SELECCIONAR OPCION")
    Titulo.config(
                fg="white",
                bg="deepskyblue",
                font =("Inter", 24),
                pady=20,
                padx=20
                )
    Titulo.pack(anchor=W)

                                                                          #IMAGEN DE FONDO
    imagen_pantalla = Image.open("Imagen_ventana_2.jpg")
    imagen_pantalla = imagen_pantalla.resize((900,780), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(imagen_pantalla)
    imagen_pantalla_2 = Label(marco_papa_2, image= render_3 )
    imagen_pantalla_2.place(x=0, y=0)
    imagen_pantalla_2.config(bg="deepskyblue")
    
    #FUNCION PARA IR A LA VENTANA 4
    def nueva_ventana():
        home.destroy()
        ventana4()
                    #               BOTONES
    #BOTON PARA IR A MOSTRAR DENUNCIAS    
    boton = Button(home,
                    text="    MOSTRAR DENUNCIAS    ", font= ("inter", 12),
                    command=nueva_ventana) 
    boton.config(relief="raised", height=3, width=25)
    boton.place(x=330,y=350)
    boton.pack_propagate(False)

    #FUNCION PARA IR A LA VENTANA 4
    def nueva_ventana():
        home.destroy()
        ventana3()

    #BOTON PARA REALIZAR DENUNCIAS    
    boton = Button(home,
                    text="    REALIZAR DENUNCIA    ", font=("inter", 12),
                    command=nueva_ventana) 
    boton.config(relief="raised", height=3, width=25)
    boton.place(x=330,y=250)
    
    #FUNCION PARA VOLVER
    def nueva_ventana():
        home.destroy()
        ventana1()

    #BOTON VOLVER
    boton = Button(home,
                    text="    VOLVER    ",
                    command=nueva_ventana) 
    boton.config(relief="raised")
    boton.place(x=40,y=630)
    home.mainloop()
    
def ventana4():
    #VENTANA 4 LISTADO DE DENUNCIA
    home = Tk()
    home.title("listado")
    home.config(bg="white")
    home.iconbitmap("./Escudo_PA.ico")
    home.geometry("900x700")
    home.resizable(0,0)
    
   #MARCO PARA EL TITULO
    marco = Frame(home,height=90)
    marco.config(bg="deepskyblue") 
    marco.pack(fill=X,
                anchor=N,
                side=TOP)
    marco.pack_propagate(False)

    #Encabezado 
    Titulo = Label(marco, text ="LISTADO DE DENUNCIAS")
    Titulo.config(
                fg="white",
                bg="deepskyblue",
                font =("Inter", 24),
                pady=20,
                padx=20
                )
    Titulo.pack(anchor=W)
    #cuerpo
    def tabla():
        # creamos la el cuadro dentro de la ventana donde ira la cabla
        Cuadro_Tabla = Frame(home)
        # creamos la tabla con sus respectivas columnas
        Tabla= ttk.Treeview(Cuadro_Tabla)
        Tabla["column"] = (1,2,3,4,5,6,7,8,9,10,11,12,13)
        # pocicionamiento a la tabla
        Tabla.pack()
        Tabla.heading("#0",text="NUMERO DE DENUNCIA")
        # nombres de las tablas
        Tabla.heading("#1",text="NOMBRE Y APELLIDO")
        Tabla.heading("#2",text="TIPO DE DOCUMENTO")
        Tabla.heading("#3",text="NUMERO DE DOCUMENTO")
        Tabla.heading("#4",text="LOCALIDAD")
        Tabla.heading("#5",text="DOMICILIO")
        Tabla.heading("#6",text="TELEFONO")
        Tabla.heading("#7",text="E-MAIL")
        Tabla.heading("#8",text="TIPO DE DENUNCIA")
        Tabla.heading("#9",text="NOMBRE Y APELLIDO DEL DENUNCIADO")
        Tabla.heading("#10",text="DEPARTAMENTO")
        Tabla.heading("#11",text="LOCALIDAD")
        Tabla.heading("#12",text="DIRECCION DE DENUNCIA")
        Tabla.heading("#13",text="DESCRIPCION")
        #archivo
        doc = open("Archivo_denuncia.txt","r")#abrimos el archivo en modo lectura
        archivo = doc.read()#leemos el archivo
        registros = archivo.split("\n")#identificamos el final
        for registro in registros:     
            var = registro.split(",")
            Tabla.insert(parent="", index="end",text=(var[0]),values=((var[1]),(var[2]),(var[3]),(var[4]),(var[5]),(var[6]),(var[7]),(var[8]),(var[9]),(var[10]),(var[11]),(var[12]),(var[13])))
            doc.close
        # scrollbar-
        # creamos la barra de scroll con referencia a la tabla
        # scrollbar- X
        scrollbar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=Tabla.xview)
        Tabla.config(xscrollcommand=scrollbar.set)
        scrollbar.place(width=900,y=430,)
        
        Cuadro_Tabla.pack(padx=15,pady=100)

    # BOTON
    boton = Button(home,
                    text="      MOSTRAR DENUNCIAS     ",
                    command=tabla,font= ("inter", 12), fg="white",bd=2,) 
    boton.config(relief="raised", height=3, width=25, bg="deepskyblue")
    boton.place(x=320,y=620)
    
    #FUNCION PARA VOLVER
    def nueva_ventana():
        home.destroy()
        ventana2()

    #BOTON VOLVER
    boton = Button(home,
                    text="    VOLVER    ",
                    command=nueva_ventana) 
    boton.config(relief="raised")
    boton.place(x=40,y=630)
    
    home.mainloop()
 
def ventana1():
    # CREAMOS LA VENTANA
    home = Tk()
    # LE PONEMOS TITULO 
    home.title("POLICIA AMBIENTAL")
    #  ICONO DE LA VENTANA
    home.iconbitmap("./Escudo_PA.ico")
    # RESOLUCION
    home.geometry("900x700")
    # LE DAMOS UNA FUNCION PARA NO MAXIMISAR LA VENTANA, EVITANDO ERRORES DE DISEÑO
    home.resizable(0,0)

    #MARCO PAPA 1
    marco_papa = Frame(home, height=120, width=900)
    marco_papa.config(bg="deepskyblue")
    marco_papa.pack(
        fill=X,
        anchor=N,
        side=TOP    
    )
    marco_papa.pack_propagate(False)

    #MARCO PAPA 2
    marco_papa_2 = Frame(home, height=780, width=900)
    marco_papa_2.config(bg="gray")
    marco_papa_2.pack(
        fill=X,
        anchor=N,
        side=BOTTOM    
    )
    marco_papa_2.pack_propagate(False)

    #IMAGEN DE LA POLICIA AMBIENTAL
    imagen_policia = Image.open("policia-ambiental.png")
    imagen_policia = imagen_policia.resize((400,90), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(imagen_policia)
    imagen_policia_2 = Label(marco_papa, image= render )
    imagen_policia_2.place(x=15, y=10)
    imagen_policia_2.config(bg="deepskyblue")

    #IMAGEN DE CORDOBA
    imagen_cordoba = Image.open("isolo_cba.png")
    imagen_cordoba = imagen_cordoba.resize((380,90), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(imagen_cordoba)
    imagen_cordoba_2 = Label(marco_papa, image= render_2 )
    imagen_cordoba_2.place(x=510, y=10)
    imagen_cordoba_2.config(bg="deepskyblue")

    #IMAGEN DE FONDO
    imagen_pantalla = Image.open("Pantalla_inicio.jpg")
    imagen_pantalla = imagen_pantalla.resize((900,780), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(imagen_pantalla)
    imagen_pantalla_2 = Label(marco_papa_2, image= render_3 )
    imagen_pantalla_2.place(x=0, y=0)
    imagen_pantalla_2.config(bg="deepskyblue")

    #FUNCION PARA IR A LA VENTANA 2 (SELECCIONAR)
    def nueva_ventana():
        home.destroy()
        ventana2()
    
    #          BOTONES
    #BOTON PARA IR COMO USUARIO
    boton = Button(home,
                    text="    USUARIO    ", font=("inter", 12), fg="white", bd=2,
                    command=nueva_ventana) 
    boton.config(relief="raised", height=3, width=25, bg="deepskyblue")
    boton.place(x=180,y=360)
    #BOTON PARA INGRESAR COMO ADMIN
    boton = Button(home,
                    text="    ADMINISTRADOR    ", font= ("inter", 12), fg="white",bd=2,
                    ) 
    boton.config(relief="raised", height=3, width=25, bg="deepskyblue")
    boton.place(x=480,y=360)
    boton.pack_propagate(False)

    
    home.mainloop()

def ventana3():
                                             #VENTANA 3 CARGAR DATOS DE LA DENUNCIA
    home = Tk()
    home.title("REGISTRO DE DENUNCIAS")
    home.config(bg="white")
    home.iconbitmap("./Escudo_PA.ico")
    home.geometry("900x700")
    home.resizable(0,0)
                                                   #MARCO PAPA 1
    marco_papa = Frame(home, height=180, width=900)
    marco_papa.config(bg="white")
    marco_papa.pack(
        fill=X,
        anchor=N,
        side=TOP    
    )
    marco_papa.pack_propagate(False)
    #MARCO PARA EL TITULO
    marco = Frame(marco_papa,height=90)
    marco.config(bg="deepskyblue") 
    marco.pack(fill=X,
                anchor=N,
                side=TOP)
    marco.pack_propagate(False)
    #TITULO
    Titulo = Label(marco, text ="REALIZAR DENUNCIA")
    Titulo.config(
                fg="white",
                bg="deepskyblue",
                font =("Inter", 24),
                pady=20,
                padx=20
                )
    Titulo.pack(anchor=W)
    #MARCO PARA EL DENUNCIANTE
    marco2 = Frame(marco_papa,height=90,width=400)
    marco2.config(bg="white",) 
    marco2.pack(side=LEFT, anchor=NW)
    marco2.pack_propagate(False)
    #MARCO PARA LA DENUNCIA
    marco3 = Frame(marco_papa,height=90,width=500)
    marco3.config(bg="white") 
    marco3.pack(side=RIGHT, anchor=NE)
    marco3.pack_propagate(False)

    marco5 = Frame(marco3, height=50.4, width=430)
    marco5.config(bg="darkgray") 
    marco5.pack( anchor=CENTER, side=LEFT)
    marco5.pack_propagate(False)
                                                         #MARCO PAPA 2
    marco_papa2 = Frame(home, height=520, width=900)
    marco_papa2.config(bg="white")
    marco_papa2.pack(
        fill=X,
        anchor=N,
        side=BOTTOM
    )
    marco_papa2.pack_propagate(False)
    #MARCO PARA LOS CAMPOS
    marco4 = Frame(marco_papa2,height=520,width=900)
    marco4.config(bg="white") 
    marco4.pack(side=TOP, anchor=CENTER)
    marco4.pack_propagate(False)
    #ENCABEZADO DENUNCIANTE
    Encabezado_Denunciante = Label(marco2, text="Datos del denunciante")
    Encabezado_Denunciante.config(
        fg="black",
        bg="darkgray",
        font= ("Open Sans", 18),
        padx=30,
        pady=10
    )
    Encabezado_Denunciante.pack(anchor=W, padx=60, pady=20)
    #ENCABEZADO DENUNCIA
    Encabezado_Denuncia = Label(marco5, text="Datos de la denuncia")
    Encabezado_Denuncia.config(
        fg="black",
        bg="darkgray",
        font= ("Open Sans", 18),
        padx=30,
        pady=10,
        
    )
    Encabezado_Denuncia.pack(anchor=E, padx=60, pady=13)
                                                                 #input
    def entradas():
        #DENUNCIANTE ==========================================================================================================================
        # NOMBRE Y APELLIDO  ---------------------------------------------------------------------------------------------------------------------
        Texto_N_Apellido = Label(marco4,text="Nombre y apellido*",bg="white")
        Texto_N_Apellido.place(x=60,y=0)
        Campo_Nombre_Apellido_Denunciante=Entry(marco4, width=35,relief=tk.SUNKEN,bd=2)
        Campo_Nombre_Apellido_Denunciante.place(x=60,y=20)
        
        #  MENU DESPLEGABLE TIPO DE DOCUMENTO 
        # NUMERO DE DOCUMENTO---------------------------------------------------------------------------------------------------------------------

        Texto_N_Documento = Label(marco4,text="Numero de documento*",bg="white")
        Texto_N_Documento.place(x=60,y=100)
        Campo_N_Documento = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_N_Documento.place(x=60,y=120)
        
        Texto_Localidad = Label(marco4,text="Localidad",bg="white")
        Texto_Localidad.place(x=60,y=150)
        Campo_Localidad = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_Localidad.place(x=60,y=170)
        
        Texto_Domicilio = Label(marco4,text="Domicilio",bg="white")
        Texto_Domicilio.place(x=60,y=200)
        Campo_Domicilio = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_Domicilio.place(x=60,y=220)
        
        Texto_Telefono = Label(marco4,text="Telefono*",bg="white")
        Texto_Telefono.place(x=60,y=250)
        Campo_Telefono = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_Telefono.place(x=60,y=270)

        Texto_E_mail = Label(marco4, text="E-mail*",bg="white")
        Texto_E_mail.place(x=60,y=300)
        Campo_E_mail = Entry(marco4, width=35)
        Campo_E_mail.place(x=60,y=320)  

        # #=============================================================DENUNCIA =============================================================================
        # NOMBRE ----------------------------------------------------------------------------
        Texto_Nombre_Apellido_Denunciado = Label(marco4, text="Nombre y apellido del denunciado",bg="white")
        Texto_Nombre_Apellido_Denunciado.place(x=400,y=50)
        Campo_Nombre_Apellido_Denunciado = Entry(marco4,width=35, relief=tk.SUNKEN, bd=2)
        Campo_Nombre_Apellido_Denunciado.place(x=400,y=70)
        # DIRECCION ----------------------------------------------------------------------------
        Texto_Direccion = Label(marco4, text="Direccion",bg="white")
        Texto_Direccion.place(x=400,y=200)
        Campo_Direccion = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_Direccion.place(x=400,y=220)
        # DESCRIPCION ----------------------------------------------------------------------------
        Texto_Descripcion = Label(marco4, text="Descripcion",bg="white")
        Texto_Descripcion.place(x=650,y=50)
        Campo_Descripcion = Entry(marco4, width=35, relief=tk.SUNKEN, bd=2)
        Campo_Descripcion.place(x=650,y=70, height=70)
        # TIPO DE DOCUMENTO ----------------------------------------------------------------------------
        lista=[]
        doc = open("./2-Tipo_de_documento.txt","r")
        archivo = doc.read()
        registros = archivo.strip(",").split("\n")
        cont=0
        for registro in registros:  
            lista.append(registros[cont])
            cont+=1    
        doc.close
        # Combobox creation
        Texto_Descripcion = Label(marco4, text="Tipo de Documento",bg="white")
        Texto_Descripcion.place(x=60,y=50)
        Campo_T_Documento = tk.StringVar()
        opciones = ttk.Combobox(marco4, width = 32,textvariable = Campo_T_Documento)
        # Adding combobox drop down list
        opciones['values'] = (lista)
        opciones.place(x=60,y=70)
        # TIPO DE DENUNCIA ----------------------------------------------------------------------------
        lista=[]
        doc = open("./3-Tipo_de_denuncia.txt","r")
        archivo = doc.read()
        registros = archivo.strip(",").split("\n")
        cont=0
        for registro in registros:  
            lista.append(registros[cont])
            cont+=1    
        doc.close
        Texto_Descripcion = Label(marco4, text="Tipo de Denuncia",bg="white")
        Texto_Descripcion.place(x=400,y=0)
        # Combobox creation
        Tipo_de_denuncia = tk.StringVar()
        opciones = ttk.Combobox(marco4, width = 32,textvariable = Tipo_de_denuncia)
        # Adding combobox drop down list
        opciones['values'] = (lista)
        opciones.place(x=400,y=20)
        # DEPARTAMENTO ----------------------------------------------------------------------------
        lista=[]
        doc = open("./4-Departamentos.txt","r")
        archivo = doc.read()
        registros = archivo.strip(",").split("\n")
        cont=0
        for registro in registros:  
            lista.append(registros[cont])
            cont+=1    
        doc.close
        
        Texto_Descripcion = Label(marco4, text="Departamento",bg="white")
        Texto_Descripcion.place(x=400,y=100)
        # Combobox creation
        Departamento = tk.StringVar()
        opciones = ttk.Combobox(marco4, width = 32, textvariable = Departamento)
        # Adding combobox drop down list
        opciones['values'] = (lista)
        opciones.place(x=400,y=120)
        # LOCALIDADES ----------------------------------------------------------------------------
        lista=[]
        doc = open("./5-Localidades.txt","r")
        archivo = doc.read()
        registros = archivo.strip(",").split("\n")
        cont=0
        for registro in registros:  
            lista.append(registros[cont])
            cont+=1    
        doc.close
        
        Texto_Descripcion = Label(marco4, text="Localidad",bg="white")
        Texto_Descripcion.place(x=400,y=150)
        # Combobox creation
        Localidad = tk.StringVar()
        opciones = ttk.Combobox(marco4, width = 32, textvariable = Localidad)
        # Adding combobox drop down list
        opciones['values'] = (lista)
        opciones.place(x=400,y=170)
        
        # BOTON GUARDAR
      
        def boton_guardar():
            archivo = open("Archivo_denuncia.txt", "a")
            #-------------------------DENUNCIANTE--------------------------
            # 1 - NOMBRE Y APELLIDO
            valor1 = Campo_Nombre_Apellido_Denunciante.get()
            # 2 - TIPO DE DOCUMENTO
            valor2 = Campo_T_Documento.get()
            # 3 - NUMERO DE DOCUMENTO
            valor3 = Campo_N_Documento.get()
            # LOCALIDAD
            valor4 = Campo_Localidad.get() 
            # DOMICILIO
            valor5 = Campo_Domicilio.get()
            # TELEFONO
            valor6 = Campo_Telefono.get()
            # # E_MAIL
            valor7 = Campo_E_mail.get()
            #-------------------------DENUNCIADO--------------------------
            # TIPO DE DENUNCIA
            valor8 = Tipo_de_denuncia.get()
            # NOMBRE Y APELLIDO DENUNCIADO
            valor9 = Campo_Nombre_Apellido_Denunciado.get()
            # DEPARTAMENTO DENUNCIADO
            valor10 = Departamento.get()
            # LOCALIDAD DENUNCIADO
            valor11 = Localidad.get()
            # DIRECCION
            valor13 = Campo_Direccion.get()
            # DESCRIPCION
            valor14 = Campo_Descripcion.get()
            #  contador var[0]
            # agg el numero de denuncia
            archivo.write("\n"+str(numero())+","+valor1+","+valor2+","+valor3+","+valor4+","+valor5+","+valor6+","+valor7+","+valor8+","+valor9+","+valor10+","+valor11+","+valor13+","+valor14)
            archivo.close()
        
        boton = Button(home,
                        text="      GUARDAR    ",
                        command=boton_guardar,) 
        boton.config(relief="raised")
        boton.place(x=770,y=630)
    entradas()
    
    #BOTON CANCELAR

    def boton_cancelar():
        entradas()
        
    boton = Button(home,
                    text="    CANCELAR    ",
                    command=boton_cancelar) 
    boton.config(relief="raised")
    boton.place(x=650,y=630)
    
    #BOTON VOLVER

    def boton_volver():
        home.destroy()
        ventana2()
        
    boton = Button(home,
                    text="    VOLVER    ",
                    command=boton_volver) 
    boton.config(relief="raised")
    boton.place(x=40,y=630)


    #MOSTRAR VENTANA -3-
    home.mainloop()

ventana1()