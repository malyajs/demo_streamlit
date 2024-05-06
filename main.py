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


import plotly.express as px

df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='active cases',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()
