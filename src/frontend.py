import streamlit as st
import requests
import time

st.image('assets/header-iris.png')
st.title('Iris Classifier App')
st.markdown('*Created by Farrel Arrizal | Batch May 2024*')
st.divider()

st.markdown('Just type the value, and get the result :sunglasses: 😭')

with st.form(key='iris-form'):
    sepal_length = st.number_input('Sepal Length', min_value = 0, help='Input the numerical sepal length')
    sepal_width = st.number_input('Sepal Width', min_value = 0, help='Input the numerical sepal width')
    petal_length = st.number_input('Petal Length', min_value = 0, help='Input the numerical petal length')
    petal_width = st.number_input('Petal Width', min_value = 0, help='Input the numerical petal width')
    
    submit_button = st.form_submit_button('predict')
    
    if submit_button:
        # do something
        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
        
        # with spinner
        with st.spinner('Wait for it...'):
            # do something
            
            response = requests.post('http://backend:8000/predict', json=data)
            result = response.json()
            
            if response.status_code == 200:
                st.success(result['result'])
                st.balloons()
            else:
                st.error(result['detail_error'])
