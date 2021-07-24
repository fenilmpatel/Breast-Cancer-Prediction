from flask import Flask,render_template,url_for,request
import numpy as np
import pandas as pd
import os
import pickle
model = pickle.load(open('knn.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index1.html',title='Home')

@app.route('/predict',methods=['POST'])
def predict():
    '''For rendering results on HTML GUI
    '''
    CT = request.form['Clump Thickness']
    UOCS = request.form['Uniformity of Cell Size']
    MA  = request.form['Marginal Adhesion']
    SECS = request.form['Single Epithelial Cell Size']
    BN =request.form['Bare Nuclei']
    BC = request.form['Bland Chromatin']
    NN = request.form['Normal Nucleoli']
    Mitoses = request.form['Mitoses']

    pred = pd.DataFrame(data={'Clump Thickness':[float(CT)],'Uniformity of Cell Size':[float(UOCS)] ,'Marginal Adhesion':[float(MA)],'Single Epithelial Cell Size':[float(SECS)],
                       'Bare Nuclei':[float(BN)],'Bland Chromatin':[float(BC)],'Normal Nucleoli': [float(NN)],'Mitoses' : [float(Mitoses)]})
    prediction = model.predict(pred)
    output = prediction[0] 
    if output > 0:
        
        return render_template('prediction.html')
    else:
        
        return render_template('prediction.html')
   
port = int(os.environ.get('PORT',5000))
if __name__ == "__main__":
    app.run(debug=1,host='0.0.0.0',port=port) # or True             
