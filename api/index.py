import json
import time
from flask import Flask
from .template.main_script import fetch_data
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://alchemix-dashboard-frontend.vercel.app/"}})
fetch_data()
time.sleep(60)
@app.route('/api/data')
@cross_origin()
def get_json_data():
    with open("data1.json", 'r') as f:
        data = json.load(f)
    data1 = json.dumps(data, sort_keys=False)
    return data1

if __name__ == '__main__':
    app.run()

