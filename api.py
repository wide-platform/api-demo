from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/good')

def home():
	return("hare is good buy")
	


@app.route('/',methods=['POST'])                   
def bmi():
	data=request.get_json()
	name=data['name']
	weight=data['weight'] #in kg
	height=data['height'] #in m
	res=(int(weight)/(float(height)*float(height)))

	if res<20:
		return(jsonify({"bmi (you are lean) ":res}))
	elif res>25:
		return(jsonify({"bmi (you are fat) ":res}))
	else :			
		return(jsonify({"bmi (you are normal) ":res}))



@app.route('/name',methods=['GET'])
def name():
	name = "reha"
	return(name)
	 
	 
	 
	 
app.run(port=1000)

if __name__=="main":
 app.run(debug=True,port=1000)
