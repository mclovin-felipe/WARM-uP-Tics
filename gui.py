from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
from simulacion import simulacion
from config import exportjson
from ppdf import generarpdf


class interfaz():
	def __init__(self):
		self.raiz = Tk()
		self.raiz.title("SuperC Mercado")
		#self.raiz.configure(width=1500,height=1500)
		self.raiz.geometry("657x720+0+0")
		self.raiz.resizable(width=False, height=False)

		self.desc = StringVar(value="descripcion generica de 60 caracteres")
		self.h_atencion = IntVar(value=1)
		self.pasos_simular = IntVar(value=1)
		self.clientes_dia = IntVar(value=1)
		
		self.distri_clientes0 = IntVar(value=1)
		self.distri_clientes1 = IntVar(value=1)
		self.distri_clientes2 = IntVar(value=1)
		self.distri_clientes3 = IntVar(value=1)
		self.distri_clientes4 = IntVar(value=1)
		self.distri_clientes5 = IntVar(value=1)
		self.distri_clientes6 = IntVar(value=1)
		self.distri_clientes7 = IntVar(value=1)
		self.distri_clientes8 = IntVar(value=1)
		self.distri_clientes9 = IntVar(value=1)

		self.caja_a0 = IntVar(value=1)
		self.caja_a1 = IntVar(value=1)
		self.caja_a2 = IntVar(value=1)
		self.caja_a3 = IntVar(value=1)
		self.caja_a4 = IntVar(value=1)
		self.caja_a5 = IntVar(value=1)
		self.caja_a6 = IntVar(value=1)
		self.caja_a7 = IntVar(value=1)
		self.caja_a8 = IntVar(value=1)
		self.caja_a9 = IntVar(value=1)
		
		self.min_pro = IntVar(value=1)
		self.max_pro = IntVar(value=1)
		self.ti_pro = IntVar(value=1)
		self.ti_caja = IntVar(value=1)
		self.ti_pago = IntVar(value=1)



		self.etiq1 = ttk.Label(self.raiz, text="Descripcion:")
		self.entry_desc = ttk.Entry(self.raiz, textvariable=self.desc, 
                              width=10)
		self.etiq2 = ttk.Label(self.raiz, text="Horas de Atencion:")
		self.entry1 = ttk.Entry(self.raiz, textvariable=self.h_atencion, 
                              width=10)
		self.etiq3 = ttk.Label(self.raiz, text="Pasos:")
		self.entry2 = ttk.Entry(self.raiz, textvariable=self.pasos_simular, 
                              width=10)
		self.etiq4 = ttk.Label(self.raiz, text="Clientes al dia:")
		self.entry3 = ttk.Entry(self.raiz, textvariable=self.clientes_dia, 
                              width=10)
		


		self.etiq5 = ttk.Label(self.raiz, text="Distribucion de clientes:")
		self.entry40 = ttk.Entry(self.raiz, textvariable=self.distri_clientes0, 
                              width=6)
		self.entry41 = ttk.Entry(self.raiz, textvariable=self.distri_clientes1, 
                              width=6)
		self.entry42 = ttk.Entry(self.raiz, textvariable=self.distri_clientes2, 
                              width=6)
		self.entry43 = ttk.Entry(self.raiz, textvariable=self.distri_clientes3, 
                              width=6)
		self.entry44 = ttk.Entry(self.raiz, textvariable=self.distri_clientes4, 
                              width=6)
		self.entry45 = ttk.Entry(self.raiz, textvariable=self.distri_clientes5, 
                              width=6)
		self.entry46 = ttk.Entry(self.raiz, textvariable=self.distri_clientes6, 
                              width=6)
		self.entry47 = ttk.Entry(self.raiz, textvariable=self.distri_clientes7, 
                              width=6)
		self.entry48 = ttk.Entry(self.raiz, textvariable=self.distri_clientes8, 
                              width=6)
		self.entry49 = ttk.Entry(self.raiz, textvariable=self.distri_clientes9, 
                              width=6)


		self.etiq6 = ttk.Label(self.raiz, text="Cajas abiertas por intervalo:")
		self.entry50 = ttk.Entry(self.raiz, textvariable=self.caja_a0, 
                              width=6)
		self.entry51 = ttk.Entry(self.raiz, textvariable=self.caja_a1, 
                              width=6)
		self.entry52 = ttk.Entry(self.raiz, textvariable=self.caja_a2, 
                              width=6)
		self.entry53 = ttk.Entry(self.raiz, textvariable=self.caja_a3, 
                              width=6)
		self.entry54 = ttk.Entry(self.raiz, textvariable=self.caja_a4, 
                              width=6)
		self.entry55 = ttk.Entry(self.raiz, textvariable=self.caja_a5, 
                              width=6)
		self.entry56 = ttk.Entry(self.raiz, textvariable=self.caja_a6, 
                              width=6)
		self.entry57 = ttk.Entry(self.raiz, textvariable=self.caja_a7, 
                              width=6)
		self.entry58 = ttk.Entry(self.raiz, textvariable=self.caja_a8, 
                              width=6)
		self.entry59 = ttk.Entry(self.raiz, textvariable=self.caja_a9, 
                              width=6)
		

		self.etiq7 = ttk.Label(self.raiz, text="Cantidad minima de productos:")
		self.entry6 = ttk.Entry(self.raiz, textvariable=self.min_pro, 
                              width=10)
		self.etiq8 = ttk.Label(self.raiz, text="Cantidad maxima de productos:")
		self.entry7 = ttk.Entry(self.raiz, textvariable=self.max_pro, 
                              width=10)
		self.etiq9 = ttk.Label(self.raiz, text="Tiempo de seleccion de productos:")
		self.entry8 = ttk.Entry(self.raiz, textvariable=self.ti_pro, 
                              width=10)
		self.etiq10 = ttk.Label(self.raiz, text="Tiempo de despacho de productos:")
		self.entry9 = ttk.Entry(self.raiz, textvariable=self.ti_caja, 
                              width=10)
		self.etiq11 = ttk.Label(self.raiz, text="Tiempo de pago de productos:")
		self.entry10 = ttk.Entry(self.raiz, textvariable=self.ti_pago, 
                              width=10)
		self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
		self.boton1 = ttk.Button(self.raiz, text="Salir", 
                                 command=quit)
		self.boton2 = ttk.Button(self.raiz, text="Generar simulacion",
								 command=self.pasar_variables)
		self.boton3 = ttk.Button(self.raiz, text="Generar pdf")
		self.boton4 = ttk.Button(self.raiz, text="Generar Json")
		self.boton5 = ttk.Button(self.raiz, text="Cargar Json",
								 command=self.abrir)



		self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry_desc.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.etiq3.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.entry2.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.etiq4.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.entry3.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		

		self.etiq5.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.entry40.place(x=160, y=265)
		self.entry41.place(x=210, y=265)
		self.entry42.place(x=260, y=265)
		self.entry43.place(x=310, y=265)
		self.entry44.place(x=360, y=265)
		self.entry45.place(x=410, y=265)
		self.entry46.place(x=460, y=265)
		self.entry47.place(x=510, y=265)
		self.entry48.place(x=560, y=265)
		self.entry49.place(x=610, y=265)		

		self.etiq6.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.entry50.place(x=160, y=300)
		self.entry51.place(x=210, y=300)
		self.entry52.place(x=260, y=300)
		self.entry53.place(x=310, y=300)
		self.entry54.place(x=360, y=300)
		self.entry55.place(x=410, y=300)
		self.entry56.place(x=460, y=300)
		self.entry57.place(x=510, y=300)
		self.entry58.place(x=560, y=300)
		self.entry59.place(x=610, y=300)
		

		self.etiq7.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry6.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.etiq8.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry7.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.etiq9.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry8.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.etiq10.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry9.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.etiq11.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.entry10.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5) 
		self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
		self.boton1.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=10, pady=10)
		#self.boton3.pack(side=RIGHT, fill=BOTH, expand=True, 
        #                 padx=10, pady=10)
		self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=10, pady=10)
		#self.boton4.pack(side=TOP, fill=BOTH, expand=True, 
        #                 padx=10, pady=10)
		self.boton5.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=10, pady=10)


		#self.raiz.configure(width=1500,height=15000)
		self.raiz.mainloop()

	def abrir(self, *args):
            self.raiz.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
            filetypes = (("json files",".json"),("all files",".*")))
            with open(self.raiz.filename) as data:
                datos = json.load(data)
            
            #print(datos["distribuciones"][0])
            self.distri_clientes0.set(datos["distribuciones"][0])
            self.distri_clientes1.set(datos["distribuciones"][1])
            self.distri_clientes2.set(datos["distribuciones"][2])
            self.distri_clientes3.set(datos["distribuciones"][3])
            self.distri_clientes4.set(datos["distribuciones"][4])
            self.distri_clientes5.set(datos["distribuciones"][5])
            self.distri_clientes6.set(datos["distribuciones"][6])
            self.distri_clientes7.set(datos["distribuciones"][7])
            self.distri_clientes8.set(datos["distribuciones"][8])
            self.distri_clientes9.set(datos["distribuciones"][9])

            self.caja_a0.set(datos["cantidad_cajas_abiertas_cada_intervalo"][0])
            self.caja_a1.set(datos["cantidad_cajas_abiertas_cada_intervalo"][1])
            self.caja_a2.set(datos["cantidad_cajas_abiertas_cada_intervalo"][2])
            self.caja_a3.set(datos["cantidad_cajas_abiertas_cada_intervalo"][3])
            self.caja_a4.set(datos["cantidad_cajas_abiertas_cada_intervalo"][4])
            self.caja_a5.set(datos["cantidad_cajas_abiertas_cada_intervalo"][5])
            self.caja_a6.set(datos["cantidad_cajas_abiertas_cada_intervalo"][6])
            self.caja_a7.set(datos["cantidad_cajas_abiertas_cada_intervalo"][7])
            self.caja_a8.set(datos["cantidad_cajas_abiertas_cada_intervalo"][8])
            self.caja_a9.set(datos["cantidad_cajas_abiertas_cada_intervalo"][9])

            self.h_atencion.set(datos["horas_atencion"])
            self.pasos_simular.set(datos["cantidad_intervalos"])
            self.clientes_dia.set(datos["total_clientes"])
            self.min_pro.set(datos["minimo_productos"])
            self.max_pro.set(datos["maximo_productos"])
            self.ti_pro.set(datos["promedio_seleccion"])
            self.ti_pago.set(datos["promedio_pago"])
            self.ti_caja.set(datos["promedio_marcado"])
            self.desc.set(datos["identificacion"])
      

	def pasar_variables(self, *args):
		if 	(int(self.h_atencion.get()) > 0 and
			int(self.pasos_simular.get()) > 0 and 
			int(self.clientes_dia.get()) > 0 and
			int(self.distri_clientes0.get()) > 0 and
			int(self.distri_clientes1.get()) > 0 and
			int(self.distri_clientes2.get()) > 0 and
			int(self.distri_clientes3.get()) > 0 and
			int(self.distri_clientes4.get()) > 0 and
			int(self.distri_clientes5.get()) > 0 and
			int(self.distri_clientes6.get()) > 0 and
			int(self.distri_clientes7.get()) > 0 and
			int(self.distri_clientes8.get()) > 0 and
			int(self.distri_clientes9.get()) > 0 and
			int(self.caja_a0.get()) > 0 and
			int(self.caja_a1.get()) > 0 and
			int(self.caja_a2.get()) > 0 and
			int(self.caja_a3.get()) > 0 and
			int(self.caja_a4.get()) > 0 and
			int(self.caja_a5.get()) > 0 and
			int(self.caja_a8.get()) > 0 and
			int(self.caja_a9.get()) > 0 and
			int(self.min_pro.get()) > 0 and
			int(self.max_pro.get()) > 0 and
			int(self.min_pro.get()) <= int(self.max_pro.get()) and
			int(self.ti_pro.get()) > 0 and
			int(self.ti_caja.get()) > 0 and
			int(self.ti_pago.get()) > 0) and (
			(int(self.distri_clientes0.get())+
			int(self.distri_clientes1.get())+
			int(self.distri_clientes2.get())+
			int(self.distri_clientes3.get())+
			int(self.distri_clientes4.get())+
			int(self.distri_clientes5.get())+
			int(self.distri_clientes6.get())+
			int(self.distri_clientes7.get())+
			int(self.distri_clientes8.get())+
			int(self.distri_clientes9.get()))==100):

				desc = self.desc.get()
				h_atencion = int(self.h_atencion.get())
				pasos_simular = int(self.pasos_simular.get())
				clientes_dia = int(self.clientes_dia.get())
				
				distri_clientes0 = int(self.distri_clientes0.get())
				distri_clientes1 = int(self.distri_clientes1.get())
				distri_clientes2 = int(self.distri_clientes2.get())
				distri_clientes3 = int(self.distri_clientes3.get())
				distri_clientes4 = int(self.distri_clientes4.get())
				distri_clientes5 = int(self.distri_clientes5.get())
				distri_clientes6 = int(self.distri_clientes6.get())
				distri_clientes7 = int(self.distri_clientes7.get())
				distri_clientes8 = int(self.distri_clientes8.get())
				distri_clientes9 = int(self.distri_clientes9.get())
				distri_clientes = []
				distri_clientes.append(distri_clientes0)
				distri_clientes.append(distri_clientes1)
				distri_clientes.append(distri_clientes2)
				distri_clientes.append(distri_clientes3)
				distri_clientes.append(distri_clientes4)
				distri_clientes.append(distri_clientes5)
				distri_clientes.append(distri_clientes6)
				distri_clientes.append(distri_clientes7)
				distri_clientes.append(distri_clientes8)
				distri_clientes.append(distri_clientes9)



				caja_a0 = int(self.caja_a0.get())
				caja_a1 = int(self.caja_a1.get())
				caja_a2 = int(self.caja_a2.get())
				caja_a3 = int(self.caja_a3.get())
				caja_a4 = int(self.caja_a4.get())
				caja_a5 = int(self.caja_a5.get())
				caja_a6 = int(self.caja_a6.get())
				caja_a7 = int(self.caja_a7.get())
				caja_a8 = int(self.caja_a8.get())
				caja_a9 = int(self.caja_a9.get())
				caja_a = []
				caja_a.append(caja_a0)
				caja_a.append(caja_a1)
				caja_a.append(caja_a2)
				caja_a.append(caja_a3)
				caja_a.append(caja_a4)
				caja_a.append(caja_a5)
				caja_a.append(caja_a6)
				caja_a.append(caja_a7)
				caja_a.append(caja_a8)
				caja_a.append(caja_a9)

			
				min_pro = int(self.min_pro.get())
				max_pro = int(self.max_pro.get())
				ti_pro = int(self.ti_pro.get())
				ti_caja = int(self.ti_caja.get())
				ti_pago = int(self.ti_pago.get())
				#ti_pago = 666
				#self.ti_pago.set(caja_a)
				print("Aceptado")
				clientesd1=[]
				datos = dict()
				datos ={
					"identificacion": desc,
					"horas_atencion": h_atencion,
					"cantidad_intervalos": pasos_simular,
					"total_clientes": clientes_dia,
					"distribuciones": distri_clientes,
					"cantidad_cajas_abiertas_cada_intervalo": caja_a,
					"minimo_productos": min_pro,
					"maximo_productos": max_pro,
					"promedio_seleccion": ti_pro,
					"promedio_marcado": ti_caja,
					"promedio_pago": ti_pago
				}
				result = simulacion(h_atencion,pasos_simular,clientes_dia,distri_clientes,caja_a,min_pro,max_pro, ti_pro, ti_caja,ti_pago)
				exportjson(desc,h_atencion,pasos_simular,clientes_dia,distri_clientes,caja_a,min_pro,max_pro, ti_pro, ti_caja,ti_pago)
				generarpdf(datos, result)
		else:
			print("Error, revisa el input")

def main():
    mi_app = interfaz()
    return 0

if __name__ == '__main__':
    main()