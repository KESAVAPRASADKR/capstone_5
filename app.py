import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Title of the app
st.title('Flat Resale Price Prediction')

with open('model_rfr.pkl', 'rb') as file:
    model = pickle.load(file)
col1,col2,col3=st.columns(3)
with col1:
    town_code={'ANG MO KIO':1, 'BEDOK':2, 'BISHAN':3, 'BUKIT BATOK':4, 'BUKIT MERAH':5,
        'BUKIT TIMAH':6, 'CENTRAL AREA':7, 'CHOA CHU KANG':8, 'CLEMENTI':9,
        'GEYLANG':10, 'HOUGANG':11, 'JURONG EAST':12, 'JURONG WEST':13,
        'KALLANG/WHAMPOA':14, 'MARINE PARADE':15, 'QUEENSTOWN':16, 'SENGKANG':17,
        'SERANGOON':18, 'TAMPINES':19, 'TOA PAYOH':20, 'WOODLANDS':21, 'YISHUN':22,
        'LIM CHU KANG':23, 'SEMBAWANG':24, 'BUKIT PANJANG':25, 'PASIR RIS':26,
        'PUNGGOL':27}
    town_selection = st.selectbox('Select town:', list(town_code.keys()))
    town= town_code[town_selection]
    bed_room_type={'1 ROOM':1, '3 ROOM':3, '4 ROOM':4, '5 ROOM':5, '2 ROOM':2, 'EXECUTIVE':3,
            'MULTI GENERATION':4, 'MULTI-GENERATION':4}
    bed_rooms_s=st.selectbox('Select bedrooms:', list(bed_room_type.keys()))
    bed_rooms=bed_room_type[bed_rooms_s]
    storey_range_code={'10 TO 12':4, '04 TO 06':2, '07 TO 09':3, '01 TO 03':1, '13 TO 15':5,
        '19 TO 21':7, '16 TO 18':6, '25 TO 27':9, '22 TO 24':8, '28 TO 30':10,
        '31 TO 33':11, '40 TO 42':14, '37 TO 39':13, '34 TO 36':12, '46 TO 48':16,
        '43 TO 45':15, '49 TO 51':17}
    storey_range_s=st.selectbox('Select floor range:', list(storey_range_code.keys()))
    storey_range=storey_range_code[storey_range_s]
    floor_area_sqm = st.number_input('Floor Area (sqm)', min_value=28)
with col2:
    pass
with col3:

    flat_model_code={'Normal':1, '3GEN':2, 'MODEL A':3, 'Duplexes':4, 'APARTMENT':5, 'TERRACE':6,
        '2-ROOM':7, 'MODEL A2':8, 'TYPE S1':9, 'TYPE S2':10}
    flat_model_s=st.selectbox('Select flat type:', list(flat_model_code.keys()))
    flat_model=flat_model_code[flat_model_s]
    lease_commence_date_options = [1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
                                1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 
                                1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 
                                1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                                2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                                2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    lease_commence_date = st.selectbox('Lease Commence Year', lease_commence_date_options)

    availabe_year=[1990,1991,1992,1993,1994,1995,1996, 1997, 1998, 1999, 2000,
                2001,2002, 2003, 2004, 2005,2006, 2007, 2008, 2009, 2010, 
                2011, 2012, 2013, 2014, 2015,2016, 2017, 2018, 2019, 2020, 
                2021, 2022, 2023]
    Available_year = st.selectbox('Year', availabe_year)
input_dic={'town':[town], 'bed_rooms':[bed_rooms], 'storey_range':[storey_range], 'floor_area_sqm':[floor_area_sqm], 
           'flat_model':[flat_model],'lease_commence_date':[lease_commence_date], 'Available_year':[Available_year]}
x_input=pd.DataFrame(input_dic)
if st.button('Predict Resale Price'):
    # Make prediction
    prediction = model.predict(x_input)
    st.write(f'The predicted resale price is: {prediction[0]:.2f}')
