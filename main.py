import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

from hmmlearn import hmm
import warnings

from plotfunction import plot_hmm_px

st.title('Visualize COVID-19 Progression for any U.S. State')
st.subheader('Plot cumulative, relative, and relative normalized daily changes in COVID-19 cases or deaths for any state, and apply an HMM plot to a relative normalized plot. ')
st.subheader('Input Paramters Below to Generate a Plot at the Bottom:')


fig_type = st.selectbox('What kind of Figure? (Note: HMM Fit only on Normalized Daily Change)',('Cumulative Daily Change','Relative Daily Change','Relative Normalized Daily Change'))
state = st.selectbox('Input Your State of Interest',('Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming'))

d = datetime.date(2020, 7, 4)
metric = st.selectbox('Input a Metric',('Cases', 'Deaths'))
date1 = st.date_input('Input the date for a Superspreader event in this state',d)
hmm_plot = st.selectbox("Do you want to see an HMM Plot?",('No','Yes'))
n_components = int(st.text_input("How many HMM components?", 2))

fig = plot_hmm_px(state=state, 
                metric=metric.lower(), 
                dates_of_interest=[date1], 
                hmm_plot=hmm_plot, 
                n_components=n_components,
                fig_type = fig_type)
fig


st.subheader('')