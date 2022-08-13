from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('linear.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictor():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predicted= model.predict(final_features)
    return render_template('index.html', predicted=f'the crime rate is {predicted}')

if __name__ == '__main__':
    app.run()