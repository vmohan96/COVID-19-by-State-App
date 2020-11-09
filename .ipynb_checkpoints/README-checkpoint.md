# Visualizing COVID-19 For Any U.S. State

### This application has now been deployed to Heroku, and can be accessed here:
- [Heroku App: COVID-19 By U.S. State](https://covid-by-state.herokuapp.com/)

The following is a Streamlit Application that allows the user to plot COVID-related metrics from mid-February to the last week of October, for any of the 50 states. This function also serves as the backend for my Streamlit App: 'covid-by-state.' 

The parameters decided by the user are as follows:
- **state:** (String) The user inputs one of the 50 states to be observed over the entire time period of the dataset.

- **metric:** (String) The user inputs their desired metric (cases or deaths) to be displayed over this period.

- **date_of_interest**: (DateTime) One or more specific dates on which there may have been superspreader events in the user's inputted state. This plots a vertical line onto the plot at that date index.

- **fig_type:** (String) The user indicates in which format they want to see the metric data. The options are:
    - Cumulative Daily Change: The graph will show the total cases/deaths for each day in the inputted state.
    - Relative Daily Change: The graph will show only NEW cases/deaths reported for each day.
    - Relative Normalized Daily Change: Same as Relative Daily Change, but normalized to a maximum value of 1.0. This is done to accommodate an HMM fit and plot on top of the graph.
    
- **hmm_plot:** (Boolean) The user indicates whether they would like a Hidden Markov Model to be fitted and plotted to the graph. This allows the user to observe notable changes in the shape of the progression curve for the given metric, and also observe potential connections between these regimes and superspreader events. Note that this will only fit and plot to the graph if fig_type = Relative Normalized Daily Change.

- **n_components:** (Integer) The hyperparameter for the HMM indicating the number of regimes to split the curve

- Test

