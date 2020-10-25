import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import pickle

import matplotlib.pyplot as plt
plt.style.use('seaborn')
from hmmlearn import hmm
import warnings
import matplotlib.pyplot as plt
from hmmlearn import hmm

#The function
@st.cache(allow_output_mutation=True)
def plot_hmm_px(state, metric='cases', dates_of_interest=None, hmm_plot=False, n_components=3):
    '''
    You can switch metric to 'deaths' if you want.
    
    '''
    df = pd.read_csv('./us-states.csv')
    state_df = df[df['state'] == state]
    state_df.drop(columns='state', inplace=True)
    state_df['date']= pd.to_datetime(state_df['date'])
    state_df.set_index('date', inplace=True)
    state_diff = state_df.diff()
    state_diff.dropna(inplace=True)
    X = state_diff[[metric]]


    #plt.figure(figsize=(14, 4))
    
    fig = px.line(X/(X.max() - X.min()),title=f'{state.title()} Daily COVID-19 {metric.capitalize()} Change')
    
    if dates_of_interest:
        i=0
        j=0
        k=0
        for date in dates_of_interest:
            fig.add_shape(type="line",x0 =date,x1=date,y0=0,y1=1.1)
            #fig.add_scatter(x=(date,date),y=(0,1.1),line={'color': f'rgb({i},{j},{k})','width': 2,}, name='Superspreader')
            #plt.axvline(x=date, label=date, color='black')
    
    if (hmm_plot=='Yes'):  
        model = hmm.GaussianHMM(n_components=n_components)
        model.fit(X)
        preds = model.predict(X) / 2
        fig.add_scatter(x=X.index, y=preds, name='Regime')
    
    return fig