import numpy as np

def lasso_regression(X, y, alpha=1.0, iterations=1000, learning_rate=0.01):
    m, n = X.shape
    W = np.zeros(n)
    for i in range(iterations):
        y_pred = np.dot(X, W)
        error = y_pred - y
        gradient = np.dot(X.T, error) / m + alpha * np.sign(W)
        W -= learning_rate * gradient
    return W

X = np.random.rand(100, 3)
y = np.dot(X, [3, 1, 2]) + np.random.randn(100)
weights = lasso_regression(X, y, alpha=0.1)
print("Lasso Regression Weights:", weights)
