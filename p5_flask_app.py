from flask import Flask, Response, request, render_template, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from hmmlearn import hmm
import warnings
import io
import base64

# initialize the flask app
app = Flask('State COVID App')

@app.route('/')
def home():
    img = io.BytesIO()

    np.random.seed(22)
    x = np.linspace(0,1,100)
    y = 5*x + 10 + np.random.normal(size=100)
    plt.plot(x,y,'o')

    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    name = 'Varun'

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

def thing():
    return f"""
        <html>
            <body>
                <h1>This is a hard-coded page bruh!</h1>
                <p>This is some hard coded {name} content</p>
            <body>
        <html>
    """

# route 5: accept the form submission and do something fancy with it
@app.route('/submit')
def make_predictions():
    # load in the form data from the incoming request
    user_input = request.args
    
    state = user_input('State: ')
    n_components = user_input('How many superspreaders do you think have happened?')
    metric = user_input('Metric: Cases or Deaths?').lower()


    model = pickle.load(open('assets/model.p', 'rb'))
    pred = model.predict(X_test)
    pred = pred[0]
    
    return render_template('results.html',prediction=pred)
    #return jsonify({'prediction':pred})
# manipulate data into a format that we pass to our model


if __name__ == '__main__':
    app.run(debug=True)