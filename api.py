
# API TO CALCULATE BMI WITH WEIGHT IN KG & HEIGHT IN METERS

from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/')
def hello():
	return "WELCOME TO BMI CALCULATION"
	
	
# GET METHOD	
@app.route("/getbmi", methods=['GET'])
def get():
	height = input("Input your height in Meters: ")
	weight = input("Input your weight in Kilogram: ")
	return jsonify(height,weight)


# POST METHOD	
@app.route("/postbmi", methods=['POST'])
def post():
	data = request.get_json()
	height = data['height']
	weight = data['weight']
	result = float(weight/(height*height))
	return jsonify("BMI IS:",result)

if __name__ == "_main_":
	app.run(debug=True)
