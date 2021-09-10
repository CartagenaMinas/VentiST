import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

ccfm=35.314699885085965
    
def calculo():
    st.title('Calculo de Requerimiento de Aire en Mina')
    st.write('## REQUERIMIENTO DE AIRE TOTAL (QTo).- Cuando en la operación se utilice equipos con motor petrolero:')
    ###########################################################################
    st.write("**a) Caudal requerido por el número de trabajadores (QTr)**")
    col1, col2 = st.columns([2, 2])
    image2 = Image.open('imagenes/2.jpg')
    col1.image(image2)
    with col1.expander("Info", expanded=False):
        st.info("""
        - Donde:
        - QTr = Caudal total para “n” trabajadores (m³/min)
        - F = Caudal mínimo por persona de acuerdo a escala establecida en el artículo 247 del reglamento
        - N = Número de trabajadores de la guardia más numerosa
        """)
    image14 = Image.open('imagenes/14.jpg')
    col1.image(image14)
    F = col2.number_input('Caudal mínimo',value=4)
    N = col2.number_input('Número de trabajadores',value=428)
    Qtr=F*N
    cfmqtr=Qtr*ccfm
    a = np.array([[Qtr, round(cfmqtr)]])
    df = pd.DataFrame(a, index = ['Qtr'], columns=['m³/min', 'CFM'])
    col2.dataframe(df.style.format("{:.1f}"))
    st.write("  ")
    st.write("  ")
    ##########################################################################
    st.write("**b) Caudal requerido por el consumo de madera (QMa)**")
    col1, col2 = st.columns([2, 2])
    image3 = Image.open('imagenes/3.jpg')
    col1.image(image3)
    with col1.expander("Info", expanded=False):
        st.info("""
        - Donde:
        - QMa = Caudal requerido por toneladas de producción (m3/min)
        - u = Factor de producción, de acuerdo a escala establecida en el segundo párrafo del literal d) del artículo 252 del reglamento
        - T = Producción en toneladas métricas húmedas por Guardia.
        """)
    image4 = Image.open('imagenes/4.jpg')
    col1.image(image4)
    T = col2.number_input('Factor de producción',value=10000)
    u = col2.number_input('Producción por Guardia',value=0)
    Qma=T*u
    cfmqma=Qma*ccfm
    a=np.append(a, [[Qma, round(cfmqma)]], axis= 0)
    df1 = pd.DataFrame(a, index = ['Qtr','Qma'], columns=['m³/min', 'CFM'])
    col2.dataframe(df1[1:].style.format("{:.1f}"))
    st.write("  ")
    st.write("  ")
    #########################
    st.write("**c) Caudal requerido por temperatura en las labores de trabajo (QTe)**")
    col1, col2 = st.columns([2, 2])
    image5 = Image.open('imagenes/5.jpg')
    col1.image(image5)
    with col1.expander("Info", expanded=False):
        st.info("""
        - Donde:
        - QTe = Caudal por temperatura (m³/min)
        - Vm = Velocidad mínima
        - A = Área de la labor promedio.
        - N = Número de niveles con temperatura mayor a 23°C, de acuerdo a escala establecida en el tercer párrafo del literal d) del artículo 252 del reglamento.
        """)
    image6 = Image.open('imagenes/6.jpg')
    col1.image(image6)
    vm = col2.number_input('Velocidad mínima',value=30)
    A = col2.number_input('Área de la labor promedio',value=21.375)
    ma_N=col2.number_input('Número de niveles con temperatura mayor a 23°C',value=16)
    Qte=vm*A*ma_N
    cfmqte=Qte*ccfm
    a=np.append(a, [[Qte, round(cfmqte)]], axis= 0)
    df2 = pd.DataFrame(a, index = ['Qtr','Qma','Qte'], columns=['m³/min', 'CFM'])
    col2.dataframe(df2[2:].style.format("{:.1f}"))
    st.write("  ")
    st.write("  ")
    #########################
    st.write("**d) Caudal requerido por equipo con motor Petrolero (QEq)    **")
    col1, col2 = st.columns([2, 2])
    image7 = Image.open('imagenes/7.jpg')
    col1.image(image7)
    with col1.expander("Info", expanded=False):
        st.info("""
        - Donde:
        - QEq = Volumen de aire necesario para la ventilación (m3/min)
        - HP = Capacidad efectiva de potencia (HPs)
        - Dm = Disponibilidad mecánica promedio de los equipos (%)
        - Fu = Factor de utilización promedio de los equipos (%)
        """)
    image15= Image.open('imagenes/15.jpg')
    col1.image(image15)
    hp = col2.number_input('Total de HP efectivos',value=303.8)
    with col2.expander("Advertencia", expanded=True):
        st.info("""
        - Se debe de calcular el cuadro que se ejemplifica en el lado izquierdo según la mina que se esté trabajando
        """)
    Qeq=3*hp
    cfmqte=Qeq*ccfm
    a=np.append(a, [[Qeq, round(cfmqte)]], axis= 0)
    df3 = pd.DataFrame(a, index = ['Qtr','Qma','Qte','Qeq'], columns=['m³/min', 'CFM'])
    col2.dataframe(df3[3:].style.format("{:.1f}"))
    st.write("  ")
    st.write("  ")
    #############################################
    st.write("**e) Caudal requerido por fugas (QFu)**")
    image9 = Image.open('imagenes/9.jpg')   
    st.image(image9)
    image8 = Image.open('imagenes/8.jpg')
    st.image(image8)
    image1 = Image.open('imagenes/1.jpg')
    st.image(image1)
    dfs=df3.sum().values
    dfs=pd.DataFrame(dfs,columns=["Qt1"], index =['m³/min', 'CFM'])
    dfs["Qfu"]=(dfs["Qt1"]*0.15)
    dfs['Qto']=dfs['Qt1']+dfs["Qfu"]
    st.dataframe(dfs.style.format("{:.1f}"))
    #############################

