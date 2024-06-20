from flask import Flask, request, url_for, redirect, render_template
import pickle

import numpy as np

app = Flask(__name__, template_folder='./templates', static_folder='./static')

model = pickle.load(open('random_forest_regression_model.pkl', 'rb')) 
    
@app.route('/')

def hello_world():
    return render_template('Index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    NorthWest=request.form['NorthWest']
    SouthWest=request.form['SouthWest']
    NorthEast=request.form['NorthEast']
    SouthEast=request.form['SouthEast']
    
    NorthWest=float(NorthWest)
    SouthWest=float(SouthWest)
    NorthEast=float(NorthEast)
    SouthEast=float(SouthEast)
 
    
   
 



    #features = [int(x) for x in request.form.values()]
    features =  np.array(['NorthWest', 'SouthWest', 'NorthEast', 'SouthEast'])


    print("features:", features)
    final = np.array(features).reshape((2,4))
    print(final)
    pred = model.predict(final)[0]
    print(pred)
    


    
    if pred < 0:
        return render_template('Index.html', pred='Error calculating Amount!')
    else:
        return render_template('Index.html', pred='Expected amount is {0:.3f}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)
