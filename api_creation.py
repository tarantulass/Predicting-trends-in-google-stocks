#following code should  be used for obtaining get request after we provide an input via inverse scaling of the test set.
from flask import Flask,request,jsonify
import joblib
import pandas as pd

#create a flask app
app = Flask(__name__)

@app.route('/predict',methods = ['POST'])
def predict():
	data = request.json
	df = pd.DataFrame(data)
	prediction = list(rnn.predict(x_testapi))

	return jsonify({'prediction':str(prediction)})

if __name__ == 'main':
	model = joblib.load('rnn_model_stocks.pkl')

	app.run(debug = True)
