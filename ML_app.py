import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier

#Loading up the Classification model we created
model = DecisionTreeClassifier(criterion='gini', max_depth=10, min_samples_leaf=5, random_state=0)
model = joblib.load('finalized_model.joblib')
#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(Buying, Maint,  Doors, Persons, Lug_boot, Safety):
    if Safety == 'med':
       safety = 1
    elif Safety == 'high':
         safety = 2
    elif Safety == 'low':
         safety = 3
    df = pd.DataFrame([[Buying, Maint, Doors, Persons, Lug_boot, safety]], columns=['Buying', 'Maint',  'Doors','Persons', 'Lug_boot', 'Safety'])
    prediction = model.predict([[Buying, Maint, Doors, Persons, Lug_boot, safety]])
    return prediction

st.title('Car Evaluation Classification')
st.image("""https://www.rolls-roycemotorcars.com/content/dam/rrmc/marketUK/rollsroycemotorcars_com/1-0-home/page-properties/rrmc-homepage-ghost-share-image.jpg""")
st.header('Enter the Information of the Car:')
st.text("vhigh = 1 high = 2 med = 3 low = 4")
Buying = st.number_input('buying:', min_value=1, max_value=4, value=1)
st.text("vhigh = 1 high = 2 med = 3 low = 4")
Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)
st.text("2-Doors = 1  3-Doors = 2 4-Doors = 3 5more = 4")
Doors = st.number_input('doors:', min_value=1, max_value=4, value=1)
st.text("2-persons = 1  4-persons = 2 more = 3 ")
Persons = st.number_input('persons:', min_value=1, max_value=3, value=1)
st.text("small = 1  med = 2 big = 3 ")
Lug_boot = st.number_input('lug_boot:', min_value=1, max_value=3, value=1)
Safety = st.radio('safety:', ('med', 'high', 'low'))

if st.button('Submit_Car_Infos'):
    cal_eval = predict(Buying, Maint, Doors, Persons, Lug_boot, Safety)
    st.success(f'The Evaluation of Car : {cal_eval[0]}')
