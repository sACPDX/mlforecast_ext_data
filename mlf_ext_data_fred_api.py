# External Data - FRED API (Fed Data)

import streamlit as st
#import streamlit.components.v1 as components                # New 7/27/2020

# Exploratory Data Analysis (EDA) Packages
import pandas as pd
import numpy as np

import datapungi_fed as dpf

#  Database on Heroku:  Created postgresql-tapered-56936 as DATABASE_URL
import os
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']

#from PIL import Image
#image = Image.open('mlf_pic_st_pete_port_cranes.jpg')
#st.image(image, caption='Skiing Timberline',
#          use_column_width=True)
#st.image("PCJH9833.JPG")

# Function:  Create the PostGres table with GDP data
def create_GDP_data_table(data_gdp):
    DATABASE_URL = os.environ['DATABASE_URL']

    print("DATABASE_URL")
    print(DATABASE_URL)

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Format of table is date, gdp
    engine = sqlalchemy.create_engine(os.environ.get("DATABASE_URL"))
    con = engine.connect()
    
    try:
        data_gdp.to_sql((mlf_GDP), con=engine, if_exists='replace')
    except (Exception, psycopg2.DatabaseError) as error:
        st.write(error)
        print(error)
    finally:
        if con is not None:
            con.close()
    return


##############################################################################################################
#
# MAIN Loop
#
##############################################################################################################

st.subheader("RUNNING PROGRAM:  mfl_ext_data_fred_api.py")

API_KEY_FED = '50fd3ebc3029aaa14a6b183e2d84f288'
data = dpf.data("50fd3ebc3029aaa14a6b183e2d84f288")

data_gdp = data.series('gdp')
#data_gdp = data

print(data_gdp)
st.write("data_gdp retrieved from Fred:", data_gdp)


# Load data to table
create_GDP_data_table(data_gdp)


#data = dpf.data()
#print(data)        #list the database groups (eg. geo) and short description of each

#print(data.geo)    #list the databases in the groups, their short descriptions and parameters
#print(data.categories)    
#print(data.series)     