import flask
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import sklearn
import pickle

with open("MLR_MODEL.pkl","rb") as p:
    m = pickle.load(p)

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    r_dspend=request.form["R&Dspend"]
    Administration=request.form["Administration"]
    Marketing=request.form["Marketing"]
    State=request.form["State"]
    sol=m.predict([r_dspend,Administration,Marketing,State]).reshape(-1,1)
    return render_template("index.html",prediction_test=sol)
if __name__ == "__main__":
    app.run(debug=True)