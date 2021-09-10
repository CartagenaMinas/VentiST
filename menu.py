import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def principal():
    lgit = """<a href='https://github.com/CartagenaMinas/VentiST' target="_blank">Github</a>"""
    st.title('CÁLCULO DEL CAUDAL DE AIRE MINA')
    st.write("")
    st.write("")
    col1, col2 = st.columns([2, 2])
    #col1.write('Bienvenidos en esta app donde se podra calcular el requerimiento de aire necesario para Minería Subterránea.')
    #col1.write(f'\n  Si quieres quieres conocer el codigo de esta app escrito en python puedes visitarlo en el siguiente enlace de {lgit}.', unsafe_allow_html=True)
    #col1.write("Tambien puedes visitar nuestra pagina web IDL Mining donde subimos post sobre programacion orientado a la ingeniera de minas y nos dedicamos a la creacion de Modelos de Deep Learning.")
    col1.markdown("<div style='text-align: justify'>Bienvenidos en esta app donde se podra calcular el requerimiento de aire necesario para Minería Subterránea.</div>", unsafe_allow_html=True)
    col1.markdown("<div style='text-align: justify'>Si quieres quieres conocer el codigo de esta app escrito en python puedes visitarlo en el siguiente enlace <a style='color:black; font-size:110% ;' href='https://github.com/CartagenaMinas/VentiST' target='_blank'><i class='fa fa-rocket'></i>GitHub</a> </div>", unsafe_allow_html=True)
    col1.markdown("<div style='text-align: justify'>Tambien puedes visitar nuestra pagina web IDL Mining donde subimos post sobre programacion orientado a la ingeniera de minas y nos dedicamos a la creacion de Modelos de Deep Learning.</div>", unsafe_allow_html=True)
    
    image = Image.open('imagenes/rsz_31.jpg')
    col2.write("")
    col2.image(image, caption='Ventilación en minería subterránea')
    st.write('### CREATED BY CRISTIAN CARTAGENA MATOS')
    components.html(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <a style="color:black; font-size:110% ;" href="https://www.linkedin.com/in/cristiancartagenamatos/" target="_blank"><i class="fa fa-linkedin-square"></i>Linkedin</a>
        <a style="color:black; font-size:110% ;" href="https://github.com/CartagenaMinas" target="_blank"><i class="fa fa-github"></i>Github</a>
        <a style="color:black; font-size:110% ;" href="http://www.idlmining.com/" target="_blank"><i class="fa fa-rocket"></i>IDL Mining</a>
        """  , height=600)
    #link = '[GitHub](https://github.com/CartagenaMinas)'
    #st.markdown(link, unsafe_allow_html=True)

