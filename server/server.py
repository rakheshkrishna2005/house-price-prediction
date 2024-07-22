from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# Route to get location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allowing cross-origin requests
    return response

# Route to predict home price
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Extracting data from the form
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Getting the estimated price from util function
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allowing cross-origin requests
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Loading saved artifacts for the prediction
    app.run()
