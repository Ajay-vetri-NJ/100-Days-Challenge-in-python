import numpy as np

def ridge_regression(X, y, alpha=1.0):
    n, m = X.shape
    I = np.eye(m)
    XTX = np.dot(X.T, X)
    ridge = np.linalg.inv(XTX + alpha * I)
    W = np.dot(ridge, np.dot(X.T, y))
    return W

X = np.random.rand(100, 3)
y = np.dot(X, [3, 1, 2]) + np.random.randn(100)
weights = ridge_regression(X, y, alpha=0.5)
print("Ridge Regression Weights:", weights)
