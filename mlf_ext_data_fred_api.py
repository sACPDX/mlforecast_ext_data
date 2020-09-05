# External Data - FRED API (Fed Data)

import streamlit as st
#import streamlit.components.v1 as components                # New 7/27/2020

# Exploratory Data Analysis (EDA) Packages
import pandas as pd
import numpy as np


# API Library for Fed Data
# https://github.com/jjotterson/datapungi_fed/blob/master/README.md

import datapungi_fed as dpf

#  Database on Heroku:  Created postgresql-tapered-56936 as DATABASE_URL
import os
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Function:  Create the PostGres table with GDP data
def create_Fed_data_table(data_table, mlf_table_name):
#def create_GDP_data_table(data_gdp):
    DATABASE_URL = os.environ['DATABASE_URL']
    #st.write("DATABASE_URL",DATABASE_URL)

#    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Format of table is date, gdp
    engine = sqlalchemy.create_engine(os.environ.get("DATABASE_URL"))
    con = engine.connect()
    #mlf_table_name = "mlf_GDP"
    
    try:
        data_table.to_sql(mlf_table_name, con=engine, if_exists='replace')
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

# Sample Query of All Database Groups - Default Databases
data_list = data.datasetlist()    
st.write("data_list", data_list)

data_categories = data.categories(125) 
st.write("data_categories")  

data_releases = data.releases()
st.write("data_releases", data_releases)

data.series('GDP')
data.sources('1')   
data.tags(tag_names='monetary+aggregates;weekly')
data.geo(series_id='WIPCPI')

##############################################################################################################
#
# GDP - US
#
##############################################################################################################

data_gdp = data.series('gdp')
data_gdp.index.name = 'date'
st.write("GDP", data_gdp)

mlf_table_name = "mlf_GDP"

# Load data to table
create_Fed_data_table(data_gdp, mlf_table_name)


##############################################################################################################
#
# CPI - CPIAUCSL
#
#   Size:  <1K (250)
# 
#
##############################################################################################################

data_CPIAUCSL = data.series('CPIAUCSL')
st.write("CPI - CPIAUCSL", data_CPIAUCSL)

mlf_table_name = "mlf_CPIAUCSL"

# Load data to table
create_Fed_data_table(data_CPIAUCSL, mlf_table_name)


##############################################################################################################
#
# T10YIE - 10-Year Breakeven Inflation Rate (T10YIE)
#
#   Size: 4.5K
#
# Suggested Citation:
#   Federal Reserve Bank of St. Louis, 10-Year Breakeven Inflation Rate [T10YIE], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/T10YIE, September 4, 2020.
#
##############################################################################################################

data_T10YIE = data.series('T10YIE')
st.write("10-Year Breakeven Inflation Rate (T10YIE)", data_T10YIE)

mlf_table_name = "data_T10YIE"

# Load data to table
#create_Fed_data_table(data_T10YIE, mlf_table_name)


##############################################################################################################
#
# Unemployment Rate - US - UNRATE
#
#   Size:  <1K
# 
#
##############################################################################################################

data_UNRATE = data.series('UNRATE')
st.write("Unemployment Rate - US - UNRATE", data_UNRATE)

mlf_table_name = "data_UNRATE"

# Load data to table
create_Fed_data_table(data_UNRATE, mlf_table_name)

##############################################################################################################
#
# M2 Money Supply
#
#   Size:  2.1K
#
##############################################################################################################

data_M2 = data.series('M2')
st.write("M2 Money Supply", data_M2)

mlf_table_name = "data_M2"

# Load data to table
#create_Fed_data_table(data_M2, mlf_table_name)


##############################################################################################################
#
# DEXUSEU - US dollars for Euro - U.S. / Euro Foreign Exchange Rate
#
#   Size:  5.5K
#
##############################################################################################################

