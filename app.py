from pycaret.regression import *
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
	payload = request.json
	columns = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors',
			   'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width',
			   'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size',
			   'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm',
			   'city-mpg', 'highway-mpg']
	df = pd.DataFrame(payload['data'], columns=columns)
	model = load_model('output/automobile_final')
	predictions = predict_model(model, df)
	return jsonify({
		'price': float(predictions[['prediction_label']].values[0][0])
	})


app.run()
