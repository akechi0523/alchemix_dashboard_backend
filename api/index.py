import json
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
# from template.main_script import fetch_data
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://alchemix-dashboard-frontend.vercel.app/"}})

# fetch_data()

# Function to convert boolean values to strings
def convert_booleans_to_strings(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_booleans_to_strings(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], bool):
                data[i] = str(data[i])
            elif isinstance(data[i], list):
                data[i] = convert_booleans_to_strings(data[i])
    elif isinstance(data, bool):
        data = str(data)
    return data

@app.route('/api/data')
@cross_origin()
def get_json_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
    converted_data = convert_booleans_to_strings(data)
    data1 = json.dumps(converted_data, sort_keys=False)
    return data1

# scheduler = BackgroundScheduler()
# scheduler.add_job(fetch_data, 'interval', hours=2)
# scheduler.start()

if __name__ == '__main__':
    app.run()