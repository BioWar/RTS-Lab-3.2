from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


def fit_train_perceptron(learning_rate, deadline, iterations):
    P = 4
    data = [(0, 6), (1, 5),
            (3, 3), (2, 4)]
    n = len(data[0])
    weights = [0.001, -0.004]
    outputs = [0, 0,    0, 1]

    for _ in range(iterations):
        total_err = 0
        for i in range(len(outputs)):
            prediction = predict(data[i], weights, P)
            err = outputs[i] - prediction
            total_err += err
            for j in range(n):
                delta = learning_rate * data[i][j] * err
                weights[j] += delta
        if total_err == 0:
            break
    return {'w_1': str(weights[0]),
            'w_2': str(weights[1])}


def predict(dot, weights, P):
    sum = 0
    for i in range(len(dot)):
        sum += weights[i] * dot[i]
    return 1 if sum > P else 0


class Container(GridLayout):
	def calculate(self):
		try:
			learning_rate, deadline, iterations = float(self.learning_rate.text), int(self.deadline.text), int(self.iterations.text)
		except:
			learning_rate, deadline, iterations = 0, 0, 0
		
		weights = fit_train_perceptron(learning_rate, deadline, iterations)
		self.w_1.text = weights.get('w_1')
		self.w_2.text = weights.get('w_2')


class MyApp(App):
	def build(self):
		return Container()

if __name__=='__main__':
	MyApp().run()
