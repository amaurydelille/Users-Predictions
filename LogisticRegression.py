import math

class Logistic_Regression:
    def __init__(self, learning_rate=0.1, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def sigmoid(self, x):
        return 1.0 / (1 + math.exp(-x))

    def power(self, x, n):
        result = 1
        while (n > 0):
            result *= x
            n -= 1
        return result

    def fit(self, X, y):
        set, input = len(X), len(X[0]) #set: our data_set, input: the features of our set (age, gender, hours, etc...)
        self.weights = [0] * input
        self.bias = 0

        #gradient_descent
        for i in range(self.max_iter):
            y_pred = []
            for j in range(set):
                z = self.bias
                for k in range(input):
                    z += self.weights[k] * X[j][k]
                y_pred.append(self.sigmoid(z))

        #update weight and bias
        error = (y[j] - y_pred[j])
        self.bias += self.learning_rate * error

        for k in range(set):
            self.weights[k] = self.learning_rate * error * X[j][k]

        return self.weights, self.bias

    def predict(self, X):
        set, input = len(X), len(X[0])
        y_pred = []

        for i in range(set):
            z = self.bias
            for j in range(input):
                z += self.weights[j] * X[i][j]
            y_pred.append(self.sigmoid(z))

        return y_pred

