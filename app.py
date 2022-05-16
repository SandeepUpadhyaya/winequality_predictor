import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("wine_retrained.pkl")



@app.route('/')
def home():
    return render_template('index.html')
print("good to go yes yes")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 3)

    return render_template('index.html', prediction_text='Wine quality  {}'.format(output))




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)