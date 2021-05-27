import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

from hmmlearn import hmm
import warnings
import datetime

#The function
@st.cache(allow_output_mutation=True)
def plot_hmm_px(state, metric='cases', dates_of_interest=None, hmm_plot=False, n_components=3, fig_type = 'Normalized Daily Change'):
    '''
    You can switch metric to 'deaths' if you want.

    '''
    # df = pd.read_csv('./us-states.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    state_df = df[df['state'] == state]
    state_df.drop(columns='state', inplace=True)
    state_df['date']= pd.to_datetime(state_df['date'])
    state_df.set_index('date', inplace=True)
    state_diff = state_df.diff()
    state_diff.dropna(inplace=True)
    X = state_diff[[metric]]
    Xcuml = state_df[[metric]]



    fig = px.line(X/(X.max() - X.min()),title=f'{state.title()} Daily COVID-19 {metric.capitalize()} Change, Normalized')
    fig_abs_change = px.line(X,title=f'{state.title()} Daily COVID-19 {metric.capitalize()} Change')
    fig_cuml_change = px.line(Xcuml,title=f'{state.title()} Daily Total COVID-19 {metric.capitalize()}')


    fig.update_xaxes(title_text='Date')
    fig_abs_change.update_xaxes(title_text='Date')
    fig_cuml_change.update_xaxes(title_text='Date')

    fig.update_yaxes(title_text=f'Daily New {metric.capitalize()}, Normalized')
    fig_abs_change.update_yaxes(title_text=f'Daily New {metric.capitalize()}')
    fig_cuml_change.update_yaxes(title_text=f'Total {metric.capitalize()}')


    if dates_of_interest:
        for date in dates_of_interest:
             fig.add_scatter(x=(date,date),y=(0,1.1),line={'color': f'rgb(0,0,0)','width': 2,}, name=f'Superspreader')
             fig_abs_change.add_scatter(x=(date,date),y=(0,X.max()[0]),line={'color': f'rgb(0,0,0)','width': 2,}, name='Superspreader')

    if (hmm_plot=='Yes'):
        model = hmm.GaussianHMM(n_components=n_components)
        model.fit(X)
        preds = model.predict(X) / 2
        fig.add_scatter(x=X.index, y=preds, name='Regime')

    if fig_type == 'Relative Normalized Daily Change':
        return fig
    elif fig_type == 'Relative Daily Change':
        return fig_abs_change
    elif fig_type == 'Cumulative Daily Change':
        return fig_cuml_change
