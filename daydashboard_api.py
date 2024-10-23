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
                "trans_date": "2024-11-16",
                "target": 16,
                "achieved": 4,
                "achieved_perc": 33,
                "color_code": 2.0
            },
            {
                "trans_date": "2024-11-15",
                "target": 16,
                "achieved": 6,
                "achieved_perc": 45,
                "color_code": 5.0
            },
            {
                "trans_date": "2024-11-14",
                "target": 16,
                "achieved": 8,
                "achieved_perc": 60,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-13",
                "target": 16,
                "achieved": 10,
                "achieved_perc": 40,
                "color_code": 2.0
            },
            {
                "trans_date": "2024-11-12",
                "target": 16,
                "achieved": 21,
                "achieved_perc": 66,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-11",
                "target": 16,
                "achieved": 2,
                "achieved_perc": 131,
                "color_code": 5.0
            },
            {
                "trans_date": "2024-11-10",
                "target": 16,
                "achieved": 1,
                "achieved_perc": 1,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-09",
                "target": 16,
                "achieved": 2,
                "achieved_perc":43,
                "color_code": 2.0
            },
            {
                "trans_date": "2024-11-08",
                "target": 16,
                "achieved": 22,
                "achieved_perc": 131,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-07",
                "target": 16,
                "achieved": 10,
                "achieved_perc":3,
                "color_code": 2.0
            },
            {
                "trans_date": "2024-11-06",
                "target": 16,
                "achieved": 21,
                "achieved_perc": 57,
                "color_code": 5.0
            },
            {
                "trans_date": "2024-11-05",
                "target": 16,
                "achieved": 3,
                "achieved_perc": 77,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-04",
                "target": 16,
                "achieved": 25,
                "achieved_perc": 88,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-11-03",
                "target": 16,
                "achieved": 45,
                "achieved_perc": 98,
                "color_code": 3.0
            },
            # {
            #     "trans_date": "2024-11-02",
            #     "target": 16,
            #     "achieved": 33,
            #     "achieved_perc": 22,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-11-01",
            #     "target": 16,
            #     "achieved": 2,
            #     "achieved_perc": 23,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-10-31",
            #     "target": 16,
            #     "achieved":1,
            #     "achieved_perc": 55,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-10-30",
            #     "target": 16,
            #     "achieved": 21,
            #     "achieved_perc": 22,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-10-29",
            #     "target": 16,
            #     "achieved": 21,
            #     "achieved_perc": 33,
            #     "color_code": 3.0
            # },
            {
                "trans_date": "2024-10-28",
                "target": 16,
                "achieved": 21,
                "achieved_perc": 55,
                "color_code": 3.0
            },
            # {
            #     "trans_date": "2024-10-27",
            #     "target": 16,
            #     "achieved": 21,
            #     "achieved_perc": 77,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-10-26",
            #     "target": 16,
            #     "achieved": 21,
            #     "achieved_perc": 72,
            #     "color_code": 3.0
            # },
            # {
            #     "trans_date": "2024-10-25",
            #     "target": 16,
            #     "achieved": 21,
            #     "achieved_perc": 83,
            #     "color_code": 3.0
            # },
            {
                "trans_date": "2024-10-24",
                "target": 16,
                "achieved": 21,
                "achieved_perc": 47,
                "color_code": 3.0
            },
            {
                "trans_date": "2024-10-23",
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
                "achieved_perc": 127,
                "color_code": 3.0
            }
        ]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)