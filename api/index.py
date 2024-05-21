import json
from flask import Flask
from main_script import fetch_data
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

data = fetch_data()

@app.route('/data')
@cross_origin()
def get_json_data():
    # data = fetch_data()
    #Read the JSON file and return its contents
    # with open('data1.json') as f:
    #     data = json.load(f)
    data1 = json.dumps(data, sort_keys=False)
    return data1

if __name__ == '__main__':
    app.run()

