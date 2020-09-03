from fpdf import FPDF
import os, os.path
import glob
def generarpdf(datos, result):


    pdf = FPDF()

    #header of the pdf file
    header = 'Reporte Simulación'
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    w = pdf.get_string_width(header) + 6
    pdf.set_x((210 - w) / 2)
    pdf.cell(w, 9, header, 0, 0, 'C')
    pdf.line(20, 18, 210-20, 18)

    pdf.ln(10)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 5, ' Datos de configuración: ')
    pdf.multi_cell(0, 5, ' Descripción: '+ datos['identificacion'])
    pdf.multi_cell(0, 5, ' Horas de atención: '+ str(datos['horas_atencion']))
    pdf.multi_cell(0, 5, ' Cantidad de intervalos: '+ str(datos['cantidad_intervalos']))
    pdf.multi_cell(0, 5, ' Total declientes: '+ str(datos['total_clientes']))
    pdf.multi_cell(0, 5, ' Distribuciones: '+ str(datos['distribuciones']))
    pdf.multi_cell(0, 5, ' Cantidad de cajas_abiertas: '+ str(datos['cantidad_cajas_abiertas_cada_intervalo']))
    pdf.multi_cell(0, 5, ' Minimo de_productos: ' + str(datos['minimo_productos']))
    pdf.multi_cell(0, 5, ' Maximo_de productos: ' + str(datos['maximo_productos']))
    pdf.multi_cell(0, 5, ' Promedio_seleccion: ' + str(datos['promedio_seleccion']))
    pdf.multi_cell(0, 5, ' promedio_marcado: ' + str(datos['promedio_marcado']))
    pdf.multi_cell(0, 5, ' Promedio_pago: ' + str(datos['promedio_pago']))
    pdf.multi_cell(0, 5, ' -------------------------------------------------')


    for i in range(10):

        pdf.ln()
        pdf.set_font('Arial', '', 12)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(0, 6, 'Resultados intervalo: '+str(result[i][0]), 0, 1, 'L', 1)

        pdf.ln(10)
        pdf.set_font('Times', '', 12)
        pdf.multi_cell(0, 5, ' La cantidad de clientes ingresados es: ' + str(result[i][1]))
        pdf.multi_cell(0, 5, ' La cantidad de clientes despachados es: ' + str(result[i][2]))
        pdf.multi_cell(0, 5, ' El promedio de productos por cliente despachado es: ' + str(result[i][3]))
        pdf.multi_cell(0, 5, ' El promedio de clientes en espera en colas de caja es: ' + str(result[i][4]))
        pdf.multi_cell(0, 5, ' La longitud maxima de cola de espera en caja fue de: ' + str(result[i][5]))
    pdf.ln()
    pdf.set_font('Arial', '', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 6, 'Tiempo total simulado: ' + str(result[1][6])+ ' minutos.', 0, 1, 'L', 1)

    #pdf.set_y(0) #on top of the page
    pdf.set_y(-30) #30 CM from the bottom of the page
    pdf.set_font('Arial', '', 8)
    pdf.set_text_color(0)
    pdf.cell(0, 5, 'Page ' + str(pdf.page_no()), 0, 0, 'C')

    dir = os.getcwd() + "/*.pdf"
    Numero = len(glob.glob(str(dir)))
    Numero += 1
    pdf.output('resultados'+str(Numero)+'.pdf', 'F')