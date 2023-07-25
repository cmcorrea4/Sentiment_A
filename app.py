from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext


st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo')
        else:
            st.write( 'Es un sentimiento Neutral')
