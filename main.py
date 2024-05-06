import streamlit as st
import numpy as np
import pandas as pd

regions = ['North', 'East', 'West', 'South']
codes = ['N', 'E', 'W', 'S']
code_dict = {r:c for r,c in zip(regions, codes)}

st.title('my first demo stramlit app !!')
# Selection box 
# first argument takes the titleof the selectionbox
# second argument takes options

region = st.selectbox("Region: ",
                     regions)

st.write(f"Your region code is: {code_dict[region]}")





map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
