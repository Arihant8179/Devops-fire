from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('forest_fire.html')  # Just the template name, not full path

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        int_features = [float(x) for x in request.form.values()]  # Changed to float for decimal values
        final = [np.array(int_features)]
        print(int_features)
        print(final)
        prediction = model.predict_proba(final)
        output = '{0:.{1}f}'.format(prediction[0][1], 2)

        if float(output) > 0.5:
            return render_template('forest_fire.html',
                                pred='Your Forest is in Danger.\nProbability of fire occurring is {}'.format(output),
                                bhai="Forest is in Danger.")
        else:
            return render_template('forest_fire.html',
                                pred='Your Forest is safe.\nProbability of fire occurring is {}'.format(output),
                                bhai="Your Forest is Safe for now")
    except Exception as e:
        return render_template('forest_fire.html',
                             pred='An error occurred: {}'.format(str(e)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
