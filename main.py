import streamlit as st
import pandas as pd


st.title('my first demo stramlit app !!')

regions = ['North', 'East', 'West', 'South']
codes = ['N', 'E', 'W', 'S']

# Selection box 
# first argument takes the titleof the selectionbox
# second argument takes options

region = st.selectbox("Region: ",
                     regions)
 
code = {r:c for zip(regions, codes)}

regions = ['North', 'East', 'West', 'South']
codes = ['N', 'E', 'W', 'S']
 
code_dict = {r:c for r,c in zip(regions, codes)}

st.write(f"Your region code is: {code_dict['region']}")
