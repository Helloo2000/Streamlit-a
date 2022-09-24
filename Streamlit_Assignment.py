#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import numpy as np
#import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.io as pio
import plotly.express as px
import plotly.offline as po
import plotly.graph_objects as go
#get_ipython().run_line_magic('matplotlib', 'inline')

#from plotly.offline import download_plotlyjs
#from plotly.offline import init_notebook_mode
#from plotly.offline import plot
#from plotly.offline import iplot
#pio.renderers.default = 'iframe'
#po.init_notebook_mode()
#cf.go_offline()
header = st.container()
dataset1 = st.container()
text1 = st.container()
dataset2 = st.container()
dataset3 = st.container()
dataset4 = st.container()
dataset5 = st.container()
text2 = st.container()
text3 = st.container()
text4 = st.container()
text5 = st.container()

# In[2]:
with header:
    st.title("# *Streamlit Assignment*")

with dataset1:
    st.header('Stocks Dataset')
    df_stocks = px.data.stocks()
    if st.checkbox('Show raw data', key = 'Stocks'):
        st.subheader('Raw data')
        st.write(df_stocks)
    
    


# In[3]:


#px.line(df_stocks, x = 'date', y = ['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT'], labels = {'x':'Date', 'y':'Price'},
#        title = 'Stock Competitors')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.GOOG, mode = 'lines+markers', name = 'Google'))
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.FB, mode = 'lines+markers', name = 'Facebook'))
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.NFLX, mode = 'lines+markers', name = 'Netflix'))
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.MSFT, mode = 'lines+markers', name = 'Microsoft'))
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.AAPL, mode = 'lines+markers', name = 'Apple'))
    fig.add_trace(go.Scatter(x = df_stocks.date, y = df_stocks.AMZN, mode = 'lines+markers', name = 'Amazon'))
    fig

with text1:
    st.text('We can observe that all stocks went through fluctuations between *Jan 2018* and *Dec 2019* with predictions to *Jan 2020*' 
            'which shows Microsoft having the highest stocks at 1.8')
# In[4]:
with dataset2:
    st.header('Countries Dataset')
    df_eu = px.data.gapminder().query('continent == "Europe" and year == 2007 and pop > 2e6')

    if st.checkbox('Show raw data', key = 'EU'):
        st.subheader('Raw data')
        st.write(df_eu)


    # In[5]:


    fig = px.bar(df_eu, x = 'country', y = 'pop', text = 'pop', color = 'country')
    fig.update_traces(texttemplate = '%{text:.2s}', textposition = 'outside')
    fig.update_layout(uniformtext_minsize = 8)
    fig.update_layout(xaxis_tickangle = -45)
    fig


# In[6]:
with dataset3:
    st.header('Flower Dataset')
    df_iris = px.data.iris()
    
    if st.checkbox('Show raw data', key = 'Iris'):
        st.subheader('Raw data')
        st.write(df_iris)


    # In[7]:


    fig = px.scatter(df_iris, x = 'sepal_width', y = 'sepal_length', color = 'species', size = 'petal_length', 
            hover_data = ['petal_width'])
    fig

# In[8]:
with dataset4:
    st.header('Restaurant Dataset')
    df_tips = px.data.tips()
    
    if st.checkbox('Show raw data', key = 'Tips'):
        st.subheader('Raw data')
        st.write(df_tips)

    # In[11]:

    #fig = px.box(df_tips, x = 'sex', y = 'tip')
    
    fig = px.box(df_tips, x = 'day', y = 'tip', color = 'sex')
    fig
    #fig = px.box(df_tips, x = 'day', y = 'tip', color = 'sex')

# In[12]:
with dataset5:
    st.header('Flights Dataset')
    flights = sns.load_dataset('flights')
    if st.checkbox('Show raw data', key = 'Flights'):
        st.subheader('Raw data')
        st.write(flights)


    # In[13]:


    fig = px.line_3d(flights, x = 'year', y = 'month', z = 'passengers', color = 'year')
    fig