# Making it a web API
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Allows for access from other sites
app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin(origin='*')
def run():
    gender = request.form.get('gender')
    age = request.form.get('age')
    education = request.form.get('education')
    return {"data": gender + age + education}

app.run()