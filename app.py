# Import kaun karega libraries
from flask import Flask ,request, jsonify, render_template
import pickle
import numpy as np

# Load karaycha apla model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Initialize karaycha Flask app
app = Flask(__name__)


# Define gharcha address route(main page)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict',methods= ['POST'])
def predict():
    # Extract data from the form
    int_features = [int(x) for x in request .form.values()]
    final_features = [np.array(int_features)]

    # Make Prediction
    prediction = model.predict(final_features)
    output = 'Placed' if prediction[0] == 1 else 'Not Placed'
     
    return render_template('index.html',prediction_text='Prediction:{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)