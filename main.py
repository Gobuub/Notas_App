import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser

st.set_page_config(layout='centered', page_icon='💡', page_title='Notas Bootcamp UAX')

st.title('INTRODUCCIÓN AL ANÁLISIS DE DATOS - by Ironhack & UAX')

st.image(Image.open('src/images/uax.png'))

st.sidebar.image(Image.open('src/images/ih.png'))

df = pd.read_csv('src/data/nota_final_all.csv')

st.caption('''
    Es hora de comprobar el resultado de todo el trabajo realizado durante el curso, como ya os dije estoy muy
    orgullo de vuestro trabajo durante todo el curso, pero para que no os olvidéis de mi tan facilmente he decidido
    poneros un último test, para comprobar de verdad he sido capaz de enseñaros algo y vosotros de aprenderlo.
    
    Este último test consiste en que comprobeis vuestra nota a partir de un código cifrado, para obtener el código,
    tendréis que escribir o 'codear' un algoritmo que cifre la primera parte de vuestro email, ese será el código único
    y exclusivo para cada uno de vosotros, y así únicamente vosotros podréis comprobar vuestra nota.
    
    Para cifrar el email tendreís que usar la técnica del cifrazo del César, en base 13
''')

caesar_cipher = '[Caesar Cypher](https://es.wikipedia.org/wiki/Cifrado_César)'

st.markdown(caesar_cipher, unsafe_allow_html=True)

mail = st.selectbox('email', df.email.unique())

if mail:
    st.text(mail)
    st.info('Comprueba que tu email es correcto antes de continuar')

sol = st.text_input('Introduce tú código')

if sol:

    st.info('Comprueba que tu código antes de continuar')
    st.text(sol)

    check = st.button('Comprobar')

    if check:

        code = df[df.email == mail]['code'].values

        if sol == code:

            nota = df[df.code == sol]['Total'].values[0]
            if nota > 5:
                st.text('ENHORABUENA')
                st.success(nota)
            else:
                st.warning('PODÍAS HABERLO HECHO MEJOR, ESTOY SEGURO, TOCA PONERSE A ESTUDIAR')
                st.error(nota)
        else:
            st.warning('EL CÓDIGO INTRODUCIDO NO ES VÁLIDO, PRUEBA DE NUEVO')