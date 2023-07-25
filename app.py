from textblob import TextBlob
import pandas as pd
import streamlit as st



st.header('Análisis de Sentimiento')
with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo',icon="😊")
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo',icon=':pensive:')
            st.warning('This is a warning', icon="⚠️")
        else:
            st.write( 'Es un sentimiento Neutral',icon='😔')
