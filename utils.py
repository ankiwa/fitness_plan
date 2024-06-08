import pickle
import json
import config
import numpy as np

class FitnessPlan():

    def __init__(self, weight, height, bmi, gender, age, bmicase) :
        self.weight = weight
        self.height = height
        self.bmi = bmi
        self.gender = gender
        self.age = age
        self.bmicase = 'bmicase_' + bmicase

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)

    def get_predicted_plan(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.weight
        test_array[1] = self.height
        test_array[2] = self.bmi
        test_array[3] = self.project_data['gender'][self.gender]
        test_array[4] = self.age
        bmicase_index = self.project_data['columns'].index(self.bmicase)
        test_array[bmicase_index] = 1
        print('Test_Array:', test_array)

        predicted_charges = self.model.predict([test_array])[0]
        print(f' Exercise Recomendation Plan is {int(predicted_charges)}')
        return predicted_charges


if __name__ == '__main__':
    weight = 92.08
    height = 1.76
    bmi	= 29.71
    gender = 'Female'
    age = 59.0
    bmicase = 'over weight'
    fit_plan = FitnessPlan(weight, height, bmi, gender, bmicase)
    fit_plan.get_predicted_plan()
