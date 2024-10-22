from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "messagecode": 200,
        "message": "Success",
        "day_level": [
            {
                "trans_date": "2024-10-22",
                "target": 16.0,
                "achieved": 21.0,
                "achieved_perc": 131.25,
                "color_code": 3.0
            },
            {
            "trans_date": "2024-10-24",
            "target": 180,
            "achieved": 9,
            "achieved_perc": 1,
            "color_code": 5.0
            },
            {
            "trans_date": "2024-10-22",
            "target": 16,
            "achieved": 21,
            "achieved_perc": 131,
            "color_code": 2.0
             },
            {
                "trans_date": "2024-10-21",
                "target": 18.0,
                "achieved": 23.0,
                "achieved_perc": 127.78,
                "color_code": 3.0
            }
        ]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)