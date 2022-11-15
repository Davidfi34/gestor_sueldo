from datetime import datetime
from fpdf import FPDF


#================ CREA RECIBO EN PDF ====================#
def pdf(parametros,usuario):

        now = datetime.now()
        fecha = str(now.day)+"-"+str(now.month)+"-"+str(now.year)

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()

        # TEXTO
        pdf.set_font('Arial', 'B', 16)
        # titulo
        pdf.cell(w = 0, h = 20, txt = 'La Empresa SRL', border = 2, ln=1,
                align = 'C', fill = 0)

        pdf.cell(w = 0, h = 10, txt = '', border = 2, ln=1,
                align = 'C', fill = 0)
        
        pdf.set_font('Arial', '', 14)
        
        pdf.cell(w = 0, h = 15, txt = 'Recibo de sueldo', border = 1, ln=1,
                align = 'C', fill = 0)
        pdf.cell(w = 0, h = 10, txt = (f"Fecha de emicion: {fecha}"), border = 1, ln=1,
                align = 'L', fill = 0)
        #DATOS PERSONALES
        pdf.cell(w = 0, h = 10, txt = (f"Apellido y Nombre: {usuario[0][2]} {usuario[0][1]}"), border = 1, ln=1,
                align = 'L', fill = 0)
        pdf.cell(w = 0, h = 10, txt = (f"DNI: {usuario[0][0]}"), border = 1, ln=1,
                align = 'L', fill = 0)
        pdf.cell(w = 0, h = 10, txt = (f"Categoria Nro:{usuario[0][7]}"), border = 1, ln=1,
                align = 'L', fill = 0)
        pdf.cell(w = 0, h = 10, txt = 'Liquidacion mes de Noviembre 2022', border = 1, ln=1,
                align = 'L', fill = 0)

        pdf.cell(w = 0, h = 10, txt = '', border = 2, ln=1,
                align = 'C', fill = 0)


        # encabezado
   
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(w = 70, h = 15, txt = 'Concepto', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 50, h = 15, txt = 'unidad', border = 1,
                align = 'C', fill = 0)

        pdf.multi_cell(w = 0, h = 15, txt = 'Deducciones', border = 1,
                align = 'C', fill = 0)


        # valores
        for valor in parametros:

                pdf.set_font('Arial', '', 12)

                pdf.cell(w = 70, h = 9, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)

                pdf.cell(w = 50, h = 9, txt = str(valor[1]), border = 1,
                        align = 'L', fill = 0)

                pdf.multi_cell(w = 0, h = 9, txt = str(valor[2]), border = 1,
                        align = 'L', fill = 0)
        
        
        url = str(usuario[0][0])+"-"+fecha

        #========= ENVIA PDF A LA CARPETA DESCARGA ========#
        pdf.output((f"descargas/recibo-{url}.pdf"))