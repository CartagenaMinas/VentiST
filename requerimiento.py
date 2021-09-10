import streamlit as st
from PIL import Image

    
def main():
    st.title('Requerimiento de Aire en Mina Subterránea D.S. N° 023-2017-EM')
    col1, col2 = st.columns([3, 1])
    #col1.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    col1.markdown("<div style='text-align: justify'>En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú.</div>", unsafe_allow_html=True)
    col1.markdown('### CÁLCULO DE REQUERIMIENTO DE AIRE')
    tipo = ['Operación con equipo de motor petrolero', 'Operación sin equipo de motor petrolero']
    opcion = col1.selectbox("Tipo de operación subterránea:", tipo)
    image = Image.open('imagenes/capture.jpg')
    col2.image(image, caption='Ventilación en minería subterránea')

    
    

    if opcion == 'Operación con equipo de motor petrolero':
        st.write('## REQUERIMIENTO DE AIRE TOTAL (QTo).- Cuando en la operación se utilice equipos con motor petrolero:')
        with st.expander("REQUERIMIENTO DE AIRE", expanded=True):
            st.write('La demanda de aire al interior de la mina debe ser calculada de acuerdo al literal d) del artículo 252 del reglamento, considerando la fórmula siguiente:')
            image1 = Image.open('imagenes/rsz_1.jpg')
            st.image(image1)
            st.info("""
            - Donde:
            - QTo = Caudal total para la operación
            - QT1 = La sumatoria de caudal requerido por:
            - a) El número de trabajadores (QTr)
            - b) El consumo de madera (QMa)
            - c) Temperatura en labores de trabajo (QTe)
            - d) Equipos con motor petrolero (QEq)
            - QFu = 15% del QT1
            """)
            st.write("**a) Caudal requerido por el número de trabajadores (QTr)**")
            image2 = Image.open('imagenes/rsz_2.jpg')
            st.image(image2)
            st.info("""
            - Donde:
            - QTr = Caudal total para “n” trabajadores (m³/min)
            - F = Caudal mínimo por persona de acuerdo a escala establecida en el artículo 247 del reglamento
            - N = Número de trabajadores de la guardia más numerosa
            """)
            image14 = Image.open('imagenes/rsz_14.jpg')
            st.image(image14)
            st.write("**b) Caudal requerido por el consumo de madera (QMa)**")
            image3 = Image.open('imagenes/rsz_3.jpg')
            st.image(image3)
            st.info("""
            - Donde:
            - QMa = Caudal requerido por toneladas de producción (m3/min)
            - u = Factor de producción, de acuerdo a escala establecida en el segundo párrafo del literal d) del artículo 252 del reglamento
            - T = Producción en toneladas métricas húmedas por Guardia.
            """)
            image4 = Image.open('imagenes/rsz_4.jpg')
            st.image(image4)
            st.write("**c) Caudal requerido por temperatura en las labores de trabajo (QTe)**")
            image5 = Image.open('imagenes/rsz_5.jpg')
            st.image(image5)
            st.info("""
            - Donde:
            - QTe = Caudal por temperatura (m³/min)
            - Vm = Velocidad mínima
            - A = Área de la labor promedio.
            - N = Número de niveles con temperatura mayor a 23°C, de acuerdo a escala establecida en el tercer párrafo del literal d) del artículo 252 del reglamento.
            """)
            image6 = Image.open('imagenes/rsz_6.jpg')
            st.image(image6)

            st.write("**d) Caudal requerido por equipo con motor Petrolero (QEq)    **")
            image7 = Image.open('imagenes/rsz_7.jpg')
            st.image(image7)
            st.info("""
            - Donde:
            - QEq = Volumen de aire necesario para la ventilación (m3/min)
            - HP = Capacidad efectiva de potencia (HPs)
            - Dm = Disponibilidad mecánica promedio de los equipos (%)
            - Fu = Factor de utilización promedio de los equipos (%)
            """)

            st.write("**e) Caudal requerido por fugas (QFu)**")
            image8 = Image.open('imagenes/rsz_8.jpg')
            st.image(image8)
            st.write("Donde:")
            image9 = Image.open('imagenes/rsz_9.jpg')
            st.image(image9)



    elif opcion == 'Operación sin equipo de motor petrolero':
        st.write('## REQUERIMIENTO DE AIRE TOTAL (QTo).- Cuando en la operación no se utilicen equipos con motor petrolero')
        with st.expander("REQUERIMIENTO DE AIRE", expanded=True):
            st.write('Debe calcularse el caudal total para la operación conforme la fórmula que se detalla a continuación y luego **compararla con el caudal por el consumo de explosivos. Luego de obtener cada uno de los valores se determina como Requerimiento de Aire Total el de mayor valor**. La demanda de aire al interior de la mina debe ser calculada de acuerdo al literal d) del artículo 252 del reglamento, considerando la fórmula siguiente:')
            image11 = Image.open('imagenes/rsz_11.jpg')
            st.image(image11)
            st.info("""
            - Donde:
            - QTo = Caudal total para la operación
            - QT1 = La sumatoria de caudal requerido por:
            - a) el número de trabajadores (QTr)
            - b) el consumo de madera (QMa)
            - c) temperatura en labores de trabajo (QTe)
            - QFu = 15% del QT1
            """)
            st.write("**a) Caudal requerido por el número de trabajadores (QTr)**")
            image2 = Image.open('imagenes/rsz_2.jpg')
            st.image(image2)
            st.info("""
            - Donde:
            - QTr = Caudal total para “n” trabajadores (m³/min)
            - F = Caudal mínimo por persona de acuerdo a escala establecida en el artículo 247 del reglamento
            - N = Número de trabajadores de la guardia más numerosa
            """)
            image14 = Image.open('imagenes/rsz_14.jpg')
            st.image(image14)
            st.write("**b) Caudal requerido por el consumo de madera (QMa)**")
            image3 = Image.open('imagenes/rsz_3.jpg')
            st.image(image3)
            st.info("""
            - Donde:
            - QMa = Caudal requerido por toneladas de producción (m3/min)
            - u = Factor de producción, de acuerdo a escala establecida en el segundo párrafo del literal d) del artículo 252 del reglamento
            - T = Producción en toneladas métricas húmedas por Guardia.
            """)
            image4 = Image.open('imagenes/rsz_4.jpg')
            st.image(image4)
            st.write("**c) Caudal requerido por temperatura en las labores de trabajo (QTe)**")
            image5 = Image.open('imagenes/rsz_5.jpg')
            st.image(image5)
            st.info("""
            - Donde:
            - QTe = Caudal por temperatura (m³/min)
            - Vm = Velocidad mínima
            - A = Área de la labor promedio.
            - N = Número de niveles con temperatura mayor a 23°C, de acuerdo a escala establecida en el tercer párrafo del literal d) del artículo 252 del reglamento.
            """)
            image6 = Image.open('imagenes/rsz_6.jpg')
            st.image(image6)


            st.write("**d) Caudal requerido por fugas (QFu)**")
            image8 = Image.open('imagenes/rsz_8.jpg')
            st.image(image8)
            st.write("Donde:")
            image12 = Image.open('imagenes/rsz_12.jpg')
            st.image(image12)

            st.write("**e) Caudal requerido por consumo de explosivo (QEx)**")
            st.write("Cuando en la operación no se utilicen equipos con motor petrolero, debe calcularse y tenerse en cuenta la necesidad de aire requerido por consumo de explosivos, conforme lo siguiente:")
            image13 = Image.open('imagenes/rsz_13.jpg')
            st.image(image13)
            st.info("""
            - Donde:
            - Qex = Caudal de aire requerido por consumo de explosivo detonado (m3/min)
            - A = Área promedio de labores (m2)
            - V = Velocidad mínima requerida según norma (m/min)
            - N = Número de niveles en voladura
            """)





