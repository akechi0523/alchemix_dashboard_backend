# import json
from flask import Flask
from main_script import fetch_data
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
data = fetch_data()

@app.route('/data')
@cross_origin()
def get_json_data():
    # data1 = json.dumps(data, sort_keys=False)
    data1 = {'messsge':"Hello"}
    return data1

# if __name__ == '__main__':
#     app.run()

