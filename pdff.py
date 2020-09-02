import itertools
import os, os.path
import glob
r = os.getcwdu()
os.chdir(r+"/pdf")
# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import styles
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Preformatted,\
            PageBreak, CondPageBreak, Flowable, Table, TableStyle, \
            NextPageTemplate, KeepTogether, Image, XPreformatted
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    page_num = canvas.getPageNumber()
    text = "Page #%s" % page_num
    canvas.drawRightString(200*mm, 20*mm, text)

story = []
canv = canvas.Canvas("plik.pdf", pagesize=landscape(A4))
width, height = landscape(A4)  # keep for later
story.append(canv.drawCentredString(width/2.0, height-108, "Simulacion"))


canv.setFillColorRGB(0, 0, 0.50)
canv.line(40, height - 60, width - 40, height - 60)
doc = SimpleDocTemplate("doc_page_num.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

stylesheet = styles.getSampleStyleSheet()
normalStyle = stylesheet["Normal"]

P = Paragraph("""<font color=red></font>""", normalStyle)
story.append(P)
datos = dict()
dias = 3
identificacion = 1
horas_atencion = 13
cantidad_intervalos = 2
total_clientes = 1200
distribuciones=[1,3,6,8,6,14,3,2,9,10]
cantidad_cajas_abiertas_cada_intervalo=30
minimo_productos=4
maximo_productos=5
promedio_seleccion=3
promedio_marcado = 4
promedio_pago = 3

datos = {
        "dias": dias,
        "identificacion" : identificacion,
        "horas_atencion" : horas_atencion,
        "cantidad_intervalos" : cantidad_intervalos,
        "total_clientes" : total_clientes,
        "distribuciones" : distribuciones,
        "cantidad_cajas_abiertas_cada_intervalo" : cantidad_cajas_abiertas_cada_intervalo,
        "minimo_productos" : minimo_productos,
        "maximo_productos" : maximo_productos,
        "promedio_seleccion" : promedio_seleccion,
        "promedio_marcado" : promedio_marcado,
        "promedio_pago" : promedio_pago
}

data = [
["Datos"],
["Dias", datos['dias']],
["Identificacion", str(datos['identificacion'])],
["Horas de atencion", str(datos['horas_atencion'])+" Horas"],
["Cantidad de intervalos", datos['cantidad_intervalos']],
["Total clientes", datos['total_clientes']],
["Distribuciones en %", str(datos['distribuciones'])],
["Cantidad de cajas abiertas por intervalo", datos['cantidad_cajas_abiertas_cada_intervalo']],
["Minimo de productos", datos['minimo_productos']],
["Maximo de productos", datos['maximo_productos']],
["Promedio de seleccion", str(datos['promedio_seleccion'])+" seg"],
["Promedio de marcado", str(datos['promedio_marcado'])+" seg"],
["Promedio de pago", str(datos['promedio_pago'])+" seg"]
]

t = Table(data, rowHeights=15, repeatCols=1)

t.setStyle(TableStyle([
("ALIGN", (0, 0), (-1, -1), "RIGHT"),
("ALIGN", (-2, 1), (-2, -1), "LEFT"),
("GRID", (0, 0), (-1, -1), 0.25, colors.black),
("BOX", (0, 0), (-1, -1), 0.25, colors.black),
("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),

]))
story.append(t)
story.append(t)
t.wrapOn(canv, 840, 300)
w, h = t.wrap(20, 20)
t.drawOn(canv, height/2, 250, 0)
print(width, height)
story.append(PageBreak())
doc.build(story, onFirstPage=addPageNumber, onLaterPages=addPageNumber)
canv.showPage()
canv.save()
