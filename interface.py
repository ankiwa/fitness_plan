from flask import Flask, jsonify, request, render_template
import config
import numpy as np
from project_app.utils import FitnessPlan

app = Flask(__name__)

###################################################################################################################
######################################## Homepage API #############################################################
###################################################################################################################

@app.route('/')
def fitness_model():
    print('Welcome to the FItness Plan Model')
    return render_template('index.html')

###################################################################################################################
########################################## Model API ##############################################################
###################################################################################################################

@app.route('/predict_charges', methods = ['POST'])
def get_fitness_plan():
        data = request.form
        weight = eval(data['weight'])
        height = eval(data['height'])
        bmi = eval(data['bmi'])
        gender = data['gender']
        age = eval(data['age'])
        bmicase = data['bmicase']
        # print(f'Age=={age}, Sex=={sex}, BMI=={bmi}, Children=={children}, Smoker=={smoker}, Region=={region}')

        fit_plan = FitnessPlan(weight, height, bmi, gender, age, bmicase)
        plan = fit_plan.get_predicted_plan()
        return jsonify({'Result':f' Exercise Recomendation Plan is : {int(plan)}'})
        print(data)




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=True)