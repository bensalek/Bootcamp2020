# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmdBCe3AOGqA_e4Ccj-AtgQ-yHJdq4Dw
"""

from flask import Flask, request, jsonify, render_template

import numpy as np
import pickle
import os

#app name
app = Flask(__name__)

#load the saved model
def load_model():
  return pickle.load(open('Loan_model.pkl','rb'))

#home page
@app.route('/')
def home():
  return render_template('index.html')

#predict the result and return it
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = XGmodel.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))