data_DEXUSEU = data.series('DEXUSEU')
st.write("DEXUSEU - US dollars for Euro - U.S. / Euro Foreign Exchange Rate", data_DEXUSEU)

mlf_table_name = "data_DEXUSEU"

# Load data to table
#create_Fed_data_table(data_DEXUSEU, mlf_table_name)


##############################################################################################################
#
# UMCSENT - University of Michigan: Consumer Sentiment
#
#   Size:  <1K
# 
# This data should be cited as follows: "Surveys of Consumers, University of Michigan, University of Michigan: Consumer Sentiment © [UMCSENT], retrieved from FRED, Federal Reserve Bank of St. Louis, (Accessed on date)"
# Copyright, 2016, Surveys of Consumers, University of Michigan. Reprinted with permission.
#
# Suggested Citation:
# University of Michigan, University of Michigan: Consumer Sentiment [UMCSENT], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/UMCSENT, September 4, 2020.
##############################################################################################################

data_UMCSENT = data.series('UMCSENT')
st.write("UMCSENT - University of Michigan: Consumer Sentiment", data_UMCSENT)

mlf_table_name = "data_UMCSENT"

# Load data to table
create_Fed_data_table(data_UMCSENT, mlf_table_name)


##############################################################################################################
#
# DGS10 - 10-Year Treasury Constant Maturity Rate
#
#   Size:  15K
#
# Suggested Citation:
#   Board of Governors of the Federal Reserve System (US), 10-Year Treasury Constant Maturity Rate [DGS10], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS10, September 4, 2020.
#
##############################################################################################################

data_DGS10 = data.series('DGS10')
st.write("DGS10 - 10-Year Treasury Constant Maturity Rate", data_DGS10)

mlf_table_name = "data_DGS10"

# Load data to table
#create_Fed_data_table(data_DGS10, mlf_table_name)


##############################################################################################################
#
# S&P 500 (SP500)
#
#   Size: 2.5K
#
# Suggested Citation:
#   S&P Dow Jones Indices LLC, S&P 500 [SP500], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/SP500, September 4, 2020.
#
##############################################################################################################

data_SP500 = data.series('SP500')
st.write("S&P 500 (SP500)", data_SP500)

mlf_table_name = "data_SP500"

# Load data to table
create_Fed_data_table(data_SP500, mlf_table_name)


##############################################################################################################
#
# Median Sales Price of Houses Sold for the United States (MSPUS)
#
#   Size: <1K
#
# Suggested Citation:
#   U.S. Census Bureau and U.S. Department of Housing and Urban Development, Median Sales Price of Houses Sold for the United States [MSPUS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MSPUS, September 4, 2020.
#
##############################################################################################################

data_MSPUS = data.series('MSPUS')
st.write("Median Sales Price of Houses Sold for the United States (MSPUS)", data_MSPUS)

mlf_table_name = "data_MSPUS"

# Load data to table
create_Fed_data_table(data_MSPUS, mlf_table_name)


##############################################################################################################
#
# Gold Fixing Price 10:30 A.M. (London time) in London Bullion Market, based in U.S. Dollars (GOLDAMGBD228NLBM)
#
#   Size:  13.5K
#
# Suggested Citation:
#   ICE Benchmark Administration Limited (IBA), Gold Fixing Price 10:30 A.M. (London time) in London Bullion Market, based in U.S. Dollars [GOLDAMGBD228NLBM], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/GOLDAMGBD228NLBM, September 4, 2020.#
#
##############################################################################################################

data_GOLDAMGBD228NLBM = data.series('GOLDAMGBD228NLBM')
st.write("Gold Fixing Price 10:30 A.M. (London time) in London Bullion Market, based in U.S. Dollars (GOLDAMGBD228NLBM)", data_GOLDAMGBD228NLBM)

mlf_table_name = "data_GOLDAMGBD228NLBM"

# Load data to table
#create_Fed_data_table(data_GOLDAMGBD228NLBM, mlf_table_name)


# End