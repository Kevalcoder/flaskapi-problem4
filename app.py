from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load('model.joblib')

app = Flask(__name__)

# Define the predict API endpoint
@app.route('/predict', methods=['GET'])
def predict():
    # Get the input values from the request query parameters
    vol_moving_avg = request.args.get('vol_moving_avg')
    adj_close_rolling_med = request.args.get('adj_close_rolling_med')

    # Convert the input values to floats
    vol_moving_avg = float(vol_moving_avg)
    adj_close_rolling_med = float(adj_close_rolling_med)

    # Make a prediction using the trained model
    prediction = int(model.predict([[vol_moving_avg, adj_close_rolling_med]])[0])

    # Return the prediction as a JSON response
    return jsonify(prediction)

if __name__ == '__main__':
    app.run()
