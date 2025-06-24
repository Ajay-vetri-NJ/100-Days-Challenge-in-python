import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, iterations=1000, learning_rate=0.01):
    m, n = X.shape
    W = np.zeros(n)
    for i in range(iterations):
        z = np.dot(X, W)
        y_pred = sigmoid(z)
        error = y_pred - y
        gradient = np.dot(X.T, error) / m
        W -= learning_rate * gradient
    return W

X = np.random.rand(100, 3)
y = (np.dot(X, [3, 1, 2]) + np.random.randn(100) > 0).astype(int)
weights = logistic_regression(X, y, iterations=2000, learning_rate=0.05)
print("Logistic Regression Weights:", weights)
