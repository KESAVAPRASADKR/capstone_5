import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

# Load the trained model
with open('model_s_flat.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Resale Price Prediction')
town_options = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                'TOA PAYOH', 'WOODLANDS', 'YISHUN']
flat_type_options = ['1', '3', '4', '5', '2', 'MULTI-GENERATION']
flat_model_options = ['Normal', '3GEN', 'MODEL A', 'Duplexes', 'APARTMENT', 'TERRACE',
                      '2-ROOM', 'MODEL A2', 'TYPE S1', 'TYPE S2']
storey_range_options = ['12', '06', '09', '03', '15', '21', '18', '27', '24', '30', '33',
                        '42', '39', '36', '48', '45', '51']
lease_commence_date_options = [1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
                               1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 
                               1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 
                               1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                               2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                               2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
availabe_year=[1990,1991,1992,1993,1994,1995,1996, 1997, 1998, 1999, 2000,
               2001,2002, 2003, 2004, 2005,2006, 2007, 2008, 2009, 2010, 
               2011, 2012, 2013, 2014, 2015,2016, 2017, 2018, 2019, 2020, 
               2021, 2022, 2023]

# Encoders
town_encoder = OrdinalEncoder().fit(np.array(town_options).reshape(-1, 1))
flat_type_encoder = OrdinalEncoder().fit(np.array(flat_type_options).reshape(-1, 1))
flat_model_encoder = OrdinalEncoder().fit(np.array(flat_model_options).reshape(-1, 1))

# Function to get user input
def get_user_input():
    A_year = st.selectbox('Year', availabe_year)
    town = st.selectbox('Select Town', town_options)
    flat_type = st.selectbox('Select Flat Type', flat_type_options)
    storey_range = st.number_input('Select Storey Range 0 to 51', min_value=0, max_value=51, value=2)
    floor_area_sqm = st.number_input('Floor Area (sqm)', min_value=0, value=50)
    flat_model = st.selectbox('Select Flat Model', flat_model_options)
    lease_commence_date = st.selectbox('Lease Commence Year', lease_commence_date_options)
    remaining_lease = st.number_input('Remaining Lease', min_value=0, max_value=1173, value=50)

    # Transform categorical inputs
    town_encoded = town_encoder.transform(np.array([town]).reshape(-1, 1)).flatten()[0]
    flat_type_encoded = flat_type_encoder.transform(np.array([flat_type]).reshape(-1, 1)).flatten()[0]
    flat_model_encoded = flat_model_encoder.transform(np.array([flat_model]).reshape(-1, 1)).flatten()[0]

    # Create input array
    user_input = np.array([[A_year, town_encoded, flat_type_encoded, storey_range, floor_area_sqm, flat_model_encoded, lease_commence_date, remaining_lease]])
    return user_input

# Get user input
user_input = get_user_input()

# Placeholder for the prediction result
if st.button('Predict Resale Price'):
    # Make prediction
    prediction = model.predict(user_input)
    st.write(f'The predicted resale price is: {prediction[0]:.2f}')
