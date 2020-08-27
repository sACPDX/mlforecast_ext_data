# External Data - FRED API (Fed Data)

import streamlit as st
#import streamlit.components.v1 as components                # New 7/27/2020

# Exploratory Data Analysis (EDA) Packages
#import pandas as pd
#import numpy as np

#import datapungi_fed as dpf

from PIL import Image
image = Image.open('mlf_pic_st_pete_port_cranes.jpg')
st.image(image, caption='Skiing Timberline',
          use_column_width=True)
#st.image("PCJH9833.JPG")

#data = dpf('gdp') 
#print(data)
#print(dpf)         #suggests to run data = dpf.data()

#data = dpf.data()
#print(data)        #list the database groups (eg. geo) and short description of each

#print(data.geo)    #list the databases in the groups, their short descriptions and parameters
#print(data.categories)    
#print(data.series)     