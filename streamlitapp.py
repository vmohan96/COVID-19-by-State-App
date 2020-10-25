import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.express as px
import pandas as pd
import numpy as np
import pickle

import matplotlib.pyplot as plt
plt.style.use('seaborn')
from hmmlearn import hmm
import warnings

from plotfunction import plot_hmm_px

st.title('Daily Change in COVID cases')
st.subheader('Plot the daily change in COVID cases for any states, and apply an HMM plot to it. ')
st.header(' ')

df = pd.read_csv('./us-states.csv')
st.dataframe(df.head())

state = (st.text_input("Input the state", 'Missouri'))
metric = str.lower(st.text_input("Input Metric", 'Cases'))
dates_of_interest = (st.text_input("Input Dates you think had Superspreaders", ['2020-09-10']))
hmm_plot = (st.text_input("Do you want to see an HMM Plot? Input Yes or No", 'No'))
n_components = int(st.text_input("How many superspreaders do you think there were?", 3))

#user_input = np.array([state, metric, dates_of_interest, hmm_plot,n_components])
#user_input

#state1,metric1,dates_of_interest1,hmm_plot1,n_components1

fig = plot_hmm_px(state=state, 
                metric=metric, 
                dates_of_interest=dates_of_interest, 
                hmm_plot=hmm_plot, 
                n_components=n_components)
fig