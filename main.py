
from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:5173",  # Vite dev server
            "http://localhost:3000",
            "https://disease-prediction-app.vercel.app"  # Replace with your actual frontend domain,
                "*",
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Range", "X-Content-Range"],
        "supports_credentials": True,
        "max_age": 600
    }
})
@app.after_request
def after_request(response):
    allowed_origins = ['http://localhost:5173', 
                       '*',
                      'https://disease-prediction-app.vercel.app']
    origin = request.headers.get('Origin')
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def home():
    return "Welcome to the Emotion Prediction API!"

# @app.route('/heartpredict', methods=['POST'])
# def predict_heart_route():
#     try:
#         # Parse JSON input
#         data = request.get_json()
#         if not data or not isinstance(data, dict):
#             return jsonify({'error': 'Invalid input data'}), 400

#         # Call prediction function
#         heart_result = predict_disease_heart(data)

#         # Check for errors in the result
#         if 'error' in heart_result:
#             return jsonify(heart_result), 400

#         return jsonify(heart_result)
#     except Exception as e:
#         app.logger.error(f"Error in /heartpredict: {str(e)}")
#         return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)