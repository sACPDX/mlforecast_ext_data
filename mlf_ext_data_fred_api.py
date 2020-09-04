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

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Function:  Create the PostGres table with GDP data
def create_GDP_data_table(data_gdp):
    DATABASE_URL = os.environ['DATABASE_URL']
    st.write("DATABASE_URL",DATABASE_URL)

#    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Format of table is date, gdp
    engine = sqlalchemy.create_engine(os.environ.get("DATABASE_URL"))
    con = engine.connect()
    mlf_table_name = "mlf_GDP"
    
    try:
        data_gdp.to_sql(mlf_table_name, con=engine, if_exists='replace')
    except (Exception, psycopg2.DatabaseError) as error:
        st.write(error)
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
data_gdp.index.name = 'date'
st.write("data_gdp retrieved from Fred:", data_gdp)

# Load data to table
create_GDP_data_table(data_gdp)

# End